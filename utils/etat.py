class EtatJeu:
    def __init__(self):
        
        self.menu = "PRINCIPAL"
        self.skin = "standar"
        self.theme = ""
        self.niveau = 0
        self.menue = None
        
        self.trace = []
        self.historique_departs = []
        
        self.creation = []
        
        self.page = 0
        self.nb_pages = 1
        self.tranche = []
        self.fichier_en_cours = None
        
        self.score = 0

        self.editeur = {
            "mode": None,
            "type_bloc": "normal",
            "orientation": "horizontale",
            "clics": [],
            "blocs": [],
            "objectif": None,
            "depart": None,
            "theme": None
        }
    
    def reset_editeur(self):
        self.editeur = {
            "mode": None,
            "type_bloc": "normal",
            "orientation": "horizontale",
            "clics": [],
            "blocs": [],
            "objectif": None,
            "depart": None,
            "theme": None
        }
