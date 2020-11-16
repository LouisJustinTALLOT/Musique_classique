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

Ainsi si on obtient :

* une section :

  * on l'ajoute à la liste des sections

  * si ce n'est pas la première:

    * on update la précédente section avec la ligne de fin
  
    * et on fait `update()`

    * ce qui fait de même avec la précédente sous-section si elle existe

    * et aussi la précédente sous-sous-section si elle existe
    (on ne peut pas avoir de précédente sous-sous-section si on n'a pas de précédente sous-section)

* une sous-section :  

  * on l'ajoute à la liste des sous-sections de la section en cours

  * si ce n'est pas la première:

    * on update la précédente sous-section avec la ligne de fin
  
    * et on fait `update()`

    * ce qui fait de même avec la précédente sous-sous-section si elle existe

* une sous-section :

  * on l'ajoute à la liste des sous-sous-sections de la sous-section en cours

  * si ce n'est pas la première :

    * on update la précédente sous-sous-section avec la ligne de fin

    * et on fait `update()`

* une œuvre :

  * si on est dans une section :

    * si on est dans une sous-section :

      * si on est dans une sous-sous-section:

        * on la compte dans la sous-sous-section

      * sinon on la compte dans le corps de la sous-section

    * sinon on la compte dans le corps de la section

  * sinon on la compte en-dehors dans le corps du document

* rien de tout cela :

  * on ne fait rien

## `Classe.compter_morceaux()`

### `Document`

-> compte en dehors du document + fait la somme du compte sur les sections

### `Section`

-> fait la somme sur les sous-sections + en-dehors

### `SousSection`

-> fait la somme sur les sous-sous-sections + en-dehors

### `SousSousSection`

-> renvoie le nombre sur la sous-section
