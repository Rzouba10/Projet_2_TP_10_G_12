from requirement.fltk import *
from gui.interface import *

if __name__ == "__main__":
    cree_fenetre(800,800)

    points = []

    init_niveaux()

    while True:

        evenement = attend_ev()
        type_evenement = type_ev(evenement)

        if type_evenement == "Quitte":
            break

        if type_evenement == "ClicGauche":
            x = abscisse(evenement)
            y = ordonnee(evenement)

            # creation de niveau

            if len(points) == 2:
                rectangle(points[0][0],points[0][1],points[1][0],points[1][1],remplissage="yellow")
                points = []
            else:
                points.append((x,y))

    print(points)

    ferme_fenetre()