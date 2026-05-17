from utils.constantes import *
from math import *

class Pile:
    """
    Structure de données LIFO (Last In, First Out).
    """
    
    def __init__(self):
        """Initialise une pile vide."""
        
        self.elements = []
    
    def empiler(self, element):
        """Ajoute un élément au sommet de la pile."""
        
        self.elements.append(element)
    
    def depiler(self):
        """Retire et retourne l'élément au sommet, ou None si vide."""
        
        if self.est_vide():
            return None
        return self.elements.pop()
    
    def sommet(self):
        """Retourne l'élément au sommet sans le retirer, ou None si vide."""
        
        if self.est_vide():
            return None
        return self.elements[-1]
    
    def est_vide(self):
        """Retourne True si la pile ne contient aucun élément."""
        
        return len(self.elements) == 0
    
    def taille(self):
        """Retourne le nombre d'éléments dans la pile."""
        
        return len(self.elements)


class File:
    """
    Structure de données FIFO (First In, First Out).
    """
    
    def __init__(self):
        """Initialise une file vide."""
        
        self.elements = []
    
    def enfiler(self, element):
        """Ajoute un élément en fin de file."""
        
        self.elements.append(element)
    
    def defiler(self):
        """Retire et retourne le premier élément de la file, ou None si vide."""
        
        if self.est_vide():
            return None
        return self.elements.pop(0)
    
    def premier(self):
        """Retourne le premier élément sans le retirer, ou None si vide."""
        
        if self.est_vide():
            return None
        return self.elements[0]
    
    def est_vide(self):
        """Retourne True si la file ne contient aucun élément."""
        
        return len(self.elements) == 0
    
    def taille(self):
        """Retourne le nombre d'éléments dans la file."""
        
        return len(self.elements)
    

def generer_vitesses(increment=10):
    """
    Génère toutes les paires de vitesses (vx, vy) dans le disque de rayon VMAX avec l'incrément donné.
    """
    
    liste_vitesses = []
    
    for vx in range(-VMAX, VMAX + 1, increment):
        for vy in range(-VMAX, VMAX + 1, increment):
            
            if vx == 0 and vy == 0:
                continue
            
            if sqrt(vx**2 + vy**2) <= VMAX:
                liste_vitesses.append((vx, vy))
    
    return liste_vitesses

def position_approchee(x, y, finesse=10):
    """
    Retourne une version discrétisée de la position selon la finesse donnée.
    """
    
    return (x // finesse, y // finesse)