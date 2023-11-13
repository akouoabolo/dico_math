import tkinter 
from tkinter import messagebox
import customtkinter

import subprocess
import random
from tkinter import *
from PIL import ImageTk, Image
import num2words

window_width = 1350
window_height = 750

# Fonctions Utiles
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = int((screen_width - width) / 2)
    y_position = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x_position}+{y_position}") 

def clear_entries_f2():
    # Réinitialiser les champs de saisie
    #km_entry.delete(0, tkinter.END)
    #hm_entry.delete(0, tkinter.END)
    #dam_entry.delete(0, tkinter.END)
    #m_entry.delete(0, tkinter.END)
    #dm_entry.delete(0, tkinter.END)
    #cm_entry.delete(0, tkinter.END)
    #mm_entry.delete(0, tkinter.END)
    
    label_denied_f2.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f2.place_forget()
#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------
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

fenetre3 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre3.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre3.resizable(width=False, height=False)




nombres = []
for i in range(5):
    nombres.append(random.randint(1, 100))
nombres_label = tkinter.Label(fenetre3, text="Voici 5 nombres aléatoires : " + ", ".join(map(str, nombres)), font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
nombres_label.place(x=220, y=80)

ordre_var = StringVar()
ordre_label = Label(fenetre3, text="Souhaitez-vous classer les nombres par ordre croissant ou décroissant?")
ordre_label.pack()
ordre_croissant_radio = Radiobutton(fenetre3, text="Croissant", variable=ordre_var, value="croissant")
ordre_croissant_radio.pack()
ordre_decroissant_radio = Radiobutton(fenetre3, text="Décroissant", variable=ordre_var, value="décroissant")
ordre_decroissant_radio.pack()

reponse_utilisateur_label = Label(fenetre3, text="Entrez les nombres séparés par des virgules :")
reponse_utilisateur_label.pack()
reponse_utilisateur = Entry(fenetre3)
reponse_utilisateur.pack()



valider_button = Button(fenetre3, text="Valider", command=verifier_ordre)
valider_button.pack()

resultat_label = Label(fenetre3, text="")
resultat_label.pack()

nombres_en_lettres_label = Label(fenetre3, text="")
nombres_en_lettres_label.pack()

reponse_utilisateur_lettres_label = Label(fenetre3, text="Entrez les nombres en lettres séparés par des virgules :")
reponse_utilisateur_lettres_label.pack()
reponse_utilisateur_lettres = Entry(fenetre3)
reponse_utilisateur_lettres.pack()

resultat_lettres_label = Label(fenetre3, text="")
resultat_lettres_label.pack()

resultat_final_label = Label(fenetre3, text="")
resultat_final_label.pack()


center_window(fenetre3, window_width, window_height) #position of windows2
# Create a Label widget and set the image as i
# ts background
image_f3 = ImageTk.PhotoImage(Image.open("font.png"))
img_tof_f3 = ImageTk.PhotoImage(Image.open("tof_f3.png"))
label_img_tof_f3 = tkinter.Label(fenetre3, image=img_tof_f3)    

img_f3 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f3 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f3=tkinter.Label(fenetre3, image=img_f3, bg="#EAAC14")
mon_label_img1_f3=tkinter.Label(fenetre3, image=img1_f3, bg="#EAAC14")
#mon_label_img.pack()

background_label_f3 = tkinter.Label(fenetre3, image=image_f3)  
background_label_f3.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f3 = tkinter.Label(fenetre3, fg='white')
label_denied_f3 = tkinter.Label(fenetre3, fg='#AA2822')


reponse_entry4_f3=tkinter.Label(fenetre3,text="")
reponse_entry4_f3.place(x=866, y=660)


# Create a button to check the answers
#check_button_f3 = customtkinter.CTkButton(fenetre3, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
#check_button_f3.place(x=1050, y=380)

# Create other widgets
label_text_f3 = tkinter.Label(fenetre3, text="Entre les bonnes valeurs de mesure dans les champs requis : \n ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#label_text2_f2 = tkinter.Label(fenetre2, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
btn_quitter_f3 = customtkinter.CTkButton(fenetre3, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre3.destroy)

# Position other widgets
#label_text_f2.place(x=0, y=0, relx=0.42, rely=0.15, anchor="center")
#label_text2_f2.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")
btn_quitter_f3.place(x=1050, y=680)


#config
# Création du bouton Suivant
#bouton_suivant = customtkinter.CTkButton(fenetre1, text="Suivant", width=3, font=("Comic Sans Ms", 16), border_spacing=0, border_width=0)
# Création du bouton Précédent
def precedent():
    fenetre3.destroy()
    subprocess.run(['python', 'test4.py'])

bouton_precedent = customtkinter.CTkButton(fenetre3, text="Précédent", command=precedent, width=3, font=("Comic Sans Ms", 16))

# Association des fonctions aux boutons
#bouton_suivant.configure(command=afficher_fenetre2)
#bouton_precedent.configure(command=afficher_fenetre1)       

# Placement des boutons
#bouton_suivant.pack(side=tkinter.RIGHT)
#bouton_precedent.grid(column=0, row=10)

#bouton de reset

reset_img_f3=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f3=tkinter.Label(fenetre3, image=reset_img_f3)
 
# Create a button to clear the entries
clear_button_f3 = tkinter.Button(fenetre3, command=clear_entries_f2, image=reset_img_f3, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f3.place(x=1290, y=0)




# Création du bouton de vérification
#check_button = tkinter.Button(fenetre2, text="Vérifier les réponses", command=check_answers)
#check_button.grid(column=1, row=7)

# Bouton pour réessayer
#retry_button = tkinter.Button(fenetre2, text="Réessayer", command=retry)
#retry_button.grid(column=1, row=8)

# Étiquette pour afficher le résultat
#result_label = tkinter.Label(fenetre2, text="", fg='black')
#result_label.grid(column=0, row=9, columnspan=2)
# Use the lift() method to bring labels to the front

label_acess_f3.lift()
label_denied_f3.lift()
mon_label_img_f3.lift()
mon_label_img1_f3.lift()

label_text_f3.lift()
nombres_label.lift()
#label_text2_f2.lift()
btn_quitter_f3.lift()
#check_button_f3.lift()
#reponse_entry2_f2.lift()
#reponse_entry3_f2.lift()
reponse_entry4_f3.lift()

fenetre3.mainloop()