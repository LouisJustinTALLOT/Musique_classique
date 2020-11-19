import os 
import re
import structure_de_document as struct
from tkinter import *


dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path) # on est dans M_c/src/ 
os.chdir(os.path.pardir) # dans Musique_classique
os.chdir("Compositeurs")
