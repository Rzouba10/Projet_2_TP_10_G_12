from requirement.fltk import *
from utils.constantes import *
from time import *

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

def retour_arriere():
    pass

