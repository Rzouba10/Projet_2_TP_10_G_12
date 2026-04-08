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

            points.append((x,y))

    print(points)

    ferme_fenetre()