from CreateOntology import *

#Metodo per controllare che le proprietà del modifier prese in considerazione 
# in uno scenario non creino conflitto con le proprietà dell'head non prese 
# in considerazione in quello stesso scenario
def conflict(line, tipical_attrs, attrs) :
    #Per ogni attributo nello scenario
    for i in range(len(tipical_attrs)) :
        #Se appartiene alla head inverte il suo valore
        if tipical_attrs[i][2]:
            
            if line[i] == '0' : line[i] = '1'
            else : line[i] = '0'
    
    onto = ManageOntology(tipical_attrs, attrs, line)
    return not onto.is_consistent()

#Metodo che restituisce una lista con i numeri degli scenari (linee) 
# all'interno della tabella che sono più rappresentativi, e quindi consigliati
# Come prima cosa crea dei blocchi di scenari con stessa probabilità, 
#  partendo da probabilità più alta
# Poi partendo dal primo blocco ad analizzare controlla che non 
#   contenga tutti gli attributi della head (troppo banale e poco rappresentativo)
#   e che il metodo conflict restituisca false, nel qual caso vengono aggiunti 
#   gli scenari rimasti alla lista risualtante, nel caso non fossero rimasti scenari, 
#   si ripete finchè non se ne trova uno.
def recommended(table) :
    
    res = []
    l = len(table.sorted_table)-1
    line_l = len(table.tipical_attrs)

    while res == [] and l > 0 :
        
        #creo blocco
        block = []
        Max = table.sorted_table[l][line_l]

        while l > 0 and table.sorted_table[l][line_l] == Max :
            block.append(tuple([table.sorted_table[l],l]))
            l -= 1
        print(block)

        for scen in block :
            #controllo se contiene tutti gli attributi head            
            contains_all_h_attrs = True
            for elem in range(len(scen[0])-1) :
                if scen[0][elem] == '0' and table.tipical_attrs[elem][2] == True :
                    contains_all_h_attrs = False
            #se non contiene tutti gli attributi head, controlla che non crei conflitti e nel caso aggiunge al result
            if not contains_all_h_attrs:
                #if consistent_scenario(scen[0][:-1], table.tipical_attrs, table.attrs):
                c = conflict(scen[0][:-1], table.tipical_attrs, table.attrs)
                if not c :
                    res.append(scen[1])
    return res  

