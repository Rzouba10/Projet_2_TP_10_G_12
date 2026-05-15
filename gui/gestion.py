from requirement.fltk import * 
from core.core import * 
from gui.interface import * 
from utils.constantes import * 
from utils.sauvegarde import * 
from core.solveur import * 
import os 
 
def maj_page(etat, nouvelle_page): 
    etat.page = nouvelle_page["page"] 
    etat.nb_pages = nouvelle_page["nb_pages"] 
    etat.tranche = nouvelle_page["tranche"] 

def dans_zone(x, y, xmin, xmax, ymin, ymax):
    return xmin <= x <= xmax and ymin <= y <= ymax

def clic_principal(x, y, etat):
    if dans_zone(x, y, 260, 410, 650, 690):
        etat.menu = "SKIN"
        charger_menue_skin(etat.skin)
    elif dans_zone(x, y, 290, 510, 280, 340):
        etat.menu = "THEME"
        efface_tout()
        image(400, 400, "ressource/image/fond/menue.png")
        image(400, 400, "ressource/image/fond/theme.png")
        image(400, 750, "ressource/image/fond/bouton_retour.png")
    elif dans_zone(x, y, 290, 510, 460, 520):
        etat.menu = "EDITEUR"
        maj_page(etat, page_niveaux())

def clic_skin(x, y, mon_jeu, etat):
    if dans_zone(x, y, 300, 500, 720, 780):
        if etat.niveau == 0:
            etat.menu = "PRINCIPAL"
            efface_tout()
            charger_menue(etat.skin, premier_lancement=False)
            return etat
        else:
            nv_skin = f"{etat.skin}_j"
            etat.menu = "NIVEAU"
            charger_page_niveau(etat.theme, etat.niveau, nv_skin, mon_jeu)
    
    taille_demi_case = 75
    for i in range(3):
        for j in range(3):
            centre_x = 200 + (j * 200)
            centre_y = 200 + (i * 200)
            if dans_zone(x, y, centre_x - taille_demi_case, centre_x + taille_demi_case, 
                               centre_y - taille_demi_case, centre_y + taille_demi_case):
                etat.skin = LISTE_SKIN[i][j]
                charger_menue_skin(etat.skin)
                return etat

def clic_editeur(x, y, etat):
    if dans_zone(x, y, 300, 500, 730, 790):
        etat.menu = "PRINCIPAL"
        efface_tout()
        charger_menue(etat.skin, premier_lancement=False)
        return etat

    if 691 <= y <= 749:
        if etat.page > 0 and 268 <= x <= 332:
            maj_page(etat, page_niveaux(etat.page - 1))
        elif etat.page < etat.nb_pages - 1 and 468 <= x <= 532:
            maj_page(etat, page_niveaux(etat.page + 1))

    for index, nom_fichier in enumerate(etat.tranche):
        centre_y = 240 + index * 79
        if centre_y - 29 <= y <= centre_y + 29:
            if 577 <= x <= 643: # Supprimer
                os.remove(f"niveaux/creation/{nom_fichier}")
                maj_page(etat, page_niveaux(etat.page))
            elif 503 <= x <= 567: # Éditer
                etat.menu = "EDITEUR_NV"
                efface_tout()

    for index in range(len(etat.tranche), 5):
        centre_y = 240 + index * 79
        if centre_y - 29 <= y <= centre_y + 29 and 577 <= x <= 643:
            etat.menu = "EDITEUR_NV"
            afichage_editeur()

