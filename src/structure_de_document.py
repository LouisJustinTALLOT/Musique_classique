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


class Section :
    def __init__(self,document, nom_section, level,  ligne_de_debut, ligne_de_fin=-1):
        self.doc = document
        self.nom = nom_section

        self.debut = ligne_de_debut
        self.fin = ligne_de_fin

        self.niveau = level
        self.liste_sous_sections = [] 

        self.texte = []
        self.nombre_de_morceaux = 0

    def update(self):
        if self.fin >= self.debut:
            self.text = self.doc.texte[self.debut:self.fin]

        if self.liste_sous_sections:
            self.liste_sous_sections[-1].fin = self.fin
            self.liste_sous_sections[-1].update()

    def compter(self):
        res = 0
        for ss_sec in self.liste_sous_sections :
            res += ss_sec.compter()

        return self.nombre_de_morceaux + res


    def __repr__(self):
        
        return f"{self.niveau} {self.nom} [{[sec for sec in self.liste_sous_sections]}]"

class Document :

    def __init__(self, nom_doc):
        self.nom = nom_doc
        self.nom_fichier = self.nom = '.md'
        
        self.texte = []

        os.chdir("Compositeurs")

        with open(self.nom_fichier) as file:
            self.texte = file.readlines()
        
        self.longueur = len(self.texte)
        
        self.liste_sections = self.remplir_sections()



    def remplir_sections(self): # ATTENTION WIP
        section_en_cours =  None

        liste_sections = []

        for i in range(len(self.longueur)):

            ligne_etudiee = self.texte[i]
            type_ligne = identifier_ligne(ligne_etudiee)

            if type_ligne == 1 :  # c'est une nouvelle section 
                
                if liste_sections: # ce n'est pas la première

                    # il faut update la dernière section avec la ligne de fin
                    liste_sections[-1].fin = i
                    # on ajoute une nouvelle section sans mettre de texte pour l'instant 
                    liste_sections.append(Section(self,
                                                  trouver_nom_section(ligne_etudiee), 
                                                  i+1 ))
                    liste_sections[-1].update()

                else : # c'est la première section
                    liste_sections.append(Section(self,
                                                  trouver_nom_section(ligne_etudiee), 
                                                  1, 
                                                  i+1 ))
            elif type_ligne == 2 : # c'est une nouvelle sous-section

                pass

            elif type_ligne == 3 : # c'est une nouvelle sous-sous-section

                pass

            elif type_ligne == 4 : # c'est un morceau

                pass

        # on est à la fin du document, il faut alors update la toute dernière section

        if liste_sections : # la liste n'est pas vide
            liste_sections[-1].fin = self.longueur 
            liste_sections[-1].update()





        return liste_sections
        



