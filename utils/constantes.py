# Murs et sol
MUR_GAUCHE = [[0, 0],   [20, 780]]
MUR_DROIT  = [[780, 0], [800, 780]]
SOL        = [[0, 780], [800, 800]]

# Physique
VMAX       = 50
PAS        = 0.2
GRAVITE    = (0, 9.81)
STATUE_JEU = False

# Personnage
LARGEUR      = 20
HAUTEUR      = 20
TAILLE_PERSO = 10

# Dimensions des blocs par thème
HAUTEUR_BLOC = {
    "desert": 35,
    "espace": 33,
    "foret":  29,
    "pirate": 33,
}
LARGEUR_BLOC = {
    "desert": 100,
    "espace": 99,
    "foret":  98,
    "pirate": 100,
}

# Skins disponibles
LISTE_SKIN = [
    ["agent_secret",      "astronaute",       "aventurier"],
    ["batman",            "luigi",             "mario"],
    ["pirates",           "standar",           "superman"],
    ["eren",              "frisk_undertale",   "geometrie"],
    ["gojo",              "levi",              "mikassa"],
    ["papyrus_undertale", "undertale_sans",    None],
]
NB_SKINS_PAR_PAGE = 9

# Couleurs des rectangle pour les blocs sans image
COULEURS_BLOCS = {
    "normal":     "green",
    "glace":      "cyan",
    "derape":     "orange",
    "colant":     "purple",
    "elastique":  "yellow",
    "trampoline": "pink",
}

# Noms d'image des blocs spéciaux
NOMS_BLOCS_SPECIAUX = {
    "trampoline": "amorti.png",
    "colant":     "colant.png",
    "derape":     "derapage.png",
    "elastique":  "elastique.png",
    "glace":      "glissement.png",
}

# Tailles des blocs horizontaux
TAILLE_BLOC_L = 150
TAILLE_BLOC_H = 40

# Tailles des blocs verticaux
TAILLE_BLOC_V_L = 40
TAILLE_BLOC_V_H = 100

# Solveur
FINESSE_POSITION  = 5
INCREMENT_VITESSE = 5