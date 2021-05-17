from owlready2 import *
import os,types
from random import randint

#Classe per la gestione delle ontologie
# Inizialmente salva i dati e crea una nuova ontologia
# in seguito crea due nuove classi nell'ontologia: head e modifier
# aggiunge a head e modifier tutti gli attributi, distinguendo tra proprietà forti e tipiche
# rende equivalenti head e modifier e in seguito crea un individuo di queste classi.
# NB!! Questa classe mette anche a disposizione un metodo per controllare la consistenza dell'ontologia

class ManageOntology :

    def __init__ (self, tipical_attrs, attrs, line) :

        self.attrs = attrs
        self.tipical_attrs = tipical_attrs
        self.line = line
   
        onto_path.append(os.path.dirname(os.path.abspath(__file__)))
        self.my_world = World()
        self.onto = self.my_world.get_ontology("http://www.example.org/onto.owl#"+str(randint(0, 99)))
                
        self.head = self.create_class('head')
        self.modifier = self.create_class('modifier')
 
        self.add_attrs()
        self.add_tipical_attrs()
             
        self.combined = self.create_class('combined')
        self.combined.equivalent_to.append(self.head & self.modifier)

        self.add_tipical_combined_attrs()

        self.ind = self.combined("ind")
        #close_world(self.my_world)


    #Metodo per aggiungere le proprietà forti all'ontologia
    # Per ogni attributo da aggiungere :
    #   Crea un attributo temporaneo e, se ha un '-' davanti, lo nega
    #   Dopo di che a seconda che sia dell'head o del modifier 
    #    lo aggiunge al concetto corretto 
    def add_attrs(self) :
        
        for x,y in self.attrs :

            tmp_attr = self.create_class(
                        (x.replace(' ', '_') if len(x)>0 and x[0] != '-' 
                        else x[1:].replace(' ', '_')) )

            if len(x)>0 and x[0] == '-' :
                tmp_attr = Not(tmp_attr)            

            if y :
                self.head.is_a.append(tmp_attr)
            if not y :
                self.modifier.is_a.append(tmp_attr) 


    #Metodo per aggiungere le proprietà tipiche all'ontologia
    # Per ogni attributo da aggiungere :
    #   Controlla che sulla linea dello scenario, l'attributo sia davvero considerato (== '1')
    #   Crea l'attributo e lo nega in caso il primo carattere sia '-'
    #   Dopo aggiunge l'attributo (creando tutte le relazioni implicite nella tipicalità)
    #    alla head o al modifier, come specificato dall'input
    def add_tipical_attrs(self) :

        for i in range(len(self.tipical_attrs)) :

            #if self.line[i] == '1' :
            
            x,y,z = self.tipical_attrs[i]
            tmp_attr = self.create_class(
                        (x.replace(' ', '_') if x[0] != '-'
                        else x[1:].replace(' ', '_')) )
            
            if x[0] == '-' :
                tmp_attr = Not(tmp_attr)

            
            if z :
                head1 = self.create_class('head1')
                heads = self.create_class('heads')
                not_head1 = self.create_class('not_head1')

                heads.equivalent_to.append(self.head & head1)
                not_head1.equivalent_to.append(Not(head1))
                head_r = self.create_property('head_R')
                
                heads.is_a.append(tmp_attr)
                head1.is_a.append(head_r.only(Not(self.head) & head1))
                not_head1.is_a.append(head_r.some(self.head & head1))

            if not z :
                modifier1 = self.create_class('modifier1')
                modifiers = self.create_class('modifiers')
                not_modifier1 = self.create_class('not_modifier1')

                modifiers.equivalent_to.append(self.modifier & modifier1)
                not_modifier1.equivalent_to.append(Not(modifier1))
                modifier_r = self.create_property('modifier_R')
                
                modifiers.is_a.append(tmp_attr)
                modifier1.is_a.append(modifier_r.only(
                                    Not(self.modifier) & modifier1) )
                not_modifier1.is_a.append(modifier_r.some(
                                    self.modifier & modifier1) )

    




    def add_tipical_combined_attrs(self) :

            for i in range(len(self.tipical_attrs)) :

                if self.line[i] == '1' :
                    
                    x,y,z = self.tipical_attrs[i]
                    tmp_attr = self.create_class(
                                (x.replace(' ', '_') if x[0] != '-'
                                else x[1:].replace(' ', '_')) )
                    
                    if x[0] == '-' :
                        tmp_attr = Not(tmp_attr)

                    
                    combined1 = self.create_class('combined1')
                    combineds = self.create_class('combineds')
                    not_combined1 = self.create_class('not_combined1')

                    combineds.equivalent_to.append(self.combined & combined1)
                    not_combined1.equivalent_to.append(Not(combined1))
                    combined_r = self.create_property('combined_R')
                    
                    combineds.is_a.append(tmp_attr)
                    combined1.is_a.append(combined_r.only(Not(self.combined) & combined1))
                    not_combined1.is_a.append(combined_r.some(self.combined & combined1))

            


    #Metodo che si appoggia ad un metodo ausialiario che controlla la consistenza
    # dell'ontologia affidandosi al reasoner Hermit
    def is_consistent(self) :        
        return self.consistency()
    
    def consistency(self) :
        try :
            with self.onto:
                sync_reasoner(self.my_world)
        except subprocess.CalledProcessError as inst :
            return False
        except :
            return False

        return True    
    

    #Metodo per creare classi nell'ontologia in modo dinamico
    def create_class(self, name, parent = Thing) :
        
        with self.onto :
            new_class = types.new_class(name, (parent,))
        return new_class

    #Metodo per creare proprietà nell'ontologia in modo dinamico
    def create_property(self, name) :

        with self.onto :
            new_prop = types.new_class(name, (ObjectProperty,))
        return new_prop







if __name__ == "__main__" :
    
    ex_t = [("attr2",0.5,False), ("attr1",0.5,False), ('-attr2', 0.7, True)]

    ex_not_t = [("-attr1",True)]

    x = ManageOntology(ex_t, ex_not_t, ['1','0','1'])
    print(x.is_consistent())

    j = ManageOntology(ex_t, ex_not_t, ['0','0','0'])
    print(j.is_consistent())


    


