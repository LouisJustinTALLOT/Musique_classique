# -*- coding: utf-8 -*-

import os

fichiers = set(os.listdir())

fichiers.remove(".git")
fichiers.remove("README.py")
fichiers.remove("template.md")

liste_fichiers = set()

for i in fichiers : 
    print(i)
    liste_fichiers.add(i[:-3])
    

print(fichiers)
print(liste_fichiers)
liste_fichiers = list(liste_fichiers)
liste_fichiers.sort()
print(liste_fichiers)


texte = f"""# Musique classique

{len(liste_fichiers)} compositeurs sont répertoriés dans cette base.
"""

with open('README.md','w', encoding='utf8') as file :
    
    file.write(texte)
