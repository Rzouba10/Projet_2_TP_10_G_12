from requirement.fltk import *
from utils.constantes import *

def init_niveaux():
    
    rectangle(MUR_DROIT[0][0],MUR_DROIT[0][1],MUR_DROIT[1][0],MUR_DROIT[1][1],remplissage="red")
    rectangle(MUR_GAUCHE[0][0],MUR_GAUCHE[0][1],MUR_GAUCHE[1][0],MUR_GAUCHE[1][1],remplissage="red")
    rectangle(SOL[0][0],SOL[0][1],SOL[1][0],SOL[1][1],remplissage="green")
    