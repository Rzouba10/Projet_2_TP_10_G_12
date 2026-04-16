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

def mouvement(jeu,skin,theme):

    STATUE_JEU = True

    while True:
        nouvelle_position = (jeu.position_x + jeu.vitesse_x) * PAS
        ancien_pos = jeu.position_x

        jeu.position_x = nouvelle_position

        if jeu.en_collision is None:
            jeu.position_x = ancien_pos
            jeu.vitesse_x = 0
        
        nouvelle_position_y = (jeu.position_x + jeu.vitesse_x) *PAS
        ancien_pos_y = jeu.position_x

        jeu.position_x = nouvelle_position_y

        if jeu.en_collision is False:
            jeu.position_x = ancien_pos_y
            jeu.vitesse_x = 0

            break
        
        jeu.vitesse_x += PAS * GRAVITE[0]
        jeu.vitesse_y += PAS * GRAVITE[1]

        charger_niveau(skin,jeu,theme)

        if jeu.position_x > 800:
            break

        if jeu.position_y > 800:
            break

        sleep(0.02)
    
    STATUE_JEU = False

def charger_niveau(skin,jeu,theme):
    efface_tout()

    print(jeu.position_x,jeu.position_y)

    image(400, 400, "ressource/image/fond/theme/"+str(theme)+".png")
    image(400, 400, "ressource/image/block/paroit/"+str(theme)+".png")
    image(jeu.position_x, jeu.position_y, "ressource/image/perso/"+str(skin)+"_j.png")

    for bloc in jeu.lst_blocs:
        image(max(bloc.coin_inf_droit[0],bloc.coin_sup_gauche[0])-(bloc.coin_inf_droit[0]-bloc.coin_sup_gauche[0]),max(bloc.coin_inf_droit[1],bloc.coin_sup_gauche[1])-(bloc.coin_inf_droit[1]-bloc.coin_sup_gauche[1]),"ressource/image/block/flotant/"+str(theme)+".png")


def dessiner_vecteur(jeu,vect):

    ligne(jeu.position_x,jeu.position_y, vect[0], vect[1], couleur="red",epaisseur=2)  
    fleche(jeu.position_x,jeu.position_y, vect[0], vect[1], couleur="red",epaisseur=2) 

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

