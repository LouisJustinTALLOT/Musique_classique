# -*- coding: utf-8 -*-

import os
import re

regex_pattern =  "\A(\|[a-zA-Z]+\w)"
ma_regex = re.compile(regex_pattern)


def compter_nombre_de_morceaux(nom_de_fichier):
    fiche_compositeur = []

    with open(f"{nom_de_fichier}", 'r', encoding = 'utf8') as file : 
        fiche_compositeur = list(file)

    fiche_compositeur = set([ligne[:-1] for ligne in fiche_compositeur])
    fiche_compositeur.remove("")

    nombre_de_morceaux = 0    

    for ligne in fiche_compositeur:
        if ma_regex.match(ligne) and ligne[:4] != "|Nom":
            nombre_de_morceaux += 1


    for i in fiche_compositeur:
        print(repr(i))

    print(nombre_de_morceaux)
    

os.chdir("Compositeurs")

compter_nombre_de_morceaux("Vivaldi.md")
input()

fichiers = set(os.listdir())

# fichiers.remove(".git")
# fichiers.remove("README.py")
# fichiers.remove("README.md")
# fichiers.remove("template.md")

liste_fichiers = []

for i in fichiers : 
    liste_fichiers.append(i[:-3])
    
liste_fichiers.sort()














texte = f"""# Musique classique

{len(liste_fichiers)} compositeurs sont répertoriés dans cette base.

|Nom du compositeur |
|-------------------|"""

for comp in liste_fichiers : 
    texte += f"""\n|[{comp}](https://github.com/LouisJustinTALLOT/Musique_classique/blob/master/Compositeurs/{comp}.md)|"""
texte += "\n"

os.chdir(os.path.pardir)

with open('README.md','w', encoding='utf8') as file :
    
    file.write(texte)
