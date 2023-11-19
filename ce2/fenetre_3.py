import tkinter 
from tkinter import *
import customtkinter
from PIL import ImageTk, Image
import subprocess
import random
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
        label_denied_f3.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f3.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f3.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
     
    
    if reponse_utilisateur_liste == nombres_tries:
        
        label_acess_f3.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f3.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f3.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        
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
        label_denied_f3.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f3.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f3.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

def clear_entries_f3():
    # Réinitialisation des valeurs
    nombres.clear()
    for i in range(5):                 
        nombres.append(random.randint(1, 100))
    nombres_label.config(text="Voici 5 nouveaux nombres aléatoires : " + ", ".join(map(str, nombres)),font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
    ordre_var.set("")  # Réinitialisation de la variable d'ordre
    reponse_utilisateur.delete(0, END)  # Effacer le champ de réponse
    #reponse_utilisateur_lettres.delete(0, END)  # Effacer le champ de réponse en lettres
    resultat_label.config(text="")
    nombres_en_lettres_label.config(text="")
    resultat_lettres_label.config(text="")
    resultat_final_label.config(text="")
    
    nombres.clear()
    for i in range(5):
        nombres.append(random.randint(1, 100))
    nombres_label.config(text="Voici 5 nouveaux nombres aléatoires : " + ", ".join(map(str, nombres)))
    ordre_var.set("")  # Réinitialisation de la variable d'ordre
    reponse_utilisateur.delete(0, END)  # Effacer le champ de réponse
    #reponse_utilisateur_lettres.delete(0, END)  # Effacer le champ de réponse en lettres
    resultat_label.config(text="")
    nombres_en_lettres_label.config(text="")
    resultat_lettres_label.config(text="")
    resultat_final_label.config(text="")
    
    label_denied_f3.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f3.place_forget()
    
    label_acess_f3.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f3.place_forget()
 
# Create a function to check the answers
#def check_answers():
    #answer1_f2 = entry1_f2.get().strip()
    #answer2_f2 = entry2_f2.get().strip()
    #answer3_f2 = entry3_f2.get().strip()
    #answer4_f2 = entry4_f2.get().strip()
    

   # if (
        #answer1_f2 == "1" and
        #answer2_f2 == "1" and
        #answer3_f2 == "1" and
        #answer4_f2 == "1"
    #):
        #label_acess_f2.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        #label_acess_f2.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        #mon_label_img_f2.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")
   # else:
        #label_denied_f2.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        #label_denied_f2.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        #mon_label_img1_f2.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

# Create the main window    

# Les fonctions de conversion
def precedent():
    fenetre3.destroy()
    subprocess.run(['python', 'fenetre_2.py'])
    
def suivant():
    fenetre3.destroy()
    subprocess.run(['python', 'fenetre_4.py'])

fenetre3 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre3.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre3.resizable(width=False, height=False)

nombres = []
for i in range(5):
    nombres.append(random.randint(1, 100))
nombres_label =tkinter.Label(fenetre3, text="Voici 5 nombres aléatoires : " + ", ".join(map(str, nombres)),font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
nombres_label.place(x=0, y=0, relx=0.38, rely=0.13, anchor="center")
#img = ImageTk.PhotoImage(Image.open("max27.png"))
#img1 = ImageTk.PhotoImage(Image.open("74.png"))

center_window(fenetre3, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f3 = ImageTk.PhotoImage(Image.open("font3.png"))


img_f3 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f3 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f3=tkinter.Label(fenetre3, image=img_f3, bg="#EAAC14")
mon_label_img1_f3=tkinter.Label(fenetre3, image=img1_f3, bg="#EAAC14")
#mon_label_img.pack()

background_label_f3 = tkinter.Label(fenetre3, image=image_f3)
background_label_f3.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f3 = tkinter.Label(fenetre3, fg='white')
label_denied_f3 = tkinter.Label(fenetre3, fg='#AA2822')

ordre_var = StringVar()
ordre_label = Label(fenetre3, text="Souhaitez-vous classer ces nombres par ordre \n\n croissant ou décroissant?",font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
ordre_label.place(x=0, y=0, relx=0.38, rely=0.52, anchor="center")
ordre_croissant_radio = Radiobutton(fenetre3, text="Croissant", variable=ordre_var, value="croissant",font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
ordre_croissant_radio.place(x=0, y=0, relx=0.48, rely=0.568, anchor="center")
ordre_decroissant_radio = Radiobutton(fenetre3, text="Décroissant", variable=ordre_var, value="décroissant",font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
ordre_decroissant_radio.place(x=0, y=0, relx=0.6, rely=0.568, anchor="center")

reponse_utilisateur_label = Label(fenetre3, text="Entrez les nombres séparés par des virgules :" ,font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left")
reponse_utilisateur_label.place(x=0, y=0, relx=0.38, rely=0.66, anchor="center")

reponse_utilisateur = Entry(fenetre3, font=("Comic sans Ms", 18, "")  ,bg="#FDFBFB",justify="left" ,highlightthickness=1, highlightbackground="orange")
reponse_utilisateur.place(x=0, y=0, relx=0.38, rely=0.75, anchor="center")


#valider_button = Button(fenetre3, text="Valider", command=verifier_ordre)
#valider_button.pack()

#relancer_button = Button(fenetre3, text="Relancer le code", command=relancer_code)
#relancer_button.pack()

resultat_label = Label(fenetre3, text="")
resultat_label.pack()

nombres_en_lettres_label = Label(fenetre3, text="")
nombres_en_lettres_label.pack()

#reponse_utilisateur_lettres_label = Label(fenetre, text="Entrez les nombres en lettres séparés par des virgules :")
#reponse_utilisateur_lettres_label.pack()
#reponse_utilisateur_lettres = Entry(fenetre)
#reponse_utilisateur_lettres.pack()

resultat_lettres_label = Label(fenetre3, text="")
resultat_lettres_label.pack()

resultat_final_label = Label(fenetre3, text="")
resultat_final_label.pack()



# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
#question1_label_f2 = tkinter.Label(fenetre2, text="1- Les abreuvoirs ont la forme de quels solide ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question1_label_f2.place(x=0, y=0, relx=0.37, rely=0.63, anchor="center")

#entry1_f2 = tkinter.Entry(reponse_entry1_f2, font=("Comic sans Ms", 18, ""), width=10, highlightthickness=1, highlightbackground="orange")
#entry1_f2.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question2_label_f2 = tkinter.Label(fenetre2, text="2- Peut-on fabriquer des abreuvoirs sous frome cylindriques ?",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question3_label_f2 = tkinter.Label(fenetre2, text="3- Supposons que les abreuvoirs fassent 2 mètres de haut,\n que se passera-t-il ? \n l'eau déborde - trop haut - trop bas", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label_f2 = tkinter.Label(fenetre2, text="4- Combien d'animaux possède Monsieur Tamo au total ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385, rely=0.63, anchor="center")
#question2_label_f2.place(x=0, y=0, relx=0.43, rely=0.69, anchor="center")
#question3_label_f2.place(x=0, y=0, relx=0.416, rely=0.80, anchor="center")
#question4_label_f2.place(x=0, y=0, relx=0.405, rely=0.91, anchor="center")

#entry2_f2 = tkinter.Entry(reponse_entry2_f2, font=("Comic sans Ms", 18, ""), width=6)
#entry2_f2.pack()



#question2b_label.pack()
#entry3_f2 = tkinter.Entry(reponse_entry3_f2, font=("Comic sans Ms", 18, ""), width=10)
#entry3_f2.pack()

# Create question 3
#question4_labe_f2l = tkinter.Label(fenetre2, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

#entry4_f2 = tkinter.Entry(reponse_entry4_f2, font=("Comic sans Ms", 18, ""), width=10)
#entry4_f2.pack()


# Create a button to check the answers
check_button_f3 = customtkinter.CTkButton(fenetre3, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=verifier_ordre)
check_button_f3.place(x=1050, y=380)

# Create other widgets
#label_text_f3 = tkinter.Label(fenetre3, text="Entre les bonnes valeurs de mesure dans les champs requis : \n ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_quitter_f3 = customtkinter.CTkButton(fenetre3, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre3.destroy)

# Position other widgets
#label_text_f3.place(x=0, y=0, relx=0.42, rely=0.15, anchor="center")
#label_text2_f2.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")
#btn_quitter_f3.place(x=1050, y=680)


#config
# Création du bouton Suivant
#bouton_suivant = customtkinter.CTkButton(fenetre1, text="Suivant", width=3, font=("Comic Sans Ms", 16), border_spacing=0, border_width=0)
# Création du bouton Précédent





# bouton suivant / précédent
bouton_precedent = customtkinter.CTkButton(fenetre3, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre3, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)
#bouton de reset

reset_img_f3=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f3=tkinter.Label(fenetre3, image=reset_img_f3)
 
# Create a button to clear the entries
clear_button_f3 = tkinter.Button(fenetre3, command=clear_entries_f3, image=reset_img_f3, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f3.place(x=1290, y=0)



nombres_label.lift()
label_acess_f3.lift()
label_denied_f3.lift()
mon_label_img_f3.lift()
mon_label_img1_f3.lift()

#label_text_f3.lift()
#label_text2_f2.lift()
#btn_quitter_f3.lift()
check_button_f3.lift()
#reponse_entry2_f2.lift()
#reponse_entry3_f2.lift()
#reponse_entry4_f3.lift()

fenetre3.mainloop()