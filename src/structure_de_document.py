import os

dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
os.chdir(dir_path)
os.chdir(os.path.pardir)
# print(os.getcwd())

    ch = chaine.split(" ")
class SousSousSection :
    def __init__(self,nom_section, txt) : 
        self.nom = nom_section
        self.texte = txt

class SousSection :
    def __init__(self,nom_sous_section,txt) : 
        self.nom = nom_section
        self.texte = txt

class Section :
    def __init__(self,nom_section) : #, ligne_de_debut, ligne_de_fin):
        self.nom = nom_section
        # self.debut = ligne_de_debut
        # self.fin = ligne_de_fin
        self.texte = []
        self.liste_sous_sections = []

    def __repr__():
        pass



class Document :

    def __init__(self, nom_doc):
        self.nom = nom_doc
        self.nom_fichier = self.nom = '.md'
        
        self.texte = []

        os.chrdir("c:/Users/ljtal/Documents/Musique_classique/Compositeurs")

        with open(self.nom_fichier) as file:
            self.texte = file.readlines()
        
        self.sections = self.remplir_sections()
    
    def remplir_sections(self):
        liste_sections = []




        return liste_sections
        



