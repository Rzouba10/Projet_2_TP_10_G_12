class EtatJeu:
    def __init__(self):
        
        self.menu = "PRINCIPAL"
        self.skin = "standar"
        self.theme = ""
        self.niveau = 0
        self.menue = None
        
        self.trace = []
        
        self.creation = []
        
        self.page = 0
        self.nb_pages = 1
        self.tranche = []

        self.editeur = {
            "mode": None,
            "type_bloc": "normal",
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
            "clics": [],
            "blocs": [],
            "objectif": None,
            "depart": None,
            "theme": None
        }