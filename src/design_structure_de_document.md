# Module `structure_de_document` - démarche de construction
  
## `Document.remplir_sections()`  

Cette fonction a pour but d'initialiser l'objet `Document` en remplissant
son attribut `liste_sections` avec différents objets `Section`.

Pour cela, on parcourt le document *i.e* le tableau `self.text` et on regarde
à chaque fois le type de ligne. 

Attention, on peut avoir dans le document :

* une section après une sous-sous-section

* une section après une sous-section

* une section après une section

* une section après rien

mais toujours dans le document ;

ou bien :

* une sous-section après une sous-sous-section

* une sous-section après une autre sous-section

* une sous-section après une section

mais toujours compris dans une section ;

et encore :

* une sous-sous-section après une autre sous-sous-section

* une sous-sous-section après une sous-section.

mais toujours compris dans une sous-section.

