from pprint import *
from DataFromInput import *
from CreateOntology import *
import math

# Example list of attributes: 
#  The first argument is the attribute's name,
#  The second argument is the percentage,
#  The third argument is a boolean (isHead)
#   which explain if the attribute belongs 
#   to the head or to the modifier concept.
evil_chair = [("Demoniac",0.9,True),
        ("Opponent Hero",0.75,True),
        ("Protagonist",0.75,True),
        ("Impulsive",0.8,True),
        ("Has Back",0.95,False),
        ("Wood",0.65,False),
        ("Comfortable",0.8,False),
        ("Inflammable",0.7,False)]

ex_t = [("attr2",0.5,True), ("attr1",0.5,True)]
ex_not_t = [("-attr1",True)]


# Class Table
# L'obiettivo di questa classe e' di creare una tabella
#  che, data una lista con attributi e relative percentuali,
#  ne calcola le "combinazioni" e le inserisce nella tabella.
class Table:

    # Costruttore
    #  Salva la lista di attributi nel parametro tipical_attrs.
    #  Crea una "tabella di verità" (fatta di combinazioni di 0 e 1)
    #  Agginge alla tabella una colonna con ogni percentuale 
    #   calcolata sulla linea
    # AGGIUNTA RUBINETTI: maxAttrs
    def __init__(self, from_input, max_attrs=math.inf) :
        
        self.title = from_input.title
        self.h_conc = from_input.head_conc
        self.m_conc = from_input.mod_conc

        self.attrs = from_input.attrs
        self.tipical_attrs = from_input.tipical_attrs
        self.table = self.createTable(max_attrs)
        self.addPercentage()
        self.delNotConsistent()
        self.sorted_table = self.getSortedTable()

    # Metodo per creare le nostre tabelle di 0 e 1
    #  L'intuizione e' che nelle tabelle di verità, leggendo 
    #   ogni riga si possono leggere dei numeri binari;
    #   quindi basta riempire ogni riga con 0 e 1 corrispondenti
    #   al numero in binario della riga (partendo dalla riga 0)
    # AGGIUNTA RUBINETTI: maxAttrs
    def createTable(self, max_attrs=math.inf) :
        w, h = len(self.tipical_attrs), pow(2, len(self.tipical_attrs))

        # AGGIUNTA RUBINETTI: commentato questa riga
        #m = [self.to_binary(y, w) for y in range(h)]
        #


        # AGGIUNTA RUBINETTI
        m = []
        for y in range(h):
            bin = self.to_binary(y, w)

            # Conto il numero di '1' presenti in bin e
            # controllo che abbia il numero di '1' <= maxAttrs
            num1 = 0
            for bit in bin:
                if bit == '1':
                    num1 = num1 + 1
            if num1 <= max_attrs:
                m.append(bin)
        #

        return m

    # Metodo per calcolare il numero binario dato un numero
    #  in base 10
    # NB! se il numero occupa meno cifre del numero di colonne 
    #  che dovrà avere la tabella, aggiunge degli zeri in cima 
    #  alla lista della riga, finchè non risulta della lunghezza 
    #  appropriata.
    def to_binary(self, num, l) :
        bin = "{0:b}".format(num)
        bin_list = list(bin)
        while (len(bin_list) < l) : 
            bin_list = ['0'] + bin_list
        return bin_list


    # Metodo che per ogni linea calcola la percentuale
    #  Essendo le linee riempite con delle liste di 0 e 1
    #   questo metodo scandice ognuna di queste linee e 
    #   usa come valore da moltiplicare (in riferimento 
    #   alla lista di attributi tipical_attrs) 1-p (con p percentuale
    #   nella lista attr) se il valore incontrato è 0, p se il
    #   valore è 1.
    #  Una volta che ha moltiplicato tra loro tutti i valori della 
    #   linea, li moltiplica ancora per 100 e poi li aggiunge alla linea.
    def addPercentage(self) :
               
        for line in range(len(self.table)) :
            tot = 100
            for x in range(len(self.table[line])) :
                if (self.table[line][x] == '1') :
                    tot *= self.tipical_attrs[x][1] 
                else :
                    tot *= 1-self.tipical_attrs[x][1]

            self.table[line] += [tot]


    # Metodo che restituisce a tabella ordinata usando il metodo 
    #  ausiliario SortTable() che implementa un algoritmo di quick sort.
    def getSortedTable(self) :
        return self.sortTable(self.table)
        
    def sortTable(self, table) :
        less, equal, greater = [], [], []

        if len(table) > 1:
            line_len = len(table[0])
            pivot = table[0][line_len - 1]
            for x in table :
                if x[line_len-1] < pivot :
                    less.append(x)
                if x[line_len-1] == pivot :
                    equal.append(x)
                if x[line_len-1] > pivot :
                    greater.append(x)

            return self.sortTable(less)+equal+self.sortTable(greater)
        
        else :
            return table


    # Metodo che richiama ManageOntology e per ogni 
    #  scenario (linea della tabella) controlla che sia consistente
    #   Per prima cosa cancella gli scenari che prendono 
    #     tutte le proprietà e quelli che non ne prendono nessuna, perchè banali
    #   Poi per ogni riga della tabella crea un'ontologia e controlla 
    #     che sia consistente, in caso di risposta negativa la riga viene cancellata
    def delNotConsistent(self) :
        i = 0
        del self.table[-1]
        del self.table[0]

        while i < len(self.table) :     
            ont = ManageOntology(tipical_attrs = self.tipical_attrs, attrs = self.attrs, line = self.table[i])
            consistent = ont.is_consistent()
            print(str(consistent)+', '+str(self.table[i][:-1])+'\n\n\n')
            if not consistent :
                del self.table[i]
                i -= 1
            i += 1
        
'''

    def getSignificants(self) :
                
        resulting_scen = []

                
'''
    

if __name__ == "__main__" :
#    dict_of_attr = DataFromWeb.DictOfAttr()
    from_input = ReadAttributes()
    tab = Table(from_input)
    pprint(tab.table)
    pprint(tab.tipical_attrs)
    pprint(tab.attrs)





     
