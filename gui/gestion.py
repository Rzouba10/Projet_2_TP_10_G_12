from requirement.fltk import *
from core.core import *
from gui.interface import *
from utils.constantes import *
from utils.sauvegarde import *
import os

def maj_page(etat, nouvelle_page):
    etat.page = nouvelle_page["page"]
    etat.nb_pages = nouvelle_page["nb_pages"]
    etat.tranche = nouvelle_page["tranche"]


def gestion_clique(x, y, mon_jeu, etat): 
    
    if STATUE_JEU == False: 

        if etat.menu == "PRINCIPAL":
            if 260 <= x <= 410 and 650 <= y <= 690:
                etat.menu = "SKIN"
                charger_menue_skin(etat.skin)
            
            if 290 <= x <= 510 and 280 <= y <= 340:
                etat.menu = "THEME"
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, "ressource/image/fond/theme.png")
                image(400, 750, "ressource/image/fond/bouton_retour.png")
            
            if 290 <= x <= 510 and 460 <= y <= 520:
                etat.menu = "EDITEUR"
                maj_page(etat, page_niveaux())

        elif etat.menu == "SKIN":
            
            if 300 <= x <= 500 and 720 <= y <= 780:
                if etat.niveau == 0:
                    etat.menu = "PRINCIPAL"
                    efface_tout()
                    charger_menue(etat.skin, premier_lancement=False) 
                    return etat
                else:
                    nv_skin = etat.skin + "_j"
                    etat.menu = "NIVEAU"
                    charger_page_niveau(etat.theme, etat.niveau, nv_skin, mon_jeu)
            
            taille_demi_case = 75
            
            for i in range(3):
                for j in range(3):
                    centre_x = 200 + (j * 200)
                    centre_y = 200 + (i * 200)
                    
                    if (centre_x - taille_demi_case <= x <= centre_x + taille_demi_case) and \
                       (centre_y - taille_demi_case <= y <= centre_y + taille_demi_case):
                        
                        etat.skin = LISTE_SKIN[i][j]
                        charger_menue_skin(etat.skin)
                        return etat

        elif etat.menu == "EDITEUR":
            
            if 300 <= x <= 500 and 730 <= y <= 790:
                etat.menu = "PRINCIPAL"
                efface_tout()
                charger_menue(etat.skin, premier_lancement=False)
                return etat

            if etat.page > 0 and 268 <= x <= 332 and 691 <= y <= 749:
                maj_page(etat, page_niveaux(etat.page - 1))

            if etat.page < etat.nb_pages - 1 and 468 <= x <= 532 and 691 <= y <= 749:
                maj_page(etat, page_niveaux(etat.page + 1))

            for index, nom_fichier in enumerate(etat.tranche):
                centre_y = 240 + index * 79
                if centre_y - 29 <= y <= centre_y + 29:
                    if 577 <= x <= 643:
                        os.remove("niveaux/creation/" + nom_fichier)
                        maj_page(etat, page_niveaux(etat.page))
                    if 503 <= x <= 567:
                        etat.menu = "EDITEUR_NV"
                        efface_tout()

            for index in range(len(etat.tranche), 5):
                centre_y = 240 + index * 79
                if centre_y - 29 <= y <= centre_y + 29:
                    if 577 <= x <= 643:
                        etat.menu = "EDITEUR_NV"
                        afichage_editeur()
        
        elif etat.menu == "EDITEUR_NV":

            if x > 800:
                if 836 <= x <= 970 and 17 <= y <= 51:
                    etat.editeur["mode"] = "AJOUTER"
                    etat.editeur["clics"] = []
                    rafraichir_editeur(etat.editeur)

                elif 836 <= x <= 970 and 54 <= y <= 87:
                    etat.editeur["mode"] = "MODIFIER"
                    etat.editeur["clics"] = []
                    rafraichir_editeur(etat.editeur)

                elif 836 <= x <= 970 and 90 <= y <= 123:
                    etat.editeur["mode"] = "SUPPRIMER"
                    etat.editeur["clics"] = []
                    rafraichir_editeur(etat.editeur)

                elif 831 <= x <= 891 and 165 <= y <= 185:
                    etat.editeur["type_bloc"] = "normal"
                    rafraichir_editeur(etat.editeur)

                elif 912 <= x <= 985 and 165 <= y <= 185:
                    etat.editeur["type_bloc"] = "glace"
                    rafraichir_editeur(etat.editeur)

                elif 831 <= x <= 891 and 198 <= y <= 218:
                    etat.editeur["type_bloc"] = "derape"
                    rafraichir_editeur(etat.editeur)

                elif 912 <= x <= 985 and 198 <= y <= 218:
                    etat.editeur["type_bloc"] = "colant"
                    rafraichir_editeur(etat.editeur)

                elif 831 <= x <= 891 and 232 <= y <= 252:
                    etat.editeur["type_bloc"] = "elastique"
                    rafraichir_editeur(etat.editeur)

                elif 912 <= x <= 985 and 232 <= y <= 252:
                    etat.editeur["type_bloc"] = "trampoline"
                    rafraichir_editeur(etat.editeur)

                elif 838 <= x <= 968 and 330 <= y <= 355:
                    etat.editeur["mode"] = "OBJECTIF"
                    etat.editeur["clics"] = []
                    rafraichir_editeur(etat.editeur)

                elif 863 <= x <= 940 and 383 <= y <= 465:
                    etat.editeur["mode"] = "DEPART"
                    etat.editeur["clics"] = []
                    rafraichir_editeur(etat.editeur)
                
                elif 833 <= x <= 966 and 522 <= y <= 547:
                    etat.editeur["theme"] = "desert"
                    etat.editeur["mode"] = "AJOUTER"
                    rafraichir_editeur(etat.editeur)

                elif 833 <= x <= 964 and 559 <= y <= 584:
                    etat.editeur["theme"] = "foret"
                    etat.editeur["mode"] = "AJOUTER"
                    rafraichir_editeur(etat.editeur)

                elif 833 <= x <= 966 and 594 <= y <= 618:
                    etat.editeur["theme"] = "espace"
                    etat.editeur["mode"] = "AJOUTER"
                    rafraichir_editeur(etat.editeur)

                elif 834 <= x <= 965 and 631 <= y <= 657:
                    etat.editeur["theme"] = "pirate"
                    etat.editeur["mode"] = "AJOUTER"
                    rafraichir_editeur(etat.editeur)

                elif 834 <= x <= 966 and 670 <= y <= 693:
                    etat.editeur["theme"] = None   
                    etat.editeur["mode"] = "AJOUTER"
                    rafraichir_editeur(etat.editeur)
                
                elif 836 <= x <= 970 and 755 <= y <= 780:
                    sauvegarder_niveau(etat.editeur)
                    etat.reset_editeur()
                    etat.menu = "EDITEUR"
                    redimensionne_fenetre(800, 800)
                    maj_page(etat, page_niveaux())

                elif 820 <= x <= 970 and 710 <= y <= 750:
                    etat.menu = "EDITEUR"
                    etat.reset_editeur()
                    efface_tout()
                    redimensionne_fenetre(800, 800)
                    maj_page(etat, page_niveaux())
                    return etat

            else:
                etat.editeur = gestion_clic_editeur(x, y, etat.editeur)
        
        elif etat.menu == "THEME":
            
            if 300 <= x <= 500 and 720 <= y <= 780:
                etat.menu = "PRINCIPAL"
                efface_tout()
                charger_menue(etat.skin, premier_lancement=False) 
                return etat
            
            if 130 <= x <= 670 and 80 <= y <= 200:
                etat.menu = "NIVEAU"
                etat.theme = "foret"
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, "ressource/image/fond/menu_niveau/foret_nv.png")
                image(400, 750, "ressource/image/fond/bouton_retour.png")
                
            if 130 <= x <= 670 and 210 <= y <= 330:
                etat.menu = "NIVEAU"
                etat.theme = "pirate"
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, "ressource/image/fond/menu_niveau/pirate_nv.png")
                image(400, 750, "ressource/image/fond/bouton_retour.png")
            
            if 130 <= x <= 670 and 340 <= y <= 460:
                etat.menu = "NIVEAU"
                etat.theme = "desert"
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, "ressource/image/fond/menu_niveau/desert_nv.png")
                image(400, 750, "ressource/image/fond/bouton_retour.png")
            
            if 130 <= x <= 670 and 470 <= y <= 590:
                etat.menu = "NIVEAU"
                etat.theme = "espace"
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, "ressource/image/fond/menu_niveau/espace_nv.png")
                image(400, 750, "ressource/image/fond/bouton_retour.png")
        
        elif etat.menu == "NIVEAU":
            
            if 300 <= x <= 500 and 720 <= y <= 780:
                etat.menu = "PRINCIPAL"
                efface_tout()
                charger_menue(etat.skin, premier_lancement=False) 
                return etat
            
            if 130 <= x <= 670 and 170 <= y <= 300:
                etat.menu = "JEU"
                etat.niveau = 1
                nv_skin = etat.skin + "_j"
                etat.trace.clear()
                mon_jeu.vider() 
                charger_page_niveau(etat.theme, etat.niveau, nv_skin, mon_jeu)
            
            if 130 <= x <= 670 and 320 <= y <= 440:
                etat.menu = "JEU"
                etat.niveau = 2
                nv_skin = etat.skin + "_j"
                etat.trace.clear()
                mon_jeu.vider()
                charger_page_niveau(etat.theme, etat.niveau, nv_skin, mon_jeu)
            
            if 130 <= x <= 670 and 460 <= y <= 590:
                etat.menu = "JEU"
                etat.niveau = 3
                nv_skin = etat.skin + "_j"
                etat.trace.clear()
                mon_jeu.vider()  
                charger_page_niveau(etat.theme, etat.niveau, nv_skin, mon_jeu)

        elif etat.menu == "JEU":
            nv_skin = etat.skin + "_j"
            charger_niveau(nv_skin, mon_jeu, etat.theme)

            vect = mon_jeu.clic_vers_vitesse((x, y))
            dessiner_vecteur(mon_jeu, vect)

        elif etat.menu == "PAUSE":
            if 250 <= x <= 540 and 270 <= y <= 340:
                nv_skin = etat.skin + "_j"
                etat.menu = "JEU"
                charger_page_niveau(etat.theme, etat.niveau, nv_skin, mon_jeu)
            
            if 250 <= x <= 540 and 360 <= y <= 430:
                etat.menu = "SOLVEUR"
                efface(etat.menue)
                image(400, 400, "ressource/image/fond/pause_solver.png")
                
            if 250 <= x <= 540 and 460 <= y <= 530:
                etat.menu = "P_SAVE"
                efface(etat.menue)
                image(400, 400, "ressource/image/fond/pause_save.png")

        elif etat.menu == "P_SAVE":
            
            if 250 <= x <= 340 and 380 <= y <= 460:
                etat.niveau = 0
                etat.theme = ""
                etat.menu = "PRINCIPAL"
                efface_tout()
                charger_menue(etat.skin, premier_lancement=False) 
                return etat

            if 450 <= x <= 550 and 380 <= y <= 460:
                etat.menu = "SAVE"
        
        elif etat.menu == "SOLVEUR":
    
            pass
            
    return etat
