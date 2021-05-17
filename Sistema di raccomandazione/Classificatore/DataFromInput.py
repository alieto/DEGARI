from pprint import *

# Classe per il parsing dell'input da file
# Per prima cosa salva tutte le linee del file su una lista
# Toglie quelle di commento e quelle vuote
# Salva in delle stringhe il titolo e i nomi del concetto head e modifier
# Infine scandisce le linee rimanenti creando due liste, 
#   una con le proprietà tipiche e una con quelle forti
class ReadAttributes :

    def __init__(self, path = 'Input') : 
        
        with open(path) as f:
            self.input_lines = f.readlines()

        self.input_lines = [x.strip() for x in self.input_lines 
                            if x.strip() != '' and x.strip()[0] != '#']
        

        self.title = self.input_lines[0].split(':')[1].strip()
        self.input_lines.pop(0)

        self.head_conc = self.input_lines[0].split(':')[1].strip()
        self.input_lines.pop(0)

        self.mod_conc = self.input_lines[0].split(':')[1].strip()
        self.input_lines.pop(0)

        self.tipical_attrs = []
        self.attrs = []
              
        for l in self.input_lines :
            l = [k.strip() for k in l.split(',')]
           
            if len(l) == 3 and l[0][0] == 'T':
                self.tipical_attrs.append(tuple([l[1],float(l[2]),
                            (True if l[0][2:-1] == 'head' else False) ]))
               
            if len(l) == 2:
                self.attrs.append(tuple([l[1],
                            (True if l[0] == 'head' else False) ]))

        self.result = self.input_lines[len(self.input_lines)-1].split(':')[1].strip()

