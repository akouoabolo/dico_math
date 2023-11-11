import tkinter as tk

# Création de la fenêtre principale
fenetre1 = tk.Tk()
fenetre1.title("Déplacement")
fenetre1.geometry("700x700")

# Création du label Bonjour
mon_label1 = tk.Label(fenetre1, text="Bonjour")
mon_label1.pack()

# Création du bouton Suivant
bouton_suivant = tk.Button(fenetre1, text="Suivant")

# Création de la fenêtre secondaire
fenetre2 = tk.Toplevel(fenetre1)
fenetre2.title("Déplacement")
fenetre2.geometry("700x700")

# Création du label Au revoir
mon_label2 = tk.Label(fenetre2, text="Au revoir")
mon_label2.pack()

# Création du bouton Précédent
bouton_precedent = tk.Button(fenetre2, text="Précédent")

# Fonction pour afficher la fenêtre secondaire et cacher la fenêtre principale
def afficher_fenetre2():
    fenetre1.withdraw() # Cacher la fenêtre principale
    fenetre2.deiconify() # Afficher la fenêtre secondaire

# Fonction pour afficher la fenêtre principale et cacher la fenêtre secondaire
def afficher_fenetre1():
    fenetre2.withdraw() # Cacher la fenêtre secondaire
    fenetre1.deiconify() # Afficher la fenêtre principale

# Association des fonctions aux boutons
bouton_suivant.config(command=afficher_fenetre2)
bouton_precedent.config(command=afficher_fenetre1)

# Placement des boutons
bouton_suivant.pack(side=tk.RIGHT)
bouton_precedent.pack(side=tk.LEFT)

# Cacher la fenêtre secondaire au début
fenetre2.withdraw()

# Lancement de la boucle principale
fenetre1.mainloop()

