from utils.structure import *
from utils.constantes import *
from requirement.fltk import *
from gui.interface import *
from time import *

FINESSE_POSITION = 10
INCREMENT_VITESSE = 10


def simuler_saut(jeu, vitesse_x, vitesse_y, objectif=None):
    from utils.constantes import PAS, GRAVITE

    pos_x_sauvegarde = jeu.position_x
    pos_y_sauvegarde = jeu.position_y
    vx_sauvegarde    = jeu.vitesse_x
    vy_sauvegarde    = jeu.vitesse_y

    jeu.vitesse_x = vitesse_x
    jeu.vitesse_y = vitesse_y

    position_finale  = None
    objectif_atteint = False

    for _ in range(5000):
        resultat = jeu.pas()

        if objectif is not None and est_dans_objectif(jeu, objectif):
            position_finale  = (jeu.position_x, jeu.position_y)
            objectif_atteint = True
            break

        if resultat == "Finish":          # joueur posé sur un bloc
            position_finale = (jeu.position_x, jeu.position_y)
            break

        if jeu.position_y > 800 or jeu.position_y < 0:
            position_finale = None
            break

    jeu.position_x = pos_x_sauvegarde
    jeu.position_y = pos_y_sauvegarde
    jeu.vitesse_x  = vx_sauvegarde
    jeu.vitesse_y  = vy_sauvegarde

    return position_finale, objectif_atteint


def est_dans_objectif(jeu, objectif):
    x = jeu.position_x
    y = jeu.position_y
    
    return (objectif["x1"] <= x <= objectif["x2"] and
            objectif["y1"] <= y <= objectif["y2"])



def solveur_profondeur(jeu, objectif, afficher_progression=None):
    
    positions_visitees = set()
    
    liste_vitesses = generer_vitesses(INCREMENT_VITESSE)
    
    pile = Pile()
    
    position_depart = (jeu.position_x, jeu.position_y)
    pile.empiler((position_depart[0], position_depart[1], []))
    
    while not pile.est_vide():
        
        pos_x, pos_y, chemin = pile.depiler()
        
        jeu.position_x = pos_x
        jeu.position_y = pos_y
        
        if est_dans_objectif(jeu, objectif):
            jeu.position_x = position_depart[0]
            jeu.position_y = position_depart[1]
            return chemin
        
        pos_approchee = position_approchee(pos_x, pos_y, FINESSE_POSITION)
        
        if pos_approchee in positions_visitees:
            continue
        
        positions_visitees.add(pos_approchee)
        
        if afficher_progression is not None:
            afficher_progression(positions_visitees)
        
        for (vx, vy) in liste_vitesses:
            
            position_apres_saut, objectif_atteint = simuler_saut(jeu, vx, vy, objectif)
            
            if position_apres_saut is not None:
                nouvelle_x, nouvelle_y = position_apres_saut
                
                if objectif_atteint:
                    jeu.position_x = position_depart[0]
                    jeu.position_y = position_depart[1]
                    return chemin + [(vx, vy)]
                
                pile.empiler((nouvelle_x, nouvelle_y, chemin + [(vx, vy)]))
    
    jeu.position_x = position_depart[0]
    jeu.position_y = position_depart[1]
    return None



def solveur_largeur(jeu, objectif, afficher_progression=None):
    
    positions_visitees = set()
    liste_vitesses     = generer_vitesses(INCREMENT_VITESSE)
    
    file = File()
    
    position_depart = (jeu.position_x, jeu.position_y)
    file.enfiler((position_depart[0], position_depart[1], []))
    
    while not file.est_vide():
        
        pos_x, pos_y, chemin = file.defiler()
        
        jeu.position_x = pos_x
        jeu.position_y = pos_y
        
        if est_dans_objectif(jeu, objectif):
            jeu.position_x = position_depart[0]
            jeu.position_y = position_depart[1]
            return chemin
        
        pos_approchee = position_approchee(pos_x, pos_y, FINESSE_POSITION)
        
        if pos_approchee in positions_visitees:
            continue
        
        positions_visitees.add(pos_approchee)
        
        if afficher_progression is not None:
            afficher_progression(positions_visitees)
        
        for (vx, vy) in liste_vitesses:
            
            position_apres_saut, objectif_atteint = simuler_saut(jeu, vx, vy, objectif)
        
            if position_apres_saut is not None:
                nouvelle_x, nouvelle_y = position_apres_saut
                
                if objectif_atteint:
                    jeu.position_x = position_depart[0]
                    jeu.position_y = position_depart[1]
                    return chemin + [(vx, vy)]  # ← on retourne immédiatement
                
                file.enfiler((nouvelle_x, nouvelle_y, chemin + [(vx, vy)]))
    
    jeu.position_x = position_depart[0]
    jeu.position_y = position_depart[1]
    return None

def afficher_positions_visitees(jeu, positions_visitees, skin, theme):
    
    charger_niveau(skin, jeu, theme, mise_a_jour_auto=False, dessiner_perso=True)
    
    for (px, py) in positions_visitees:
        vrai_x = px * FINESSE_POSITION
        vrai_y = py * FINESSE_POSITION
        image(vrai_x, vrai_y, f"ressource/image/perso/{skin}.png")
    
    mise_a_jour()


def rejouer_solution(jeu, chemin_solution, skin, theme, trace):
    from gui.interface import mouvement
    
    trace.clear()
    
    for (vx, vy) in chemin_solution:
        jeu.vitesse_x = vx
        jeu.vitesse_y = vy
        mouvement(jeu, skin, theme, trace)
        
    
    
