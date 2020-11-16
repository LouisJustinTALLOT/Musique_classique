import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
os.chdir(os.path.pardir)

def trouver_nom_section(chaine):
    ch = chaine.split(" ")
    return " ".join(ch[1:])

regex_pattern =  "\A(\|[ a-zA-Z]{5}\w)"
ma_regex = re.compile(regex_pattern)

def identifier_ligne(ligne):
    """retourne :
    1 si une section             ## nom section
    2 si une sous section        ### nom sous-section
    3 si une sous sous section   #### nom sous-sous-section
    4 si c'est un morceau        |Le morceau 
    -1 sinon
    """
        
    if len(ligne) < 6:
        return -1

    if ma_regex.match(ligne) and ligne[:4] != "|Nom":
        return 4

    if ligne[:3] == "## ":
        return 1

    if ligne[:4] == "### ":
        return 2

    if ligne[:5] == "#### ":   
        return 3

    return -1

# for li in ["|Symphonie 3|   ", "|Nom de l'oeuvre", "## Symphonies", "### Piano", "#### Scherzos", "  "]:
#     print(identifier_ligne(li), li)

class SousSousSection :
    def __init__(self,nom_sous_sous_section, ligne_de_debut, ligne_de_fin, txt) : 
        self.nom = nom_sous_sous_section
        self.debut = ligne_de_debut
        self.fin = ligne_de_fin
        self.texte = txt

class SousSection :
    def __init__(self,nom_sous_section, ligne_de_debut, ligne_de_fin,txt) : 
        self.nom = nom_sous_section
        self.debut = ligne_de_debut
        self.fin = ligne_de_fin 
        self.texte = txt
        self.liste_sous_sous_sections = self.remplir_sous_sous_sections()

    def remplir_sous_sous_sections(self):
        return 

class Section :
    def __init__(self,nom_section, ligne_de_debut, ligne_de_fin,txt):
        self.nom = nom_section
        self.debut = ligne_de_debut
        self.fin = ligne_de_fin
        self.texte = txt
        self.liste_sous_sections = self.remplir_sous_sections()

    def remplir_sous_sections(self):
        return


    def __repr__(self):
        pass

class Document :

    def __init__(self, nom_doc):
        self.nom = nom_doc
        self.nom_fichier = self.nom = '.md'
        
        self.texte = []

        os.chdir("Compositeurs")

        with open(self.nom_fichier) as file:
            self.texte = file.readlines()
        
        self.longueur = len(self.texte)
        
        self.sections = self.remplir_sections()



    def remplir_sections(self):
        liste_sections = []

        for i in range(len(self.longueur)):
            "   "


        return liste_sections
        



