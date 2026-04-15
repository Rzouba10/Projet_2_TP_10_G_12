from requirement.fltk import *
from core.core import *
from gui.interface import *
from utils.constantes import *

def gestion_clique(x,y,mon_jeu):
    
    global menu_actuel, skin, theme, niveau
    
    if STATUE_JEU == False: 

        if menu_actuel == "PRINCIPAL":
            if 260 <= x <= 410 and 650 <= y <= 690:
                menu_actuel = "SKIN"
                charger_menue_skin(skin)
            
            if 290 <= x <= 510 and 280 <= y <= 340:
                menu_actuel = "THEME"
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, "ressource/image/fond/theme.png")
                retour = image(400, 750, "ressource/image/fond/bouton_retour.png")
            
            if 290 <= x <= 510 and 460 <= y <= 520:
                menu_actuel = "EDITEUR"
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, "ressource/image/fond/creation.png")
                retour = image(400, 770, "ressource/image/fond/bouton_retour.png")

        elif menu_actuel == "SKIN":
            
            if 300 <= x <= 500 and 720 <= y <= 780:
                if niveau == 0:
                    menu_actuel = "PRINCIPAL"
                    efface_tout()
                    charger_menue(skin, premier_lancement=False) 
                    return

            
            taille_demi_case = 75
            
            for i in range(3):
                for j in range(3):
                    centre_x = 200 + (j * 200)
                    centre_y = 200 + (i * 200)
                    
                    if (centre_x - taille_demi_case <= x <= centre_x + taille_demi_case) and \
                       (centre_y - taille_demi_case <= y <= centre_y + taille_demi_case):
                        
                        skin = LISTE_SKIN[i][j]
                        
                        charger_menue_skin(skin)
                        
                        return

        elif menu_actuel == "EDITEUR":

            if 300 <= x <= 500 and 730 <= y <= 790:
                menu_actuel = "PRINCIPAL"
                efface_tout()
                charger_menue(skin, premier_lancement=False) 
                return

        elif menu_actuel == "THEME":
            
            if 300 <= x <= 500 and 720 <= y <= 780:
                menu_actuel = "PRINCIPAL"
                efface_tout()
                charger_menue(skin, premier_lancement=False) 
                return
            
            # Fortet
            if 130 <= x <= 670 and 80 <= y <= 200:
                menu_actuel = "NIVEAU"
                theme = "foret"
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, "ressource/image/fond/menu_niveau/foret_nv.png")
                image(400, 750, "ressource/image/fond/bouton_retour.png")
                
            # Pirate
            if 130 <= x <= 670 and 210 <= y <= 330:
                menu_actuel = "NIVEAU"
                theme = "pirate"
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, "ressource/image/fond/menu_niveau/pirate_nv.png")
                image(400, 750, "ressource/image/fond/bouton_retour.png")
            
            # Desert
            if 130 <= x <= 670 and 340 <= y <= 460:
                menu_actuel = "NIVEAU"
                theme = "desert"
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, "ressource/image/fond/menu_niveau/desert_nv.png")
                image(400, 750, "ressource/image/fond/bouton_retour.png")
            
            # Espace
            if 130 <= x <= 670 and 470 <= y <= 590:
                menu_actuel = "NIVEAU"
                theme = "espace"
                efface_tout()
                image(400, 400, "ressource/image/fond/menue.png")
                image(400, 400, "ressource/image/fond/menu_niveau/espace_nv.png")
                image(400, 750, "ressource/image/fond/bouton_retour.png")
                
        
        
        elif menu_actuel == "NIVEAU":
            
            
            if 300 <= x <= 500 and 720 <= y <= 780:
                menu_actuel = "PRINCIPAL"
                efface_tout()
                charger_menue(skin, premier_lancement=False) 
                return

            if 130 <= x <= 670 and 170 <= y <= 300:
                pass

if __name__ == "__main__":
    
    menu_actuel = "PRINCIPAL"
    skin = "standar"
    theme = ""
    niveau = 0
    creation = []
    
    point = []
    mon_jeu = Game()
    
    cree_fenetre(800,800)
    
    charger_menue(skin, premier_lancement=True)
    
    while True:
        evenement = attend_ev()
        type_evenement = type_ev(evenement)
        
        if type_ev(evenement) == "Quitte":
            break
        
        if type_ev(evenement) == "ClicGauche":
            x = abscisse(evenement)
            y = ordonnee(evenement)
            
            gestion_clique(x,y,mon_jeu)
            
            point.append((x,y))

    
    print(point)
    
    ferme_fenetre()