from utils.constantes import *
from math import *

class Pile:
    
    def __init__(self):
        self.elements = []
    
    def empiler(self, element):
        self.elements.append(element)
    
    def depiler(self):
        if self.est_vide():
            return None
        return self.elements.pop()
    
    def sommet(self):
        if self.est_vide():
            return None
        return self.elements[-1]
    
    def est_vide(self):
        return len(self.elements) == 0
    
    def taille(self):
        return len(self.elements)


class File:
    
    def __init__(self):
        self.elements = []
    
    def enfiler(self, element):
        self.elements.append(element)
    
    def defiler(self):
        if self.est_vide():
            return None
        return self.elements.pop(0)
    
    def premier(self):
        if self.est_vide():
            return None
        return self.elements[0]
    
    def est_vide(self):
        return len(self.elements) == 0
    
    def taille(self):
        return len(self.elements)
    

def generer_vitesses(increment=10):
    liste_vitesses = []
    
    for vx in range(-VMAX, VMAX + 1, increment):
        for vy in range(-VMAX, VMAX + 1, increment):
            
            if vx == 0 and vy == 0:
                continue
            
            if sqrt(vx**2 + vy**2) <= VMAX:
                liste_vitesses.append((vx, vy))
    
    return liste_vitesses

def position_approchee(x, y, finesse=10):
    
    return (x // finesse, y // finesse)