from requirement.fltk import *
from utils.constantes import *
from time import *
import os

def charger_page_niveau(theme, niveau, skin, mon_jeu):
    nom_fichier = "niveaux/" + str(theme) + "/" + "nv" + str(niveau) + ".txt"
    mon_jeu.ranger_donnees(nom_fichier)
    charger_niveau(skin, mon_jeu, theme)

def charger_menue(skin,premier_lancement=False):
    
    if premier_lancement:
        fond = image(400, 400, "ressource/image/fond/menue.png")
        logo = image(400, 400, "ressource/image/fond/titre.png")
        
        mise_a_jour()
        
        sleep(2)
        
        efface(logo)
        efface(fond)
        
        fond_2 = image(400, 400, "ressource/image/fond/menue_2.png")
        skin_f = image(145, 680, "ressource/image/perso/" + str(skin)+".png")
        
        mise_a_jour()
    
    else:
        fond_2 = image(400, 400, "ressource/image/fond/menue_2.png")
        skin_f = image(145, 700, "ressource/image/perso/" + str(skin)+".png")
        
        mise_a_jour()

def page_niveaux(page=0):
    liste_fichiers = []
    for fichier in os.listdir("niveaux/creation"):
        if fichier.endswith(".txt"):
            liste_fichiers.append(fichier)
    liste_fichiers.sort()

    nb_pages = len(liste_fichiers) // 5 + 1
    if len(liste_fichiers) % 5 != 0:
        nb_pages += 1
    if nb_pages == 0:
        nb_pages = 1

    if page < 0:
        page = 0
    if page > nb_pages - 1:
        page = nb_pages - 1

    indice_debut = page * 5
    indice_fin = indice_debut + 5
    tranche = liste_fichiers[indice_debut:indice_fin]

    efface_tout()
    image(400, 400, "ressource/image/fond/menue.png")
    image(400, 400, "ressource/image/fond/creation.png")
    image(400, 770, "ressource/image/fond/bouton_retour.png")

    position_y = 240
    for index in range(5):
        if index < len(tranche):
            nom_niveau = tranche[index].replace(".txt", "")
            texte(150, position_y, nom_niveau, couleur="black", taille=20, ancrage="w")
            image(535, position_y, "ressource/image/bouton/modifier.png")
            image(610, position_y, "ressource/image/bouton/suprimer.png")
        else:
            image(610, position_y, "ressource/image/bouton/ajouter.png")
        position_y += 79

    if page > 0:
        image(300, 720, "ressource/image/bouton/fleche_g.png")
    if page < nb_pages - 1:
        image(500, 720, "ressource/image/bouton/fleche_d.png")

    mise_a_jour()
    
    return {"page": page, "nb_pages": nb_pages, "tranche": tranche}

