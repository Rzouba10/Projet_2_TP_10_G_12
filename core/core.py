from math import *
#from utils.constantes import *

class Game:

    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.vitesse_x = 0
        self.vitesse_y = 0
        self.nb_jump = 0
        self.objectif = None
        self.lst_blocs = list()
        
    def lire_fichier_niveau(self,fichier):
        lignes = list()
        f = open(fichier, "r", encoding="utf-8")
        for ligne in f:
            ligne = ligne.rstrip()
            lignes.append(ligne)
        f.close()
        return lignes

    def ranger_donnees(self,fichier):
        donnes = self.lire_fichier_niveau(fichier)
        x = donnes[0].split(",")
        self.position_x = int(x[0])
        self.position_y = int(x[1])

        y = donnes[1].split(",")
        self.objectif = [(int(y[0]),int(y[1])),(int(y[2]),int(y[3]))]

        for i in range(2,len(donnes)):
            temp = donnes[i].split(",")
            self.lst_blocs.append(
                Bloc((int(temp[0]),int(temp[1])),(int(temp[2]),int(temp[3])),temp[4])
            )
    
    def clic_vers_vitesse(self, clic):
        u_x = clic[0] - self.position_x
        u_y = clic[1] - self.position_y
        distance = sqrt(u_x**2+u_y**2)
        if distance > VMAX:
            ratio = VMAX / distance
        else:
            ratio = 1
        u_x= u_x*ratio + self.position_x
        u_y= u_y*ratio + self.position_y

        return (int(u_x),int(u_y))

    def detection_colision(self,coin_sup_gauche,coin_inf_droit):
        x_max = coin_inf_droit[0]
        x_min = coin_sup_gauche[0]
        y_max = coin_sup_gauche[1]
        y_min = coin_inf_droit[1]

        if (self.position_x >= x_min and self.position_x <= x_max) and (self.position_y >= y_min and self.position_x <= y_max):
            return True

    def en_collision(self):
        for bloc in self.lst_blocs:
            if self.detection_colision(bloc.coin_sup_gauche,bloc.coin_inf_droit):
                return True
        return False

    def is_winnable(self):
        return self.en_collision(self.objectif[0],self.objectif[1])

class Bloc:
    def __init__(self,coin_sup_gauche,coin_inf_droit,type):
        self.coin_sup_gauche = coin_sup_gauche
        self.coin_inf_droit = coin_inf_droit
        self.type = type

    def __str__(self):
        return f'{self.coin_sup_gauche} {self.coin_inf_droit} {self.type}'
        
VMAX = 50
jeu = Game()
jeu.ranger_donnees("niveaux/desert/nv1.txt")
print(jeu.en_collision())
print(jeu.lst_blocs[0])