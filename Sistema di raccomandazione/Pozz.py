import sys
#import gi
#gi.require_version('Gtk', '3.0')
#from gi.repository import Gtk

from DataFromInput import *
#from DataFromWeb import *
from MkTable import *
from Recommended import *

if __name__ == '__main__' :
    # AGGIUNTA RUBINETTI
    max_attrs = math.inf
    filename = ""
    #

    if len(sys.argv) >= 2:
        # AGGIUNTA RUBINETTI
        filename = sys.argv[1]
        input_data = ReadAttributes(filename)

        if len(sys.argv) >= 3:
            max_attrs = int(sys.argv[2])
        #
        del sys.argv[1]
    else :
        input_data = ReadAttributes()

    tab = Table(input_data, max_attrs)


    l = "Head Concept: "+ tab.h_conc+"\tModifier Concept: "+tab.m_conc

    res_scenario = -1

    rec = recommended(tab)
    if rec != [] :
        l += '\nRecommended scenario(s) N°:'
        for x in rec :
           l += ' '+str(x)+' '
           if res_scenario == -1 :
               res_scenario = x
           
        #res_scenario è l'indice dello scenario che viene scritto come risultato nel file del prototipo
        #Scrittura del risultato di CoCoS nel file del prototipo elaborato
        f = open(filename, "a")
        s = str(tab.sorted_table[x])
        s = s.replace('[', "")
        s = s.replace(']', "")
        f.write("\nResult : " + s)
        f.close()
    else:
        l += '\nNO recommended scenarios!'

    print("\n\n Result: ", l)
else:
    print ("Unknown error at the very beginning...")