def clic_editeur_nv(x, y, etat):
    if x <= 800:
        etat.editeur = gestion_clic_editeur(x, y, etat.editeur)
        return

    boutons = [
        (836, 970, 17, 51, "mode", "AJOUTER"),
        (836, 970, 54, 87, "mode", "MODIFIER"),
        (836, 970, 90, 123, "mode", "SUPPRIMER"),
        (838, 968, 330, 355, "mode", "OBJECTIF"),
        (863, 940, 383, 465, "mode", "DEPART"),
        (831, 891, 165, 185, "type_bloc", "normal"),
        (912, 985, 165, 185, "type_bloc", "glace"),
        (831, 891, 198, 218, "type_bloc", "derape"),
        (912, 985, 198, 218, "type_bloc", "colant"),
        (831, 891, 232, 252, "type_bloc", "elastique"),
        (912, 985, 232, 252, "type_bloc", "trampoline"),
        (833, 966, 522, 547, "theme", "desert"),
        (833, 964, 559, 584, "theme", "foret"),
        (833, 966, 594, 618, "theme", "espace"),
        (834, 965, 631, 657, "theme", "pirate"),
        (834, 966, 670, 693, "theme", None)
    ]

    for xmin, xmax, ymin, ymax, cle, valeur in boutons:
        if dans_zone(x, y, xmin, xmax, ymin, ymax):
            etat.editeur[cle] = valeur
            if cle == "mode":
                etat.editeur["clics"] = []
            elif cle == "theme":
                etat.editeur["mode"] = "AJOUTER"
            rafraichir_editeur(etat.editeur)
            return

    if dans_zone(x, y, 836, 970, 755, 780):
        editeur = etat.editeur
        
        if not editeur["blocs"] or editeur["objectif"] is None or editeur["depart"] is None:
            etat.menu = "ALERTE"
            efface_tout()
            image(500, 400, "ressource/image/fond/editeur_alerte.png")
            mise_a_jour()
            return

        jeu_test = Game()
        dx, dy = editeur["depart"]
        jeu_test.position_x = dx
        jeu_test.position_y = dy
        obj = editeur["objectif"]
        x1, y1 = obj["coin1"]
        x2, y2 = obj["coin2"]
        jeu_test.objectif = [(x1, y1), (x2, y2)]
        
        for bloc in editeur["blocs"]:
            if "x" in bloc:
                cx, cy = bloc["x"], bloc["y"]
                bx1 = cx - TAILLE_BLOC_L // 2
                by1 = cy - TAILLE_BLOC_H // 2
                bx2 = cx + TAILLE_BLOC_L // 2
                by2 = cy + TAILLE_BLOC_H // 2
            else:
                bx1, by1 = bloc["coin1"]
                bx2, by2 = bloc["coin2"]
            jeu_test.lst_blocs.append(Bloc((bx1, by1), (bx2, by2), bloc["type"]))

        objectif_test = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
        solution = solveur_largeur(jeu_test, objectif_test)

        if solution is None:
            etat.menu = "ALERTE"
            efface_tout()
            image(500, 400, "ressource/image/fond/editeur_alerte.png")
            mise_a_jour()
            return 
        
        etat.menu = "THEME_SAVE"
        page_choix_theme_sauvegarde()
        
    elif dans_zone(x, y, 820, 970, 710, 750):
        etat.menu = "EDITEUR"
        etat.reset_editeur()
        efface_tout()
        redimensionne_fenetre(800, 800)
        maj_page(etat, page_niveaux())
        return etat

def clic_alerte(x, y, etat):
    if dans_zone(x, y, 383, 617, 375, 415):
        etat.menu = "EDITEUR_NV"
        afichage_editeur()
        rafraichir_editeur(etat.editeur)

def clic_theme_save(x, y, etat):
    if not (383 <= x <= 617):
        return etat

    themes = [
        (255, 295, "desert"),
        (318, 358, "foret"),
        (380, 420, "espace"),
        (442, 482, "pirate"),
        (504, 544, "none"),
    ]

    for ymin, ymax, theme_choisi in themes:
        if ymin <= y <= ymax:
            sauvegarder_niveau(etat.editeur, theme_choisi)
            etat.reset_editeur()
            etat.menu = "EDITEUR"
            redimensionne_fenetre(800, 800)
            maj_page(etat, page_niveaux())
            return etat

    return etat

def clic_creation(x, y, mon_jeu, etat):
    if dans_zone(x, y, 300, 500, 730, 790):
        etat.menu = "THEME"
        efface_tout()
        image(400, 400, "ressource/image/fond/menue.png")
        image(400, 400, "ressource/image/fond/theme.png")
        image(400, 750, "ressource/image/fond/bouton_retour.png")
        return etat

    if 691 <= y <= 749:
        if etat.page > 0 and 268 <= x <= 332:
            maj_page(etat, page_niveaux_creation(etat.page - 1))
        elif etat.page < etat.nb_pages - 1 and 468 <= x <= 532:
            maj_page(etat, page_niveaux_creation(etat.page + 1))

    for index, nom_fichier in enumerate(etat.tranche):
        centre_y = 240 + index * 79
        if centre_y - 29 <= y <= centre_y + 29:
            if 503 <= x <= 567:
                chemin = f"niveaux/creation/{nom_fichier}"
                etat.niveau = 0         
                etat.theme = mon_jeu.theme
                nv_skin = f"{etat.skin}_j"
                etat.trace.clear()
                mon_jeu.vider()
                mon_jeu.ranger_donnees(chemin)
                etat.theme = mon_jeu.style
                etat.menu = "JEU"
                charger_niveau(nv_skin, mon_jeu, etat.theme)
                return etat

def clic_theme(x, y, etat):
    if dans_zone(x, y, 300, 500, 720, 780):
        etat.menu = "PRINCIPAL"
        efface_tout()
        charger_menue(etat.skin, premier_lancement=False)
        return etat
    
    themes = [
        (80, 200, "foret"),
        (210, 330, "pirate"),
        (340, 460, "desert"),
        (470, 590, "espace"),
        (600, 720, "creation")
    ]
    
    if 130 <= x <= 670:
        for ymin, ymax, nom_theme in themes:
            if ymin <= y <= ymax:
                if nom_theme == "creation":
                    etat.menu = "CREATION"
                    maj_page(etat, page_niveaux_creation())
                    return
                etat.menu = "NIVEAU"
                etat.theme = nom_theme
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, f"ressource/image/fond/menu_niveau/{nom_theme}_nv.png")
                image(400, 750, "ressource/image/fond/bouton_retour.png")
                return

