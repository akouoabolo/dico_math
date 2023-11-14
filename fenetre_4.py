import tkinter 
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
import subprocess

window_width = 1350
window_height = 750

# Fonctions Utiles
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = int((screen_width - width) / 2)
    y_position = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x_position}+{y_position}") 

#-----------------------------------------QUATRIEME FENETRE-----------------------------------------------------------------

# Fonction pour afficher la fenêtre secondaire et cacher la fenêtre principale

# Create a function to check the answers
def check_answers():
    answer1_0f4 = entry1_0f4.get().strip()
    answer1_1f4 = entry1_1f4.get().strip()
    answer1_2f4 = entry1_2f4.get().strip()
    
    answer2_f4 = entry2_f4.get().strip()
    answer3_f4 = entry3_f4.get().strip()
    answer4_f4= entry4_f4.get().strip()
    

    if (
        answer1_0f4 == "1" and
        answer1_1f4 == "1" and
        answer1_2f4 == "1" and
          
        answer2_f4 == "1" and
        answer3_f4 == "1" and
        answer4_f4 == "1"
    ):
        label_acess_f4.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f4.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f4.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")
    else:
        label_denied_f4.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f4.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f4.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

# Create the main window    
fenetre4 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre4.title("dico_mathématique")
#fenetre4.geometry("1350x750")
fenetre4.resizable(width=False, height=False)

img = ImageTk.PhotoImage(Image.open("max27.png"))
img1 = ImageTk.PhotoImage(Image.open("74.png"))

center_window(fenetre4, window_width, window_height) #position of windows4
# Create a Label widget and set the image as its background
image_f4 = ImageTk.PhotoImage(Image.open("back_4.png"))

img_f4 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f4 = ImageTk.PhotoImage(Image.open("74.png"))

mon_label_img_f4=tkinter.Label(fenetre4, image=img, bg="#EAAC14")
mon_label_img1_f4=tkinter.Label(fenetre4, image=img1, bg="#EAAC14")
#mon_label_img.pack()

background_label_f4 = tkinter.Label(fenetre4, image=image_f4)
background_label_f4.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f4 = tkinter.Label(fenetre4, fg='white')
label_denied_f4 = tkinter.Label(fenetre4, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1_0f4=tkinter.Label(fenetre4,text="")
reponse_entry1_0f4.place(x=170, y=355)
reponse_entry1_1f4=tkinter.Label(fenetre4,text="")
reponse_entry1_1f4.place(x=425, y=407)
reponse_entry1_2f4=tkinter.Label(fenetre4,text="")
reponse_entry1_2f4.place(x=779, y=338)


reponse_entry2_f4=tkinter.Label(fenetre4,text="")
reponse_entry2_f4.place(x=930, y=500)

reponse_entry3_f4=tkinter.Label(fenetre4,text="")
reponse_entry3_f4.place(x=660, y=615)


reponse_entry4_f4=tkinter.Label(fenetre4,text="")
reponse_entry4_f4.place(x=866, y=660)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
question1_label_f4 = tkinter.Label(fenetre4, text="1- Donne la forme géométrique de chaque parcelle \n dans les champs de saisie", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question1_label_f4.place(x=0, y=0, relx=0.38, rely=0.69, anchor="center")

entry1_0f4 = tkinter.Entry(reponse_entry1_0f4, font=("Comic sans Ms", 18, ""), width=10)
entry1_0f4.pack()
entry1_1f4 = tkinter.Entry(reponse_entry1_1f4, font=("Comic sans Ms", 18, ""), width=10)
entry1_1f4.pack()
entry1_2f4 = tkinter.Entry(reponse_entry1_2f4, font=("Comic sans Ms", 18, ""), width=10)
entry1_2f4.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label_f4 = tkinter.Label(fenetre4, text="2- Quelle culture produit le plus de produits en regardant \n cette image ? ",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f4 = tkinter.Label(fenetre4, text="3- Supposons que les abreuvoirs fassent 2 mètres de haut,\n que se passera-t-il ? \n l'eau déborde - trop haut - trop bas", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question4_label_f4 = tkinter.Label(fenetre4, text="4- Combien d'animaux possède Monsieur Tamo au total ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385, rely=0.63, anchor="center")
question2_label_f4.place(x=0, y=0, relx=0.3, rely=0.79, anchor="center")
#question3_label_f4.place(x=0, y=0, relx=0.416, rely=0.80, anchor="center")
#question4_label_f4.place(x=0, y=0, relx=0.405, rely=0.91, anchor="center")

entry2_f4 = tkinter.Entry(reponse_entry2_f4, font=("Comic sans Ms", 18, ""), width=6)
#entry2_f4.pack()



#question2b_label.pack()
entry3_f4 = tkinter.Entry(reponse_entry3_f4, font=("Comic sans Ms", 18, ""), width=10)
#entry3_f4.pack()
# Create question 3
question4_label_f4 = tkinter.Label(fenetre4, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4_f4 = tkinter.Entry(reponse_entry4_f4, font=("Comic sans Ms", 18, ""), width=10)
#entry4_f4.pack()
 
# Create a button to check the answers
check_button_f4 = customtkinter.CTkButton(fenetre4, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f4.place(x=1050, y=380)

# Create other widgets
label_text_f4 = tkinter.Label(fenetre4, text="Monsieur Mbarga souhaite déterminer les formes géométriques \n des parcelles de son terrain : \n ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#label_text2_f4 = tkinter.Label(fenetre4, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
btn_quitter_f4 = customtkinter.CTkButton(fenetre4, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre4.destroy)

# Position other widgets
label_text_f4.place(x=0, y=0, relx=0.43, rely=0.15, anchor="center")
#label_text2_f4.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")
btn_quitter_f4.place(x=1050, y=680)


#config
# Création du bouton Suivant
bouton_suivant = customtkinter.CTkButton(fenetre4, text="Suivant", width=3, font=("Comic Sans Ms", 16), border_spacing=0, border_width=0)
# Création du bouton Précédent
bouton_precedent = customtkinter.CTkButton(fenetre4, text="Précédent", width=3, font=("Comic Sans Ms", 16))

def precedent():
    fenetre4.destroy()
    subprocess.run(['python', 'fenetre_3.py'])

def suivant():
    fenetre4.destroy()
    subprocess.run(['python', 'fenetre_5.py'])

# Association des fonctions aux boutons
bouton_suivant.configure(command=suivant)
bouton_precedent.configure(command=precedent)       

# Placement des boutons
bouton_suivant.pack(side=tkinter.RIGHT)
bouton_precedent.pack(side=tkinter.LEFT)

#bouton de reset

reset_img_f4=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f4=tkinter.Label(fenetre4, image=reset_img_f4)
 
# Create a button to clear the entries
clear_button_f4 = tkinter.Button(fenetre4, command=clear_entries_f4, image=reset_img_f4, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f4.place(x=1290, y=0)


# Use the lift() method to bring labels to the front


label_acess_f4.lift()
label_denied_f4.lift()
mon_label_img_f4.lift()
mon_label_img1_f4.lift()

label_text_f4.lift()
#label_text2_f4.lift()
btn_quitter_f4.lift()
check_button_f4.lift()
reponse_entry2_f4.lift()
reponse_entry3_f4.lift()
reponse_entry4_f4.lift()

fenetre4.mainloop()