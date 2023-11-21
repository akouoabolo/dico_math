import tkinter 
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
import subprocess
import random
import num2words

window_width = 1350
window_height = 750

# Fonctions Utiles / centrer la fenêtre
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = int((screen_width - width) / 2)
    y_position = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x_position}+{y_position}") 

def convertir_en_lettres(nombre):
    nombre_en_lettres = num2words.num2words(nombre, lang='fr')
    return nombre_en_lettres
   # Votre code de vérification ici

def verifier_ordre():
    ordre = ordre_var.get()
    nombres_tries = sorted(nombres)
    if ordre == "décroissant":
        nombres_tries = sorted(nombres, reverse=True)
    #reponse_utilisateur_liste = list(map(int, reponse_utilisateur.get().split(",")))
    try:
        reponse_utilisateur_liste = list(map(int, reponse_utilisateur.get().split(",")))
    except ValueError:
        #resultat_label.config(text="Veuillez entrer des nombres valides.")
        #resultat_label.config(text="Dommage! Vous n'avez pas correctement classé les nombres. Recommencez s'il vous plaît.")
        label_denied_f2.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f2.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f2.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
     
    
    if reponse_utilisateur_liste == nombres_tries:
        
        label_acess_f2.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f2.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f2.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        
        #resultat_label.config(text="Bravo! Vous avez correctement classé les nombres.")
        nombres_en_lettres = []
        for nombre in nombres:
            nombre_en_lettres = convertir_en_lettres(nombre)
            nombres_en_lettres.append(nombre_en_lettres)
            nombres_en_lettres_label.config(text="Ces nombres en lettre sont :\n " + ", ".join(map(str, nombres_en_lettres)),font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
            nombres_en_lettres_label.place(x=258, y=600)
     
        #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")      
    else:
        #resultat_label.config(text="Dommage! Vous n'avez pas correctement classé les nombres. Recommencez s'il vous plaît.")
        label_denied_f2.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f2.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f2.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

def clear_entries_f2():
    # Réinitialisation des valeurs
    nombres.clear()
    for i in range(5):                 
        nombres.append(random.randint(1, 100))
    nombres_label.config(text="Voici 5 nouveaux nombres aléatoires : " + ", ".join(map(str, nombres)),font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
    ordre_var.set("")  # Réinitialisation de la variable d'ordre
    reponse_utilisateur.delete(0, END)  # Effacer le champ de réponse
    #reponse_utilisateur_lettres.delete(0, END)  # Effacer le champ de réponse en lettres
    
    nombres.clear()
    for i in range(5):
        nombres.append(random.randint(1, 100))
    nombres_label.config(text="Voici 5 nouveaux nombres aléatoires : " + ", ".join(map(str, nombres)))
    ordre_var.set("")  # Réinitialisation de la variable d'ordre
    reponse_utilisateur.delete(0, END)  # Effacer le champ de réponse
    #reponse_utilisateur_lettres.delete(0, END)  # Effacer le champ de réponse en lettres

    label_denied_f2.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f2.place_forget()
    
    label_acess_f2.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f2.place_forget()
 

# Les fonctions de conversion
def precedent():
    fenetre2.destroy()
    subprocess.run(['python', 'fenetre_2.py'])
    
def suivant():
    fenetre2.destroy()
    subprocess.run(['python', 'fenetre_4.py'])

fenetre2 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre2.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre2.resizable(width=False, height=False)

nombres = []
for i in range(5):
    nombres.append(random.randint(1, 100))
nombres_label =tkinter.Label(fenetre2, text="Voici 5 nombres aléatoires : " + ", ".join(map(str, nombres)),font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
nombres_label.place(x=0, y=0, relx=0.38, rely=0.13, anchor="center")

center_window(fenetre2, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f2 = ImageTk.PhotoImage(Image.open("font3.png"))


img_f2 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f2 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f2=tkinter.Label(fenetre2, image=img_f2, bg="#EAAC14")
mon_label_img1_f2=tkinter.Label(fenetre2, image=img1_f2, bg="#EAAC14")

background_label_f2 = tkinter.Label(fenetre2, image=image_f2)
background_label_f2.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f2 = tkinter.Label(fenetre2, fg='white')
label_denied_f2 = tkinter.Label(fenetre2, fg='#AA2822')

ordre_var = StringVar()
ordre_label = Label(fenetre2, text="Souhaitez-vous classer ces nombres par ordre \n\n croissant ou décroissant?",font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
ordre_label.place(x=0, y=0, relx=0.38, rely=0.52, anchor="center")
ordre_croissant_radio = Radiobutton(fenetre2, text="Croissant", variable=ordre_var, value="croissant",font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
ordre_croissant_radio.place(x=0, y=0, relx=0.48, rely=0.568, anchor="center")
ordre_decroissant_radio = Radiobutton(fenetre2, text="Décroissant", variable=ordre_var, value="décroissant",font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
ordre_decroissant_radio.place(x=0, y=0, relx=0.6, rely=0.568, anchor="center")

reponse_utilisateur_label = Label(fenetre2, text="Entrez les nombres séparés par des virgules :" ,font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
reponse_utilisateur_label.place(x=0, y=0, relx=0.38, rely=0.66, anchor="center")

reponse_utilisateur = Entry(fenetre2, font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left" ,highlightthickness=1, highlightbackground="orange")
reponse_utilisateur.place(x=0, y=0, relx=0.38, rely=0.75, anchor="center")

resultat_label = Label(fenetre2, text="")
resultat_label.pack()

nombres_en_lettres_label = Label(fenetre2, text="")
nombres_en_lettres_label.pack()


resultat_lettres_label = Label(fenetre2, text="")
resultat_lettres_label.pack()

resultat_final_label = Label(fenetre2, text="")
resultat_final_label.pack()

# Create a button to check the answers
check_button_f2 = customtkinter.CTkButton(fenetre2, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=verifier_ordre)
check_button_f2.place(x=1050, y=380)


# bouton suivant / précédent
bouton_precedent = customtkinter.CTkButton(fenetre2, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre2, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)
#bouton de reset

reset_img_f2=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f2=tkinter.Label(fenetre2, image=reset_img_f2)
 
# Create a button to clear the entries
clear_button_f2 = tkinter.Button(fenetre2, command=clear_entries_f2, image=reset_img_f2, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f2.place(x=1290, y=0)


# Move the label to the top
nombres_label.lift()
label_acess_f2.lift()
label_denied_f2.lift()
mon_label_img_f2.lift()
mon_label_img1_f2.lift()

check_button_f2.lift()

fenetre2.mainloop()