import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
os.chdir(os.path.pardir)

entiers_1_6 = [1, 2, 3, 4, 5, 6]

def sum_liste_chaine(li,sep=""):
    res = ""
    for c in li[:-1]:
        res += c + sep
    res += li[-1]
    return res

def trouver_nom_section(chaine):
    ch = chaine.split(" ")
    return " ".join(ch[1:])

regex_pattern =  r"\A(\|[ a-zA-Z]{5}\w)"
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
        return -2

    for i in range(1,7):
        if ligne[:i+1] == "#"*i + " ":
            return i

    return -1

class Section :
    def __init__(self,document, nom_section, level,  ligne_de_debut, ligne_de_fin=-1, par = None):
        self.doc = document
        self.nom = nom_section

        self.debut = ligne_de_debut
        self.fin = ligne_de_fin

        self.niveau = level
        self.liste_sous_sections = []

        self.texte = []
        self.nombre_de_morceaux = 0

        self.parent = par

    def update(self):
        if self.fin >= self.debut:
            self.texte = self.doc.texte[self.debut:self.fin]

        if self.liste_sous_sections:
            self.liste_sous_sections[-1].fin = self.fin
            self.liste_sous_sections[-1].update()

    def compter(self):
        res = 0
        for ss_sec in self.liste_sous_sections :
            res += ss_sec.compter()

        return self.nombre_de_morceaux + res

    def __repr__(self):
        if self.liste_sous_sections :
          return f"{self.niveau} {self.nom} {[sec for sec in self.liste_sous_sections]}"
        else:
            return f"{self.niveau} {self.nom}"

class Document :

    def __init__(self, nom_doc):
        self.nom = nom_doc
        self.nom_fichier = self.nom + '.md'

        self.texte = []

        os.chdir(dir_path)
        os.chdir(os.path.pardir)
        os.chdir("Compositeurs")

        with open(self.nom_fichier, 'r', encoding = 'utf8') as file:
            self.texte = file.readlines()

        self.longueur = len(self.texte)

        self.nombre_total_de_morceaux = 0

        self.liste_sections = self.remplir_sections()

        self.nombre_total_de_morceaux = self.tout_compter()

    
    def remplacer(self, numero_ligne, ligne):
        texte = ""
        for no in range(self.longueur):
            if no == numero_ligne:
                texte += ligne + "\n"
            else:
                texte += self.texte[no]

        os.chdir(dir_path)
        os.chdir(os.path.pardir)
        os.chdir("Compositeurs")
        with open(self.nom_fichier, 'w', encoding = 'utf8') as file:
            file.write(texte)

    def tout_compter(self):
        res = self.nombre_total_de_morceaux

        for sec in self.liste_sections :
            res += sec.compter()

        return res 

    def remplir_sections(self):

        liste_sections = []

        for i in range(self.longueur):

            ligne_etudiee = self.texte[i]
            type_ligne = identifier_ligne(ligne_etudiee)

            if type_ligne in entiers_1_6 :

                new = Section(self, trouver_nom_section(ligne_etudiee), type_ligne, i+1 )

                if not liste_sections: # c'est la toute première section
                    liste_sections.append(new)

                else : # on doit update la section précédente
                    liste_sections[-1].fin = i
                    liste_sections[-1].update()
                    liste_sections.append(new)

            elif type_ligne == -2 : # c'est un morceau

                if liste_sections :
                   liste_sections[-1].nombre_de_morceaux += 1
                else :
                    self.nombre_total_de_morceaux += 1

        # on est à la fin du document, il faut alors update la toute dernière section

        if liste_sections : # la liste n'est pas vide
            liste_sections[-1].fin = self.longueur
            liste_sections[-1].update()

        return liste_sections

    def trouver_et_decommenter(self, chaine):
        for i in range(self.longueur):
            if chaine in self.texte[i] and self.texte[i][:4] == "<!--":
                ch = chaine.split()
                if "-->" in ch[-1]:
                    rempl = sum_liste_chaine(ch[1:-1], " ")
                else:
                    rempl = sum_liste_chaine(ch[1:]," ")

                self.remplacer(i,rempl)
                return True
        return False

def enleve_espaces_debut_fin(chaine):

    while chaine[0] == " ":
        chaine = chaine[1:]

    while chaine[-1] == " ":
        chaine = chaine[:-1]

    return chaine

def new_file(prenom_compositeur, nom_compositeur):
    prenom_compositeur = enleve_espaces_debut_fin(prenom_compositeur)
    nom_compositeur = enleve_espaces_debut_fin(nom_compositeur)

    texte = ""
    texte += f"""# {prenom_compositeur} {nom_compositeur} - œuvres\n"""

    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    os.chdir(os.path.pardir)
    os.chdir("Compositeurs")

    nom_du_fichier = nom_compositeur + ".md"

    if nom_du_fichier not in os.listdir():
        with open(nom_du_fichier,'w', encoding='utf8') as fi:
            fi.write(texte)
    
def insert(section):
    """|Nom de l'œuvre| Op., n° | Lien | Commentaire | Note|
    |--------------|---------|------|-------------|-----|
    |              |         | [Interprète](youtube)|   |  ★|"""
    pass


# print(new_file("Jean","    Pierre   "))
new_file("Jean","    Pierre   ")
d = Document("Pierre")
d.remplacer(5,"dhiaudaih")
d.trouver_et_decommenter("Instrument")