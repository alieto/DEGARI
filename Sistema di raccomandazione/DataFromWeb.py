from collections import Counter
import pprint
import requests
from bs4 import BeautifulSoup
from string import ascii_uppercase as alphabet_upper


# Una classe il cui scopo e' calcolare la percentuale con cui
#  un attribute ricorre tra tutti i Villains della wikia disney

class DictOfAttr : 
    
    #Costruttore:
    # crea una lista attributes che poi li conterrà tutti,
    # tiene conto del numero di pagine con le variabili num_none_pages e num_tot_pages,
    # prende la lista di cattivi dal metodo getVillainsList(),
    # url_base composta poi con il nome del villain darà l'url della pagina web,
    # dict_of_attributes, inizialmente vuoto, sarà poi il nostro dictionary riempito (da setDict()) con le coppie (attribute : percentuale). 
    def __init__(self, url_base = "http://disney.wikia.com/wiki/") :
        self.attributes = []
        self.num_none_pages = 0
        self.url_list = self.getVillainsList()
        self.num_tot_pages = len(self.url_list)
        self.url_base = url_base
        self.dict_of_attributes = {}
        self.setDict() 
        self.sorted = self.getSortedDict() 
        self.wrt_on_file()

    # Prende in input l'url da cui partire e trova, in ordine alfabetico,
    #  il nome di ogni Villain che salverà in una lista.
    # Restituisce alla fine un set, composto da tutti gli elementi della lista,
    #  così da poter evitare anche eventuali doppioni.
    def getVillainsList(self, url = "http://disney.wikia.com/wiki/Category:Villains"): 
        sites = []
        prova = "a" #utile solo per fare prove sui primi 200 siti
        
        #for letter in alphabet_upper :
        for letter in prova : 
            html = requests.get(url+"?from="+letter).content
            soup = BeautifulSoup(html, "lxml")
            data = soup.find('div', {'class' : 'mw-content-ltr'})

            for ultag in data.find_all('ul'):
                for litag in ultag.find_all('li'):
                    if (litag.text[0] != '['):
                        sites.append(litag.text)

        return set(sites) #per eliminare eventuali doppioni
    
    # Prende in input l'url del sito parsificare, ne scarica
    #  l'html e poi all'interno dell'url cerca gli attributes
    #  riguardanti la personalità,salvandoli in una lista.
    # Infine cerca di formattare al meglio le stringhe degli 
    #  attributes e se la lista finale non è vuota la concatena
    #  con l'attributo self.attributes della classe. 
    # Se la lista risultante è invece vuota, allora incrementa il
    #  valore del contatore self.num_none_pages della classe. 
    def getOnePersonality(self, url) :
        personality = []
        html = requests.get(url).content
        print(url)
        soup = BeautifulSoup(html, 'lxml')
        data = soup('h3', {'class' : 'pi-data-label pi-secondary-font'})

        for title in data :
            if (title.string == "Personality") :
                x = title.next_sibling.next_sibling.string
                if (x is not None) : personality = x.split(',')
        
        #Formattare il testo
        for i in range  (len(personality)):
            personality[i] = personality[i].lower()
            if (personality[i].find(" and ")) :
                s = personality[i].split(" and ")
                personality.pop(i)
                personality+=s

            if (personality[i].startswith(" ")) :
                personality[i] = personality[i][1:]

            if (personality[i].startswith("and ")) :
                personality[i] = personality[i][4:]

            if (personality[i].startswith("a ")) :
                personality[i] = personality[i][2:]
    

        if (personality != []) :
            self.attributes += personality
        else :
            self.num_none_pages += 1

    # Come prima cosa richiama il metodo getOnePersonality per ogni villain,
    #  passandogli in input l'url composta da self.url_base e il nome del villain.
    # Subito dopo prende la lista con tutti gli attributi e usando Counter(),
    #  che era stato importato da collections, la trasforma in un dictionary
    #  composto da coppie { attribute : number_of_occurrence }.
    # Scorre il dictionary printandolo su un file e intando modificandone
    #  il contenuto così da ottenere infine delle coppie della forma
    #  { attribute : percentage_of_occurrence }
    def setDict(self):
        print(self.num_tot_pages)

        for name in self.url_list :
            self.getOnePersonality(self.url_base+name)

        self.dict_of_attributes = Counter(self.attributes)

        out_file = open("attributes.out", 'w')
        for key, val in self.dict_of_attributes.items():
            self.dict_of_attributes[key] = val/(self.num_tot_pages - self.num_none_pages)
            out_file.write(key + " : " +str(self.dict_of_attributes[key]) 
                    +", " + str(val) + "\n")

        out_file.close()
    
    # Restituisce il dizionario ordinato richiamando la funzione ausiliaria
    #  sortDict() che è un'implementazione del quicksort()
    def getSortedDict(self):
        return self.sortDict(list(self.dict_of_attributes.items()))

    def sortDict(self, attr) :
        less, equal, greater = [], [], []
        
        if (len(attr) > 1) :
            pivot = attr[0]
            for x in attr :
                if x[1] < pivot[1]:
                    less.append(x)
                if x[1] == pivot[1]:
                    equal.append(x)
                if x[1] > pivot[1]:
                    greater.append(x)

            return self.sortDict(less)+equal+self.sortDict(greater)

        else :
            return attr


    def wrt_on_file(self) :
        attrs = self.sorted[-5:]
        file = open('Input_data_from_web','w') 
         
        file.write("\x23 Just copy paste to the 'Input' file with the other concept you want to combine\n") 
        file.write("modifier concept name : evil\n")
        file.write("modifier,"+attrs[-1][0]+"\n")
        for x in attrs[:-1] :
            file.write("T(modifier),"+x[0]+","+str(x[1]+0.5)+"\n") 
         
        file.close() 




if __name__ == "__main__" :
    attr = DictOfAttr()
    pprint.pprint (attr.getSortedDict())

