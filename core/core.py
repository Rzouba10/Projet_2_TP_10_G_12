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

class Bloc:
    def __init__(self,coin_sup_gauche,coin_inf_droit,type):
        self.coin_sup_gauche = coin_sup_gauche
        self.coin_inf_droit = coin_inf_droit
        self.type = type

    def __str__(self):
        return f'{self.coin_sup_gauche} {self.coin_inf_droit} {self.type}'
        

jeu = Game()
jeu.ranger_donnees("niveaux/desert/nv1.txt")
print(jeu.lst_blocs[0])