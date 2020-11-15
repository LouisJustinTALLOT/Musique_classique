# -*- coding: utf-8 -*-

import os


os.chdir("Compositeurs")

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
