from utils.constantes import *
import os

def sauvegarder_niveau(etat_editeur):

    fichiers_existants = os.listdir("niveaux/creation")
    
    fichiers_txt = []
    for nom_fichier in fichiers_existants:
        if nom_fichier.endswith(".txt"):
            fichiers_txt.append(nom_fichier)
    
    numero_nouveau_fichier = len(fichiers_txt) + 1
    
    chemin_fichier = f"niveaux/creation/nv_{numero_nouveau_fichier}.txt"
    
    fichier = open(chemin_fichier, "w")
    

    if etat_editeur["depart"] is not None:
        depart_x, depart_y = etat_editeur["depart"]
        fichier.write(f"{depart_x},{depart_y}\n")
    
    if etat_editeur["objectif"] is not None:
        objectif = etat_editeur["objectif"]
        
        obj_x1, obj_y1 = objectif["coin1"]
        obj_x2, obj_y2 = objectif["coin2"]
        
        fichier.write(f"{obj_x1},{obj_y1},{obj_x2},{obj_y2}\n")
    
    for bloc in etat_editeur["blocs"]:
        
        if "x" in bloc:
            centre_x = bloc["x"]
            centre_y = bloc["y"]
            
            bloc_x1 = centre_x - TAILLE_BLOC_L // 2
            bloc_y1 = centre_y - TAILLE_BLOC_H // 2
            bloc_x2 = centre_x + TAILLE_BLOC_L // 2 
            bloc_y2 = centre_y + TAILLE_BLOC_H // 2 
            
        else:
            bloc_x1, bloc_y1 = bloc["coin1"]
            bloc_x2, bloc_y2 = bloc["coin2"]
        
        type_bloc = bloc["type"]
        
        fichier.write(f"{bloc_x1},{bloc_y1},{bloc_x2},{bloc_y2},{type_bloc}\n")
    
    fichier.close()
    
    return chemin_fichier