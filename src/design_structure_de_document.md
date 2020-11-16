# Module `structure_de_document` - démarche de construction
  
## `Document.remplir_sections(self)`  

Cette fonction a pour but d'initialiser l'objet `Document` en remplissant
son attribut `liste_sections` avec différents objets `Section`.

Pour cela, on parcourt le document *i.e* le tableau `self.text` et on regarde
à chaque fois le type de ligne. 