def clic_niveau(x, y, mon_jeu, etat):
    if dans_zone(x, y, 300, 500, 720, 780):
        etat.menu = "PRINCIPAL"
        efface_tout()
        charger_menue(etat.skin, premier_lancement=False)
        return etat
    
    niveaux = [
        (170, 300, 1),
        (320, 440, 2),
        (460, 590, 3)
    ]
    
    if 130 <= x <= 670:
        for ymin, ymax, num_niveau in niveaux:
            if ymin <= y <= ymax:
                etat.menu = "JEU"
                etat.niveau = num_niveau
                nv_skin = f"{etat.skin}_j"
                etat.trace.clear()
                mon_jeu.vider()
                charger_page_niveau(etat.theme, etat.niveau, nv_skin, mon_jeu)
                return

def clic_jeu(x, y, mon_jeu, etat):
    nv_skin = f"{etat.skin}_j"
    charger_niveau(nv_skin, mon_jeu, etat.theme)
    vect = mon_jeu.clic_vers_vitesse((x, y))
    dessiner_vecteur(mon_jeu, vect)

def clic_pause(x, y, mon_jeu, etat):
    if dans_zone(x, y, 250, 540, 270, 340):
        nv_skin = f"{etat.skin}_j"
        etat.menu = "JEU"
        charger_niveau(nv_skin, mon_jeu, etat.theme)
    elif dans_zone(x, y, 250, 540, 360, 430):
        etat.menu = "SOLVEUR"
        efface(etat.menue)
        image(400, 400, "ressource/image/fond/pause_solver.png")
    elif dans_zone(x, y, 250, 540, 460, 530):
        etat.menu = "P_SAVE"
        efface(etat.menue)
        image(400, 400, "ressource/image/fond/pause_save.png")

def clic_p_save(x, y, etat):
    if 380 <= y <= 460:
        if 250 <= x <= 340:
            etat.niveau = 0
            etat.theme = ""
            etat.menu = "PRINCIPAL"
            efface_tout()
            charger_menue(etat.skin, premier_lancement=False)
            return etat
        elif 450 <= x <= 550:
            etat.menu = "SAVE"

def clic_solveur(x, y, mon_jeu, etat):
    if not (310 <= y <= 420): 
        return
        
    nv_skin = f"{etat.skin}_j"

    if 520 <= x <= 710: 
        etat.menu = "JEU"
        charger_niveau(nv_skin, mon_jeu, etat.theme)
        return

    if (90 <= x <= 280) or (300 <= x <= 500):
        if mon_jeu.objectif is None:
            etat.menu = "JEU"
            return
            
        objectif = {
            "x1": mon_jeu.objectif[0][0], "y1": mon_jeu.objectif[0][1],
            "x2": mon_jeu.objectif[1][0], "y2": mon_jeu.objectif[1][1],
        }
        
        def progression(positions_visitees):
            afficher_positions_visitees(mon_jeu, positions_visitees, nv_skin, etat.theme)
            
        etat.menu = "JEU"
        
        if 90 <= x <= 280:
            solution = solveur_profondeur(mon_jeu, objectif, afficher_progression=progression)
        else:
            solution = solveur_largeur(mon_jeu, objectif, afficher_progression=progression)
            
        if solution is not None:
            rejouer_solution(mon_jeu, solution, nv_skin, etat.theme, etat.trace)
        else:
            charger_niveau(nv_skin, mon_jeu, etat.theme)


def gestion_clique(x, y, mon_jeu, etat):
    
    if STATUE_JEU: 
        return etat

    actions_menu = {
        "PRINCIPAL": lambda: clic_principal(x, y, etat),
        "SKIN": lambda: clic_skin(x, y, mon_jeu, etat),
        "EDITEUR": lambda: clic_editeur(x, y, etat),
        "EDITEUR_NV": lambda: clic_editeur_nv(x, y, etat),
        "THEME_SAVE": lambda: clic_theme_save(x, y, etat),
        "THEME": lambda: clic_theme(x, y, etat),
        "CREATION":    lambda: clic_creation(x, y, mon_jeu, etat),
        "NIVEAU": lambda: clic_niveau(x, y, mon_jeu, etat),
        "JEU": lambda: clic_jeu(x, y, mon_jeu, etat),
        "PAUSE": lambda: clic_pause(x, y, mon_jeu, etat),
        "P_SAVE": lambda: clic_p_save(x, y, etat),
        "ALERTE": lambda: clic_alerte(x, y, etat),
        "SOLVEUR": lambda: clic_solveur(x, y, mon_jeu, etat)
    }

    action = actions_menu.get(etat.menu)
    
    if action:
        resultat = action()

        if resultat is not None:
            return resultat

    return etat
