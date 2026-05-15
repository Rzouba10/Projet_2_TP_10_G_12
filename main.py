from requirement.fltk import *
from core.core import *
from utils.etat import *
from gui.gestion import *
        
if __name__ == "__main__":
    
    etat = EtatJeu()
    
    point = []
    mon_jeu = Game()
    
    cree_fenetre(800,800)
    
    charger_menue(etat.skin, premier_lancement=True)
    
    while True:
        evenement = attend_ev()
        type_evenement = type_ev(evenement)
        
        if type_ev(evenement) == "Quitte":
            break
        
        if type_ev(evenement) == "ClicGauche":
            x = abscisse(evenement)
            y = ordonnee(evenement)
            
            etat = gestion_clique(x, y, mon_jeu, etat)
            
            point.append((x,y))
        
        if type_evenement == "ClicDroit":
            x = abscisse(evenement)
            y = ordonnee(evenement)

            if etat.menu == "JEU" and not STATUE_JEU:
                nv_skin = etat.skin + "_j"
                etat.historique_departs.append((mon_jeu.position_x, mon_jeu.position_y))
                mouvement(mon_jeu,nv_skin,etat.theme,etat.trace)
                mon_jeu.nb_jump += 1
                print(mon_jeu.nb_jump, "SCORE_DEBUG")
        
        if type_ev(evenement) == "Touche" :
            ev = donne_ev()
            t = touche(evenement)
            
            if t == "Escape" and etat.menu == "JEU":
                etat.menue = image(400, 400, "ressource/image/fond/pause.png")
                etat.menu = "PAUSE"

            if t == "z" and etat.menu == "JEU" and not STATUE_JEU:
                nv_skin = f"{etat.skin}_j"
                retour_arriere(mon_jeu, nv_skin, etat.theme, etat.historique_departs)
            
    print(point)
    
    ferme_fenetre()