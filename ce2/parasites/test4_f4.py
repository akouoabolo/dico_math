import random
import num2words
from tkinter import *

def convertir_en_lettres(nombre):
    nombre_en_lettres = num2words.num2words(nombre, lang='fr')
    return nombre_en_lettres

def verifier_ordre():
    ordre = ordre_var.get()
    nombres_tries = sorted(nombres)
    if ordre == "décroissant":
        nombres_tries = sorted(nombres, reverse=True)
    reponse_utilisateur_liste = list(map(int, reponse_utilisateur.get().split(",")))
    if reponse_utilisateur_liste == nombres_tries:
        resultat_label.config(text="Bravo! Vous avez correctement classé les nombres.")
        nombres_en_lettres = []
        for nombre in nombres:
            nombre_en_lettres = convertir_en_lettres(nombre)
            nombres_en_lettres.append(nombre_en_lettres)
        nombres_en_lettres_label.config(text="Les nombres en chiffres sont : " + ", ".join(map(str, nombres_en_lettres)))
        reponse_utilisateur_lettres_liste = reponse_utilisateur_lettres.get().split(",")
        if all(nombre in nombres_en_lettres for nombre in reponse_utilisateur_lettres_liste):
            resultat_lettres_label.config(text="Bravo! Vous avez correctement classé les nombres en lettres.")
            resultat_final_label.config(text="Bravo! Vous avez terminé l'exercice.")
        else:
            resultat_lettres_label.config(text="Dommage! Vous n'avez pas correctement classé les nombres en lettres. Recommencez s'il vous plaît.")
    else:
        resultat_label.config(text="Dommage! Vous n'avez pas correctement classé les nombres. Recommencez s'il vous plaît.")

fenetre = Tk()
fenetre.title("Classement des nombres")
fenetre.geometry("400x400")

nombres = []
for i in range(5):
    nombres.append(random.randint(1, 100))
nombres_label = Label(fenetre, text="Voici 5 nombres aléatoires : " + ", ".join(map(str, nombres)))
nombres_label.pack()

ordre_var = StringVar()
ordre_label = Label(fenetre, text="Souhaitez-vous classer les nombres par ordre croissant ou décroissant?")
ordre_label.pack()
ordre_croissant_radio = Radiobutton(fenetre, text="Croissant", variable=ordre_var, value="croissant")
ordre_croissant_radio.pack()
ordre_decroissant_radio = Radiobutton(fenetre, text="Décroissant", variable=ordre_var, value="décroissant")
ordre_decroissant_radio.pack()

reponse_utilisateur_label = Label(fenetre, text="Entrez les nombres séparés par des virgules :")
reponse_utilisateur_label.pack()
reponse_utilisateur = Entry(fenetre)
reponse_utilisateur.pack()

valider_button = Button(fenetre, text="Valider", command=verifier_ordre)
valider_button.pack()

resultat_label = Label(fenetre, text="")
resultat_label.pack()

nombres_en_lettres_label = Label(fenetre, text="")
nombres_en_lettres_label.pack()

reponse_utilisateur_lettres_label = Label(fenetre, text="Entrez les nombres en lettres séparés par des virgules :")
reponse_utilisateur_lettres_label.pack()
reponse_utilisateur_lettres = Entry(fenetre)
reponse_utilisateur_lettres.pack()

resultat_lettres_label = Label(fenetre, text="")
resultat_lettres_label.pack()

resultat_final_label = Label(fenetre, text="")
resultat_final_label.pack()

fenetre.mainloop()
