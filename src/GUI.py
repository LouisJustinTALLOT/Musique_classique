import os 
import re
import structure_de_document as struct
import tkinter as tk


dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path) # on est dans M_c/src/ 
os.chdir(os.path.pardir) # dans Musique_classique
os.chdir("Compositeurs")

compositeurs = os.listdir()
for i in range(len(compositeurs)):
    compositeurs[i] = compositeurs[i][:-3]
compositeurs.sort()

dict_docs = {}
for c in compositeurs:
    dict_docs[c] = struct.Document(c)

def nouveau_compositeur(en_prenom, en_nom):
    # on va lire template.md, le copier en changeant le premier nom
    # il faut aussi prévoir une zone de texte
    prenom = en_prenom.get()
    nom = en_nom.get()
    en_nom.delete(0, 'end') 
    en_prenom.delete(0, 'end')
    
    struct.new_file(prenom, nom)
def afficher_doc(doc):
    for widget in fen.winfo_children():
        widget.destroy()
    liste_compo_deroulante(compositeurs)
    tk.Label(fen, text = "").grid(row = 1, column = 4)
    # print(doc.nom)
    # le nom en haut avec le nb de morceaux
    # Label(fen, text = doc.nom).grid(row = 0, column = 3)
    tk.Label(fen, text = doc.nombre_total_de_morceaux).grid(row = 1, column = 5)
    # les parties
    for i in range(1,len(doc.liste_sections)+1):
        # un label avec le nom de la section et le nombre d'oeuvres
        tk.Label(fen, text = doc.liste_sections[i-1].nom).grid(row = i, column = 2)
        if doc.liste_sections[i-1].compter():
            tk.Label(fen, text = doc.liste_sections[i-1].compter()).grid(row = i, column = 5)
    tk.Label(fen, text = "").grid(row = i+1, column = 3)

    tk.Label(fen, text = "Prénom : ").grid(row = i+2, column = 1)
    tk.Label(fen, text = " Nom : ").grid(row = i+2, column = 3)

    entree_prenom = tk.Entry(fen) ; entree_prenom.grid(row = i+2, column = 2)
    entree_nom = tk.Entry(fen) ; entree_nom.grid(row = i+2, column = 4)
    tk.Button(fen, 
              text = "Nouveau compositeur", 
              command = lambda : nouveau_compositeur(entree_prenom, 
                                                    entree_nom)).grid(row = i+2, 
                                                                    column = 5)


    tk.Button(fen, text="Quit", command=fen.destroy).grid(row = i+4, column = 3)

def callback_list(*args):
    global var_listbox1
    afficher_doc(dict_docs[var_listbox1.get()])

def liste_compo_deroulante(compo):
    global var_listbox1
    var_listbox1 = tk.StringVar(fen)
    var_listbox1.set("Compositeur")
    opt = tk.OptionMenu(fen, var_listbox1, *compo)
    var_listbox1.trace("w", callback_list)
    opt.grid(row = 3, column = 0)
    
# la partie principale

fen = tk.Tk()
# fen.geometry('500x200')
# lb = Listbox(fen)
# lb.insert(1, compositeurs)
# lb.grid()

liste_compo_deroulante(compositeurs)
tk.Label(fen, text = "Prénom : ").grid(row = 5, column = 1)
tk.Label(fen, text = " Nom : ").grid(row = 5, column = 3)

entree_prenom = tk.Entry(fen) ; entree_prenom.grid(row = 5, column = 2)
entree_nom = tk.Entry(fen) ; entree_nom.grid(row = 5, column = 4)
tk.Button(fen, 
          text = "Nouveau compositeur", 
          command = lambda : nouveau_compositeur(entree_prenom, 
                                                 entree_nom)).grid(row = 5, 
                                                                   column = 5)

tk.Button(fen, text="Quit", command=fen.destroy).grid(row = 10, column = 3)
# print(fen.winfo_children())
fen.mainloop()
