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

def clear_entries_f14():
    entry1_f14.delete(0, 'end')
    entry2_f14.delete(0, 'end')
    entry3_f14.delete(0, 'end')
    entry4_f14.delete(0, 'end')
    #entry5_f7.delete(0, 'end')
    #entry6_f2.delete(0, 'end')
    #entry7_f2.delete(0, 'end')
    #entry8_f2.delete(0, 'end')
    
    label_denied_f14.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f14.place_forget()

    label_acess_f14.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f14.place_forget()
#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------

# Create a function to check the answers

def check_answers():
    answer1_f14 = entry1_f14.get().strip()
    answer2_f14 = entry2_f14.get().strip()
    answer3_f14 = entry3_f14.get().strip()
    answer4_f14 = entry4_f14.get().strip()
    #answer5_f7 = entry5_f7.get().strip()
    #answer6_f2 = entry6_f2.get().strip()
    #answer7_f2 = entry7_f2.get().strip()
    #answer8_f2 = entry7_f2.get().strip()

    if (
        answer1_f14 == "1" and
        answer2_f14 == "1" and
        answer3_f14 == "1" and
        answer4_f14 == "1" 
        #answer5_f7 == "1" 
        #answer6_f2 == "1" and
        #answer7_f2 == "1" and
        #answer8_f2 == "1" 
        
    ):
        label_acess_f14.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f14.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f14.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")sé
    else:
        label_denied_f14.config(text='Oops! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f14.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f14.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

def precedent():
    fenetre14.destroy()
    subprocess.run(['python', 'fenetre_13CE1.py'])  
    
def suivant():
    fenetre14.destroy()
    subprocess.run(['python', 'fenetre_15CE1.py'])  


# Create the main window    
fenetre14 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre14.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre14.resizable(width=False, height=False)


img = ImageTk.PhotoImage(Image.open("max27.png"))
img1 = ImageTk.PhotoImage(Image.open("74.png"))

center_window(fenetre14, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f14 = ImageTk.PhotoImage(Image.open("font14.png"))

img_f14 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f14 = ImageTk.PhotoImage(Image.open("74.png"))

mon_label_img_f14=tkinter.Label(fenetre14, image=img, bg="#EAAC14")
mon_label_img1_f14=tkinter.Label(fenetre14, image=img1, bg="#EAAC14")
#mon_label_img.pack()
background_label_f14 = tkinter.Label(fenetre14, image=image_f14)
background_label_f14.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f14 = tkinter.Label(fenetre14, fg='white')
label_denied_f14 = tkinter.Label(fenetre14, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1_f14=tkinter.Label(fenetre14,text="")
reponse_entry1_f14.place(x=500, y=410)

reponse_entry2_f14=tkinter.Label(fenetre14,text="")
reponse_entry2_f14.place(x=505, y=535)

reponse_entry3_f14=tkinter.Label(fenetre14,text="")
reponse_entry3_f14.place(x=685, y=585)


reponse_entry4_f14=tkinter.Label(fenetre14,text="")
reponse_entry4_f14.place(x=910, y=675)


reponse_entry5_f14=tkinter.Label(fenetre14,text="")
reponse_entry5_f14.place(x=866, y=650)


reponse_entry6_f14=tkinter.Label(fenetre14,text="")
reponse_entry6_f14.place(x=866, y=650)


reponse_entry7_f14=tkinter.Label(fenetre14,text="")
reponse_entry7_f14.place(x=530, y=570)

reponse_entry8_f14=tkinter.Label(fenetre14,text="")
reponse_entry8_f14.place(x=600, y=620)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
question1_label_f14 = tkinter.Label(fenetre14, text="1- Le chauffeur du bus fait 5 tours. Combien de passagers \ndoit-il transporter ?:  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question1_label_f2 = tkinter.Label(fenetre6, text="1- Donne la dimension en longueur  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")#FDFBFB",justify="left")
question1_label_f14.place(x=0, y=0, relx=0.435, rely=0.55, anchor="center")

entry1_f14 = tkinter.Entry(reponse_entry1_f14, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry1_f14.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label_f14 = tkinter.Label(fenetre14, text="2- En observant les deux cadrans d'horloge indiquant les horaires \nd'ouverture et de fermeture du site, quelle est \nl'heure d'ouverture ? ",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f14 = tkinter.Label(fenetre14, text="3- Quelle est l'heure de fermeture ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left" )
question4_label_f14 = tkinter.Label(fenetre14, text="4- Le guide a apporté 56 bouteilles d'eau a partager avec 4 groupes \nd'enfants. Combien de bouteilles chaque groupe aura-t-il ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385,
# rely=0.63, anchor="center")
question2_label_f14.place(x=0, y=0, relx=0.467, rely=0.69, anchor="center")
question3_label_f14.place(x=0, y=0, relx=0.345, rely=0.80, anchor="center")
question4_label_f14.place(x=0, y=0, relx=0.475, rely=0.90, anchor="center")

entry2_f14 = tkinter.Entry(reponse_entry2_f14, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry2_f14.pack()



#question2b_label.pack()
entry3_f14 = tkinter.Entry(reponse_entry3_f14, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry3_f14.pack()

# Create question 3
question4_labe_f7 = tkinter.Label(fenetre14, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4_f14 = tkinter.Entry(reponse_entry4_f14, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry4_f14.pack()

#entry5_f7 = tkinter.Entry(reponse_entry5_f7, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry5_f7.pack()

#entry6_f2 = tkinter.Entry(reponse_entry6_f2, font=("Comic sans Ms", 18, ""), width=5,highlightthickness=1, highlightbackground="orange")
#entry6_f2.pack()

#entry7_f2 = tkinter.Entry(reponse_entry7_f2, font=("Comic sans Ms", 18, ""), width=29,highlightthickness=1, highlightbackground="orange")
#entry7_f2.pack()

#entry8_f2 = tkinter.Entry(reponse_entry8_f2, font=("Comic sans Ms", 18, ""), width=10,highlightthickness=1, highlightbackground="orange")
#entry8_f2.pack()

# Create a button to check the answers
check_button_f14 = customtkinter.CTkButton(fenetre14, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f14.place(x=1050, y=380)

# Create other widgets

label_text_f14 = tkinter.Label(fenetre14, text="Lisez le texte, regardez l'image, puis répondez aux questions.", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#label_text2_f2 = tkinter.Label(fenetre2, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
btn_quitter_f14 = customtkinter.CTkButton(fenetre14, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre14.destroy)

# Position other widgets
label_text_f14.place(x=0, y=0, relx=0.446, rely=0.15, anchor="center")
#label_text2_f2.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")
#btn_quitter_f13.place(x=1050, y=680)


#config
# Création du bouton Suivant
# Création du bouton Précédent
bouton_precedent = customtkinter.CTkButton(fenetre14, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre14, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)

#bouton de reset

reset_img_f14=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f14=tkinter.Label(fenetre14, image=reset_img_f14)
 
# Create a button to clear the entries
clear_button_f14 = tkinter.Button(fenetre14, command=clear_entries_f14, image=reset_img_f14, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f14.place(x=1290, y=0)


# Use the lift() method to bring labels to the front

label_acess_f14.lift()
label_denied_f14.lift()
mon_label_img_f14.lift()
mon_label_img1_f14.lift()

label_text_f14.lift()
#label_text2_f2.lift()
#btn_quitter_f13.lift()
check_button_f14.lift()
reponse_entry1_f14.lift()
reponse_entry2_f14.lift()
reponse_entry3_f14.lift()
reponse_entry4_f14.lift()
reponse_entry5_f14.lift()
reponse_entry6_f14.lift()
#reponse_entry7_f7.lift()
reponse_entry8_f14.lift()

fenetre14.mainloop()