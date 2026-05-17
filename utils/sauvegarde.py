from utils.constantes import *
import os

def sauvegarder_niveau(etat_editeur, theme_choisi, nom_fichier=None):
    if nom_fichier:
        chemin_fichier = f"niveaux/creation/{nom_fichier}"
    else:
        fichiers_txt = [f for f in os.listdir("niveaux/creation") if f.endswith(".txt")]
        numero = len(fichiers_txt) + 1
        chemin_fichier = f"niveaux/creation/nv_{numero}.txt"

    with open(chemin_fichier, "w") as fichier:

        if etat_editeur["depart"] is not None:
            dx, dy = etat_editeur["depart"]
            fichier.write(f"{dx},{dy}\n")
        else:
            fichier.write("0,0\n")

        if etat_editeur["objectif"] is not None:
            obj = etat_editeur["objectif"]
            x1, y1 = obj["coin1"]
            x2, y2 = obj["coin2"]
            fichier.write(f"{x1},{y1},{x2},{y2}\n")
        else:
            fichier.write("0,0,0,0\n")
        
        fichier.write(f"{theme_choisi if theme_choisi else 'none'}\n")

        for bloc in etat_editeur["blocs"]:
            if "x" in bloc:
                cx, cy = bloc["x"], bloc["y"]
                tl = bloc.get("taille_l", TAILLE_BLOC_L)
                th = bloc.get("taille_h", TAILLE_BLOC_H)
                x1 = cx - tl // 2
                y1 = cy - th // 2
                x2 = cx + tl // 2
                y2 = cy + th // 2
                theme = bloc.get("theme", "custom")
            else:
                x1, y1 = bloc["coin1"]
                x2, y2 = bloc["coin2"]
                theme = "custom"
            type_bloc = bloc["type"]
            fichier.write(f"{x1},{y1},{x2},{y2},{type_bloc},{theme}\n")

    return chemin_fichier