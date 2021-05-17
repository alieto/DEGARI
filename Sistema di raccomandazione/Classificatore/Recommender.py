#Classificatore che restituisce tutte le istanze ordinate in base ad una graduatoria calcolata
#che rientrano nel nuovo genere fornito in input

import sys
import os
import json
import Recommender_config as cfg

from DataFromInput import *

#Controlla se una parola(w) e' contenuta in una stringa(s)
def contains_word(s, w):
    return ((' ' + str(w) + ' ') in (' ' + str(s) + ' ')) or ((' ' + str(w) + ',') in (' ' + str(s) + ' '))

def contains_value(lista, w):
    for p in lista:
        if str(p[0]) == w:
            return True
    return False

#Calcola la graduatoria e riclassifica tutte le istanze offrendo la raccomandazione
def elaboraGraduatoria(prop_list, not_prop_list = []) :
    print("\nRecommended artworks:\n\n")
        
    graduatoria = {}
    lista_istanze = []
    chars_not_allowed_in_filename = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']

    sum = 0

    #Apertura json contenente le descrizioni delle opere
    with open(cfg.jsonDescrFile) as json_file:
        data = json.load(json_file)
        
        #Calcolo graduatoria
        for instance in data:
            sum = sum + 1
            for char in chars_not_allowed_in_filename:
                instance[cfg.instanceID] = str(instance[cfg.instanceID]).replace(char, "")
            instance[cfg.instanceID]=instance[cfg.instanceID].replace("'","_")
            if instance[cfg.instanceID] not in graduatoria :
                graduatoria[instance[cfg.instanceID]] = 0
                for prop in prop_list:
                    for t in cfg.instanceTitle:
                        if contains_word(instance[t], str(prop[0])) :
                            graduatoria[instance[cfg.instanceID]] = 0.1
                artworkFile = open(cfg.protPath + instance[cfg.instanceID] + ".txt", "r")
                for p in artworkFile:
                    word = p.split(':')
                    if contains_value(prop_list,word[0].strip()) :
                        score = round(float(word[1].strip()),2)
                        #Inserimento istanza in graduatoria 
                        graduatoria[instance[cfg.instanceID]] += score 
                artworkFile.close()               

        #Scorrimento istanze
        for instance in data:
            for char in chars_not_allowed_in_filename:
                instance[cfg.instanceID] = instance[cfg.instanceID].replace(char, "")

            matches = []
            #Scorrimento proprietà risultato
            for prop in prop_list:
                inDescr = False
                i = 0
                while ((not inDescr) and i < len(cfg.instanceDescr)):
                    inDescr = contains_word(instance[cfg.instanceDescr[i]], str(prop[0]))
                    i = i+1

                inTitle = False
                i = 0
                while ((not inTitle) and i < len(cfg.instanceTitle)):
                    inTitle = contains_word(instance[cfg.instanceTitle[i]], str(prop))
                    i = i+1

                if inDescr or inTitle :
                    matches.append(str(prop[0]))
                    #Se viene trovato un match, viene aggiunto a una lista
            
            #Se nell'istanza compare una proprietà negata, l'istanza viene scartata
            for prop in not_prop_list:
                inDescr = False
                i = 0
                while ((not inDescr) and i < len(cfg.instanceDescr)):
                    inDescr = contains_word(instance[cfg.instanceDescr[i]], str(prop))
                    i = i+1

                if inDescr or contains_word(instance[cfg.instanceTitle[0]], str(prop)) :
                    matches.clear()
                    break
            
            #Un'istanza è considerata se contiene almeno il 30% delle proprietà della lista
            if int(len(matches)) >= int(len(prop_list)*30/100):
                lista_istanze.append([instance[cfg.instanceID] + " - " + instance[cfg.instanceTitle[0]],
                                        "\n\t\\-> matches: " + str(matches)])
            elif int(len(matches)) == 0:
                graduatoria[instance[cfg.instanceID]] = 0
    
    #Graduatoria risultato
    i = 0
    #Scorrimento graduatoria ordinata per il punteggio degli artwork in modo decrescente
    for artwork, score in sorted(graduatoria.items(), key=lambda kv:kv[1], reverse=True):
        if score == 0:
            break
        print(artwork + "-" + str(score))

        for istanza in lista_istanze:
            if contains_word(istanza[0], artwork):
                i+=1
                print("\t" + istanza[0] + istanza[1] + "\n")
                f = open("recommendations.tsv", "a")
                f.write(istanza[0].replace("\t", " ") + "\t" + category + "\n")
                f.close()
    if i == 0 :
        print("No recommendable contents for this category.")
    else:
        perc = (100*i)/sum
        print("Classified "+str(i)+" of "+str(sum)+" contents ("+str(perc)+"%)")
        f = open("resume.tsv", "a")
        f.write(category.replace("\t", " ") + "\t" + str(i) + "\n")
        f.close()

#Main
if __name__ == '__main__' :
    if len(sys.argv) == 2 :
        #Lettura nome prototipo da classificare
        prototipo = sys.argv[1]
        category = prototipo.split("/")[-1]

        #Lettura file prototipo - viene riutilizzato lo script "DataFromInput" di CoCoS
        f = ReadAttributes(prototipo)
        
        print("\nRecommendation for category: " + category + "\n\nCategory prototype: \n")
        
        #Trasformazione risultato stringa in lista
        r = [str(s) for s in f.result.split(',')]     

        #Lista delle proprietà risultato forti + tipiche
        prop_list = []
        not_prop_list = []

        #Inserimento proprietà forti nella lista
        for p in f.attrs :
            if str(p).find('-') == -1:
                prop_list.append(p)
            else :
                not_prop_list.append(p[0].replace("-", "").strip())

        #Inserimento proprietà tipiche estratte dal risultato di COCOS
        i = 0
        for p in f.tipical_attrs:
            if r[i].strip() == "'1'":
                prop_list.append(p)
            i+=1
        pprint(prop_list)
        pprint(not_prop_list)

        #Calcolo graduatoria nuova categoria
        elaboraGraduatoria(prop_list, not_prop_list)

    elif len(sys.argv) > 2 : #Inserimento parole da linea di comando (stile ricerca rai play)
        prop_list = []
        for i in range(1,len(sys.argv)):
            prop_list.append(tuple([sys.argv[i],'1']))
        pprint(prop_list)

        #Calcolo graduatoria nuova categoria
        elaboraGraduatoria(prop_list)
    else :
        print("Specify a prototype for the classification!")
