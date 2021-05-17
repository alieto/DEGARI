import sys
import os

#Classe che rappresenta una proprietà tipica di un genere
class Property :
    name = ""
    prob = 0.0

    def __init__(self, name, prob):
        self.name = name
        self.prob = prob

#Classe per lettura del file di un GENERE
class ReaderFileProperty :

    #Ritorna la lista delle proprietà tipiche dal file indicato
    def getProperties(self, path_file) :    
        prop_list = []

        #Lettura file
        with open(path_file) as f:
            self.input_lines = f.readlines()
        
        #Inserimento proprietà tipiche
        for p in self.input_lines:
            prop = p.split(':')
            prob = float(prop[1].strip())
            x = Property(prop[0], round(prob,2))
            prop_list.append(x)
        return prop_list

#Funzione scrittura file di input per COCOS
def writeFile_COCOS(head, modifier, head_prop, modifier_prop):
    f = open("prototipi/"+ head + "_" + modifier, "w")
    f.write("#Title composizione\n")
    f.write("Title : " + head + "-" + modifier + "\n\n")
    f.write("#Concetto Principale\n")
    f.write("Head Concept Name : " + head + "\n\n")
    f.write("#Concetto Modificatore\n")
    f.write("Modifier Concept Name : " + modifier + "\n\n")
    
    #Proprietà Dure - Lettura dai file nella cartella genres/attr
    a = open("./genres_attr/" + head + ".txt", "r")
    for p in a :
        f.write("head, " + p)
    f.write("\n\n")
    
    a = open("./genres_attr/" + modifier + ".txt", "r")
    for p in a :
        f.write("modifier, " + p)
    f.write("\n\n")
    
    #Properietà Deboli
    for i in range(len(modifier_prop)) :
        f.write("T(modifier), " + modifier_prop[i].name + ", " + str(modifier_prop[i].prob) + "\n")
    f.write("\n")

    for i in range(len(head_prop)) :
       f.write("T(head), " + head_prop[i].name + ", " + str(head_prop[i].prob) + "\n")
    f.write("\n")
    f.close()

#Main : lettura generi da associare creativamente tramite argomento di linea di comando, lettura proprietà dai file, scrittura file per COCOS
if __name__ == '__main__' :
    head = ""
    modifier = ""
    #Lettura parametri, generi da trattare con COCOS
    if len(sys.argv) == 3 :
        head = sys.argv[1]
        modifier = sys.argv[2]

        #Lettura file
        f = ReaderFileProperty()
        head_prop = f.getProperties('genres/'+ head +'.txt')
        modifier_prop = f.getProperties('genres/'+ modifier +'.txt')
        
        #Scrittura file        
        writeFile_COCOS(head,modifier,head_prop,modifier_prop)
        
        #Esecuzione COCOS
        #print(creaScenario("prototipi/"+ head + "_" + modifier))
    else :
        print("Inserire i 2 generi come argomento!")


