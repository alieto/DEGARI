import sys

from DataFromInput import *
from MkTable import *
from Recommended import *

def creaScenario(path) :

    
    input_data = ReadAttributes(path)

    tab = Table(input_data)

    l = "Head Concept: "+ tab.h_conc+"\tModifier Concept: "+tab.m_conc
        
    rec = retScenario(tab)
    if rec != 0 :
        l += '' + rec + ' '
    else :  
    	l += '\nNO recommended scenarios!'

    return l