def page_niveaux_creation(page=0):
    liste_fichiers = []
    for fichier in os.listdir("niveaux/creation"):
        if fichier.endswith(".txt"):
            liste_fichiers.append(fichier)
    liste_fichiers.sort()

    nb_pages = max(1, -(-len(liste_fichiers) // 5))  # division arrondie au supérieur

    page = max(0, min(page, nb_pages - 1))

    indice_debut = page * 5
    tranche = liste_fichiers[indice_debut:indice_debut + 5]

    efface_tout()
    image(400, 400, "ressource/image/fond/menue.png")
    image(400, 400, "ressource/image/fond/creation.png")   # même fond que l'éditeur
    image(400, 770, "ressource/image/fond/bouton_retour.png")

    position_y = 240
    for index in range(5):
        if index < len(tranche):
            nom_niveau = tranche[index].replace(".txt", "")
            texte(150, position_y, nom_niveau, couleur="black", taille=20, ancrage="w")
            image(535, position_y, "ressource/image/bouton/jouer.png")  # ton image bouton jouer
        position_y += 79

    if page > 0:
        image(300, 720, "ressource/image/bouton/fleche_g.png")
    if page < nb_pages - 1:
        image(500, 720, "ressource/image/bouton/fleche_d.png")

    mise_a_jour()

    return {"page": page, "nb_pages": nb_pages, "tranche": tranche}

def page_choix_theme_sauvegarde():
    image(500, 400, "ressource/image/fond/editeur_theme.png")
    mise_a_jour()

def afichage_editeur():
    
    efface_tout()
    redimensionne_fenetre(1000,800 )
    
    rectangle(0,0,800,800,remplissage="grey")
    image(500,400,"ressource/image/fond/editeur.png")
    image(900, 730, "ressource/image/fond/bouton_retour.png")
    
    rectangle(MUR_GAUCHE[0][0], MUR_GAUCHE[0][1], 
          MUR_GAUCHE[1][0], MUR_GAUCHE[1][1], 
          remplissage="green")
    rectangle(MUR_DROIT[0][0], MUR_DROIT[0][1], 
          MUR_DROIT[1][0], MUR_DROIT[1][1], 
          remplissage="green")
    
    rectangle(SOL[0][0], SOL[0][1], 
          SOL[1][0], SOL[1][1], 
          remplissage="green")
    
    pass

def charger_editeur_depuis_fichier(chemin):
    editeur = {
        "blocs": [],
        "objectif": None,
        "depart": None,
        "mode": "AJOUTER",
        "type_bloc": "normal",
        "clics": [],
        "theme": None,
    }

    f = open(chemin, "r", encoding="utf-8")
    lignes = []
    for ligne in f:
        lignes.append(ligne.rstrip())
    f.close()

    dep = lignes[0].split(",")
    editeur["depart"] = (int(dep[0]), int(dep[1]))

    obj = lignes[1].split(",")
    editeur["objectif"] = {
        "coin1": (int(obj[0]), int(obj[1])),
        "coin2": (int(obj[2]), int(obj[3])),
    }

    editeur["theme"] = lignes[2]
    if editeur["theme"] in ("none", "None", ""):
        editeur["theme"] = None

    theme = editeur["theme"]
    for i in range(3, len(lignes)):
        if lignes[i] == "":
            continue
        parts = lignes[i].split(",")
        x1, y1, x2, y2 = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
        type_bloc = parts[4]
        theme_bloc = parts[5]

        if theme_bloc not in ("custom", "none", ""):
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            tl = x2 - x1
            th = y2 - y1
            suffixe = "_v" if th > tl else ""

            if type_bloc in NOMS_BLOCS_SPECIAUX:
                nom_fichier_img = NOMS_BLOCS_SPECIAUX[type_bloc]
                if suffixe:
                    nom_base, ext = nom_fichier_img.rsplit(".", 1)
                    nom_fichier_img = f"{nom_base}{suffixe}.{ext}"
                chemin_img = f"ressource/image/block/special/{theme_bloc}/{nom_fichier_img}"
            else:
                chemin_img = f"ressource/image/block/flotant/{theme_bloc}{suffixe}.png"

            editeur["blocs"].append({
                "x": cx, "y": cy,
                "type": type_bloc,
                "chemin": chemin_img,
                "theme": theme_bloc,
                "taille_l": tl,
                "taille_h": th,
            })
        else:
            editeur["blocs"].append({
                "coin1": (x1, y1),
                "coin2": (x2, y2),
                "type": type_bloc,
            })
        
    return editeur

def charger_niveau(skin, jeu, theme, mise_a_jour_auto=True, dessiner_perso=True):
    if STATUE_JEU == False:
        efface_tout()

        if theme and theme != "none":
            image(400, 400, f"ressource/image/fond/theme/{theme}.png")
            image(400, 400, f"ressource/image/block/paroit/{theme}.png")
        else:
            rectangle(0, 0, 800, 800, remplissage="grey")
            rectangle(MUR_GAUCHE[0][0], MUR_GAUCHE[0][1], MUR_GAUCHE[1][0], MUR_GAUCHE[1][1], remplissage="green")
            rectangle(MUR_DROIT[0][0],  MUR_DROIT[0][1],  MUR_DROIT[1][0],  MUR_DROIT[1][1],  remplissage="green")
            rectangle(SOL[0][0],        SOL[0][1],         SOL[1][0],        SOL[1][1],         remplissage="green")

        for bloc in jeu.lst_blocs:
            if bloc.type not in ("mur_gauche", "mur_droit", "sol"):
                x1, y1 = bloc.coin_sup_gauche
                x2, y2 = bloc.coin_inf_droit

                if bloc.style == "custom":
                    couleur = COULEURS_BLOCS.get(bloc.type, "green")
                    rectangle(x1, y1, x2, y2, remplissage=couleur, couleur="black")
                else:
                    theme_bloc = bloc.style

                    largeur_bloc = x2 - x1
                    hauteur_bloc = y2 - y1
                    suffixe = "_v" if hauteur_bloc > largeur_bloc else ""

                    if bloc.type in NOMS_BLOCS_SPECIAUX:
                        nom_fichier_img = NOMS_BLOCS_SPECIAUX[bloc.type]
                        if suffixe:
                            nom_base, ext = nom_fichier_img.rsplit(".", 1)
                            nom_fichier_img = f"{nom_base}{suffixe}.{ext}"
                        chemin = f"ressource/image/block/special/{theme_bloc}/{nom_fichier_img}"
                    else:
                        chemin = f"ressource/image/block/flotant/{theme_bloc}{suffixe}.png"
                    image(x1, y1, chemin, ancrage="nw")

                    image(x1, y1, chemin, ancrage="nw")

        if jeu.objectif is not None:
            x1, y1 = jeu.objectif[0]
            x2, y2 = jeu.objectif[1]
            centre_x = (x1 + x2) // 2
            if theme and theme != "none":
                centre_x = (x1 + x2) // 2
                image(centre_x, y2, f"ressource/image/block/objectif/{theme}.png", ancrage="s")
            else:
                rectangle(x1, y1, x2, y2, couleur="red", epaisseur=2)
                
        if dessiner_perso:
            perso = image(jeu.position_x, jeu.position_y, f"ressource/image/perso/{skin}.png")
        
        if mise_a_jour_auto:
            mise_a_jour()

def dessiner_vecteur(jeu, vect):

    ligne(jeu.position_x, jeu.position_y, vect[0], vect[1], couleur="red", epaisseur=2)  
    fleche(jeu.position_x, jeu.position_y, vect[0], vect[1], couleur="red", epaisseur=2)

def mouvement(jeu, skin, theme, trace):
    global STATUE_JEU
    STATUE_JEU = True
    
    index_debut_trace = len(trace)
    ancienne_x = jeu.position_x
    ancienne_y = jeu.position_y

    efface_tout()
    if theme and theme != "none":
            image(400, 400, f"ressource/image/fond/theme/{theme}.png")
            image(400, 400, f"ressource/image/block/paroit/{theme}.png")
    else:
        rectangle(0, 0, 800, 800, remplissage="grey")
        rectangle(MUR_GAUCHE[0][0], MUR_GAUCHE[0][1], MUR_GAUCHE[1][0], MUR_GAUCHE[1][1], remplissage="green")
        rectangle(MUR_DROIT[0][0],  MUR_DROIT[0][1],  MUR_DROIT[1][0],  MUR_DROIT[1][1],  remplissage="green")
        rectangle(SOL[0][0],        SOL[0][1],         SOL[1][0],        SOL[1][1],         remplissage="green")

    for bloc in jeu.lst_blocs:
       if bloc.type not in ("mur_gauche", "mur_droit", "sol"):
                x1, y1 = bloc.coin_sup_gauche
                x2, y2 = bloc.coin_inf_droit

                if bloc.style == "custom":
                    couleur = COULEURS_BLOCS.get(bloc.type, "green")
                    rectangle(x1, y1, x2, y2, remplissage=couleur, couleur="black")
                else:
                    theme_bloc = bloc.style

                    largeur_bloc = x2 - x1
                    hauteur_bloc = y2 - y1
                    suffixe = "_v" if hauteur_bloc > largeur_bloc else ""

                    if bloc.type in NOMS_BLOCS_SPECIAUX:
                        nom_fichier_img = NOMS_BLOCS_SPECIAUX[bloc.type]
                        if suffixe:
                            nom_base, ext = nom_fichier_img.rsplit(".", 1)
                            nom_fichier_img = f"{nom_base}{suffixe}.{ext}"
                        chemin = f"ressource/image/block/special/{theme_bloc}/{nom_fichier_img}"
                    else:
                        chemin = f"ressource/image/block/flotant/{theme_bloc}{suffixe}.png"
                    image(x1, y1, chemin, ancrage="nw")

    if jeu.objectif is not None:
        x1, y1 = jeu.objectif[0]
        x2, y2 = jeu.objectif[1]
        centre_x = (x1 + x2) // 2
        if theme and theme != "none":
            centre_x = (x1 + x2) // 2
            image(centre_x, y2, f"ressource/image/block/objectif/{theme}.png", ancrage="s")
        else:
            rectangle(x1, y1, x2, y2, couleur="red", epaisseur=2)

    id_perso = image(jeu.position_x, jeu.position_y, f"ressource/image/perso/{skin}.png")
    mise_a_jour()

    resultat_final = None
    
    while True:

        if jeu.is_winnable():
            efface(id_perso)
            image(jeu.position_x, jeu.position_y, f"ressource/image/perso/{skin}.png")
            mise_a_jour()
            resultat_final = "GAGNE"
            break
        
        if jeu.pas() == "Finish":
            break
        
        if len(trace) == index_debut_trace or \
           abs(jeu.position_x - trace[-1][0]) + abs(jeu.position_y - trace[-1][1]) > 10:
            trace.append((jeu.position_x, jeu.position_y))
            cercle(ancienne_x, ancienne_y, 5, remplissage="white", couleur="black")

        efface(id_perso)
        id_perso = image(jeu.position_x, jeu.position_y, f"ressource/image/perso/{skin}.png")
        ancienne_x = jeu.position_x
        ancienne_y = jeu.position_y

        mise_a_jour()

        if jeu.position_y > 800:
            break

        sleep(0.001)

    STATUE_JEU = False
    return resultat_final

def charger_menue_skin(skin):
    efface_tout()
    fond = image(400, 400, "ressource/image/fond/menue.png")
    retour = image(400, 750, "ressource/image/fond/bouton_retour.png")
    
    for i in range(3):
        for j in range(3):
            if LISTE_SKIN[i][j] == skin:
                image(200+(j*200),200+(i*200),"ressource/image/fond/Skin_t.png")
            elif LISTE_SKIN[i][j] != skin:
                image(200+(j*200),200+(i*200),"ressource/image/fond/Skin_f.png")
            image(200+(j*200),200+(i*200),"ressource/image/perso/" + str(LISTE_SKIN[i][j])+".png")

    mise_a_jour()           


def charger_pause_save(evenement):
    
    x = abscisse(evenement)
    y = ordonnee(evenement)
    
    if 250 <= x <= 540 and 270 <= y <= 340:
         pass
    
    if 250 <= x <= 540 and 360 <= y <= 430:
         pass
    
    if 250 <= x <= 540 and 460 <= y <= 530:
         pass

def retour_arriere(jeu, skin, theme, historique_departs):
    if not historique_departs:
        return

    x, y = historique_departs.pop()

    jeu.position_x = x
    jeu.position_y = y

    charger_niveau(skin, jeu, theme)

def trouver_bloc(x, y, etat_editeur):
    for i, b in enumerate(etat_editeur["blocs"]):
        if "x" in b:
            tl = b.get("taille_l", TAILLE_BLOC_L)
            th = b.get("taille_h", TAILLE_BLOC_H)
            x1 = b["x"] - tl // 2
            y1 = b["y"] - th // 2
            x2 = b["x"] + tl // 2
            y2 = b["y"] + th // 2
        else:
            x1, y1 = b["coin1"]
            x2, y2 = b["coin2"]
        if x1 <= x <= x2 and y1 <= y <= y2:
            return i
    return None


def rafraichir_editeur(etat_editeur):
    efface_tout()
    image(500, 400, "ressource/image/fond/editeur.png")
    image(900, 730, "ressource/image/fond/bouton_retour.png")

    rectangle(MUR_GAUCHE[0][0], MUR_GAUCHE[0][1],
              MUR_GAUCHE[1][0], MUR_GAUCHE[1][1], remplissage="green")
    rectangle(MUR_DROIT[0][0],  MUR_DROIT[0][1],
              MUR_DROIT[1][0],  MUR_DROIT[1][1],  remplissage="green")
    rectangle(SOL[0][0], SOL[0][1],
              SOL[1][0], SOL[1][1], remplissage="green")

    for b in etat_editeur["blocs"]:
        if "x" in b:
            image(b["x"], b["y"], b["chemin"])
        else:
            couleur = COULEURS_BLOCS.get(b["type"], "green")
            rectangle(b["coin1"][0], b["coin1"][1],
                      b["coin2"][0], b["coin2"][1],
                      remplissage=couleur, couleur="black")

    if etat_editeur["objectif"]:
        obj = etat_editeur["objectif"]
        rectangle(obj["coin1"][0], obj["coin1"][1],
                  obj["coin2"][0], obj["coin2"][1],
                  couleur="red", epaisseur=2)

    if etat_editeur["depart"]:
        dx, dy = etat_editeur["depart"]
        image(dx, dy, "ressource/image/perso/standar_j.png")

    dessiner_panneau_editeur(etat_editeur)
    mise_a_jour()


def dessiner_panneau_editeur(etat_editeur):
    POSITIONS_BOUTONS = {
        "AJOUTER":    (837, 20,  970, 49),
        "MODIFIER":   (838, 57,  971, 84),
        "SUPPRIMER":  (838, 95,  972, 120),
        "normal":     (820, 168, 897, 181),
        "glace":      (906, 166, 982, 184),
        "derape":     (820, 201, 895, 218),
        "colant":     (906, 201, 985, 218),
        "elastique":  (820, 235, 896, 250),
        "trampoline": (906, 237, 982, 252),
        "verticale":    (831, 285, 891, 305),
        "horizontale":  (912, 285, 985, 305),
        "OBJECTIF":   (835, 333, 968, 356),
        "DEPART":     (860, 380, 942, 459),
        "desert":     (833, 522, 966, 547),
        "foret":      (833, 559, 964, 584),
        "espace":     (833, 594, 966, 618),
        "pirate":     (834, 631, 965, 657),
        "theme_none": (834, 670, 966, 693),
    }
    mode = etat_editeur["mode"]
    type_b = etat_editeur["type_bloc"]
    theme = etat_editeur.get("theme", None)
    orientation = etat_editeur.get("orientation", "horizontale")

    if mode in POSITIONS_BOUTONS:
        bx1, by1, bx2, by2 = POSITIONS_BOUTONS[mode]
        rectangle(bx1, by1, bx2, by2, couleur="red", epaisseur=2)

    if orientation in POSITIONS_BOUTONS:
        bx1, by1, bx2, by2 = POSITIONS_BOUTONS[orientation]
        rectangle(bx1, by1, bx2, by2, couleur="red", epaisseur=2)
    
    if type_b in POSITIONS_BOUTONS:
        bx1, by1, bx2, by2 = POSITIONS_BOUTONS[type_b]
        rectangle(bx1, by1, bx2, by2, couleur="red", epaisseur=2)

    if theme in POSITIONS_BOUTONS:
        bx1, by1, bx2, by2 = POSITIONS_BOUTONS[theme]
        rectangle(bx1, by1, bx2, by2, couleur="red", epaisseur=2)
    elif theme is None:
        bx1, by1, bx2, by2 = POSITIONS_BOUTONS["theme_none"]
        rectangle(bx1, by1, bx2, by2, couleur="red", epaisseur=2)
    
def gestion_clic_editeur(x, y, etat_editeur):
    
    mode = etat_editeur["mode"]
    theme = etat_editeur.get("theme", None)

    if theme and mode == "AJOUTER":
        type_block = etat_editeur["type_bloc"]
        orientation = etat_editeur.get("orientation", "horizontale")

        if orientation == "verticale":
            taille_l = TAILLE_BLOC_V_L
            taille_h = TAILLE_BLOC_V_H
            suffixe = "_v"
        elif type_block in NOMS_BLOCS_SPECIAUX:
            taille_l = TAILLE_BLOC_L
            taille_h = TAILLE_BLOC_H
            suffixe = ""
        else:
            taille_l = LARGEUR_BLOC.get(theme, TAILLE_BLOC_L)
            taille_h = HAUTEUR_BLOC.get(theme, TAILLE_BLOC_H)
            suffixe = ""

        if type_block in NOMS_BLOCS_SPECIAUX:
            nom_fichier_img = NOMS_BLOCS_SPECIAUX[type_block]
            # ajoute _v avant l'extension si vertical
            if suffixe:
                nom_base, ext = nom_fichier_img.rsplit(".", 1)
                nom_fichier_img = f"{nom_base}{suffixe}.{ext}"
            chemin = f"ressource/image/block/special/{theme}/{nom_fichier_img}"
        else:
            chemin = f"ressource/image/block/flotant/{theme}{suffixe}.png"

        etat_editeur["blocs"].append({
            "x": x, "y": y,
            "type": type_block,
            "chemin": chemin,
            "theme": theme,
            "taille_l": taille_l,
            "taille_h": taille_h,
        })
        rafraichir_editeur(etat_editeur)
        return etat_editeur

    if mode == "MODIFIER":
        bloc_indice = trouver_bloc(x, y, etat_editeur)
        if bloc_indice is not None:
            if not etat_editeur["clics"]:
                etat_editeur["clics"] = [("selection", bloc_indice)]
                rafraichir_editeur(etat_editeur)
                b = etat_editeur["blocs"][bloc_indice]
                if "x" in b:
                    rectangle(b["x"] - TAILLE_BLOC_L//2, b["y"] - TAILLE_BLOC_H//2,
                              b["x"] + TAILLE_BLOC_L//2, b["y"] + TAILLE_BLOC_H//2,
                              couleur="white", epaisseur=2)
                else:
                    rectangle(b["coin1"][0], b["coin1"][1],
                              b["coin2"][0], b["coin2"][1],
                              couleur="white", epaisseur=2)
                mise_a_jour()
        elif etat_editeur["clics"]:
            idx = etat_editeur["clics"][0][1]
            b = etat_editeur["blocs"][idx]
            if "x" in b:
                b["x"] = x
                b["y"] = y
            else:
                dx = b["coin2"][0] - b["coin1"][0]
                dy = b["coin2"][1] - b["coin1"][1]
                b["coin1"] = (x - dx//2, y - dy//2)
                b["coin2"] = (x + dx//2, y + dy//2)
            etat_editeur["clics"] = []
            rafraichir_editeur(etat_editeur)
        return etat_editeur

    if mode == "SUPPRIMER":
        bloc_indice = trouver_bloc(x, y, etat_editeur)  # trouver_bloc gère les deux
        if bloc_indice is not None:
            etat_editeur["blocs"].pop(bloc_indice)
            rafraichir_editeur(etat_editeur)

        if etat_editeur["objectif"]:
            obj = etat_editeur["objectif"]
            if obj["coin1"][0] <= x <= obj["coin2"][0] and \
               obj["coin1"][1] <= y <= obj["coin2"][1]:
                etat_editeur["objectif"] = None
                rafraichir_editeur(etat_editeur)

        if etat_editeur["depart"]:
            dx, dy = etat_editeur["depart"]
            if dx - 25 <= x <= dx + 25 and dy - 25 <= y <= dy + 25:
                etat_editeur["depart"] = None
                rafraichir_editeur(etat_editeur)
        return etat_editeur

    if mode == "AJOUTER":
        etat_editeur["clics"].append((x, y))
        if len(etat_editeur["clics"]) == 2:
            c1 = etat_editeur["clics"][0]
            c2 = etat_editeur["clics"][1]
            x1, y1 = min(c1[0], c2[0]), min(c1[1], c2[1])
            x2, y2 = max(c1[0], c2[0]), max(c1[1], c2[1])
            etat_editeur["blocs"].append({
                "coin1": (x1, y1),
                "coin2": (x2, y2),
                "type": etat_editeur["type_bloc"]
            })
            etat_editeur["clics"] = []
            rafraichir_editeur(etat_editeur)
        elif len(etat_editeur["clics"]) == 1:
            rafraichir_editeur(etat_editeur)
            cercle(x, y, 4, remplissage="white")
            mise_a_jour()

    elif mode == "OBJECTIF":
        etat_editeur["clics"].append((x, y))
        if len(etat_editeur["clics"]) == 2:
            c1 = etat_editeur["clics"][0]
            c2 = etat_editeur["clics"][1]
            x1, y1 = min(c1[0], c2[0]), min(c1[1], c2[1])
            x2, y2 = max(c1[0], c2[0]), max(c1[1], c2[1])
            etat_editeur["objectif"] = {"coin1": (x1, y1), "coin2": (x2, y2)}
            etat_editeur["clics"] = []
            rafraichir_editeur(etat_editeur)
        elif len(etat_editeur["clics"]) == 1:
            rafraichir_editeur(etat_editeur)
            cercle(x, y, 4, remplissage="red")
            mise_a_jour()

    elif mode == "DEPART":
        etat_editeur["depart"] = (x, y)
        etat_editeur["clics"] = []
        rafraichir_editeur(etat_editeur)

    return etat_editeur

def afficher_victoire(score):
    image(400, 400, "ressource/image/fond/victoire.png")
    texte(400, 550,"Score : "+ str(score), couleur="white", taille=40, ancrage="center")
    image(400, 700, "ressource/image/fond/bouton_retour.png")
    mise_a_jour()