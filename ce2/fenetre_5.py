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

def clear_entries_f5():

    #entry5_f7.delete(0, 'end')
    #entry6_f2.delete(0, 'end')
    #entry7_f2.delete(0, 'end')
    #entry8_f2.delete(0, 'end')
    
    label_denied_f5.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f5.place_forget()
    label_acess_f5.place_forget()
    mon_label_img_f5.place_forget()
    
    proposition_entry.delete(0, tkinter.END)
#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------

# Create a function to check the answers

def check_answers():
    
    global niveau, propositions, proposition_entry, reponse_label, niveau_suivant_button
    proposition = proposition_entry.get()
    try:
        proposition = int(proposition)
        if proposition == propositions[niveau - 1][1]:
            #reponse_label.config(text="Bien joué, tu as trouvé !")
            niveau_suivant_button.config(state=tkinter.NORMAL)
        else:
            #reponse_label.config(text="T'as raté ! Réessayes encore.")
            niveau_suivant_button.config(state=tkinter.DISABLED)
    except ValueError:
        label_denied_f5.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f5.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f5.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        niveau_suivant_button.config(state=tkinter.DISABLED)
    #answer5_f7 = entry5_f7.get().strip()
    #answer6_f2 = entry6_f2.get().strip()
    #answer7_f2 = entry7_f2.get().strip()
    #answer8_f2 = entry7_f2.get().strip()
    proposition = int(proposition)
    if proposition == propositions[niveau - 1][1]:
        #answer5_f7 == "1" 
        #answer6_f2 == "1" and
        #answer7_f2 == "1" and
        #answer8_f2 == "1" 
        
    
        label_acess_f5.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f5.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f5.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        niveau_suivant_button.config(state=tkinter.NORMAL)
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")sé
    else:
        label_denied_f5.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f5.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f5.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        niveau_suivant_button.config(state=tkinter.DISABLED)
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")
#nouveau


def verifier_reponse():
    global niveau, propositions, proposition_entry, reponse_label, niveau_suivant_button
    proposition = proposition_entry.get()
    try:
        proposition = int(proposition)
        if proposition == propositions[niveau - 1][1]:
            reponse_label.config(text="Bien joué, tu as trouvé !")
            niveau_suivant_button.config(state=tkinter.NORMAL)
        else:
            reponse_label.config(text="T'as raté ! Réessayes encore.")
            niveau_suivant_button.config(state=tkinter.DISABLED)
    except ValueError:
        reponse_label.config(text="Veuillez entrer un nombre valide.")
        niveau_suivant_button.config(state=tkinter.DISABLED)

def passer_au_niveau_suivant():
    label_denied_f5.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f5.place_forget()
    label_acess_f5.place_forget()
    mon_label_img_f5.place_forget()
    global niveau, propositions, proposition_label, question_label, proposition_entry, verifier_button, reponse_label, niveau_suivant_button
    if niveau < len(propositions):
        niveau += 1
        question_label.config(text=f"Niveau {niveau}:")
        proposition_label.config(text=propositions[niveau - 1][0])
        proposition_entry.delete(0, tkinter.END)
        reponse_label.config(text="")
        niveau_suivant_button.config(state=tkinter.DISABLED)
        proposition_entry.focus_set()
        
    else:
        question_label.config(text="Félicitations ! Vous avez terminé le jeu.")
def precedent():
    fenetre5.destroy()
    subprocess.run(['python', 'fenetre_4.py'])
    
    
def suivant():
    fenetre5.destroy()
    subprocess.run(['python', 'fenetre_6.py'])
    

# Create the main window    
fenetre5 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre5.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre5.resizable(width=False, height=False)


#img = ImageTk.PhotoImage(Image.open("font.png"))
#mg1 = ImageTk.PhotoImage(Image.open("74.png"))

center_window(fenetre5, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f5 = ImageTk.PhotoImage(Image.open("font5.png"))

img_f5 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f5 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f5=tkinter.Label(fenetre5, image=img_f5, bg="#EAAC14")
mon_label_img1_f5=tkinter.Label(fenetre5, image=img1_f5, bg="#EAAC14")
#mon_label_img.pack()
background_label_f5 = tkinter.Label(fenetre5, image=image_f5)
background_label_f5.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f5 = tkinter.Label(fenetre5, fg='white')
label_denied_f5 = tkinter.Label(fenetre5, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1_f5=tkinter.Label(fenetre5,text="")
reponse_entry1_f5.place(x=450, y=429)

reponse_entry2_f5=tkinter.Label(fenetre5,text="")
reponse_entry2_f5.place(x=870, y=429)

reponse_entry3_f5=tkinter.Label(fenetre5,text="")
reponse_entry3_f5.place(x=470, y=510)


reponse_entry4_f5=tkinter.Label(fenetre5,text="")
reponse_entry4_f5.place(x=695, y=680)


reponse_entry5_f5=tkinter.Label(fenetre5,text="")
reponse_entry5_f5.place(x=866, y=650)


reponse_entry6_f5=tkinter.Label(fenetre5,text="")
reponse_entry6_f5.place(x=866, y=650)


reponse_entry7_f5=tkinter.Label(fenetre5,text="")
reponse_entry7_f5.place(x=530, y=570)

reponse_entry8_f5=tkinter.Label(fenetre5,text="")
reponse_entry8_f5.place(x=600, y=620)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
#question1_label_f8 = tkinter.Label(fenetre8, text="1- l'angle plat :  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question1_label_f2 = tkinter.Label(fenetre6, text="1- Donne la dimension en longueur  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")#FDFBFB",justify="left")
#question1_label_f8.place(x=0, y=0, relx=0.27, rely=0.60, anchor="center")

#entry1_f8 = tkinter.Entry(reponse_entry1_f8, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry1_f8.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label_f5 = tkinter.Label(fenetre5, text="2- L'angle droit : ",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f5 = tkinter.Label(fenetre5, text="3- L'angle obtus :", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left" )
question4_label_f5 = tkinter.Label(fenetre5, text="4- Langle aigu : ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385,
# rely=0.63, anchor="center")
#question2_label_f8.place(x=0, y=0, relx=0.274, rely=0.70, anchor="center")
#question3_label_f8.place(x=0, y=0, relx=0.567, rely=0.60, anchor="center")
#question4_label_f8.place(x=0, y=0, relx=0.561, rely=0.70, anchor="center")

#entry2_f8 = tkinter.Entry(reponse_entry2_f8, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry2_f8.pack()



#question2b_label.pack()
#entry3_f8 = tkinter.Entry(reponse_entry3_f8, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry3_f8.pack()

# Create question 3
question4_labe_f5 = tkinter.Label(fenetre5, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

#entry4_f8 = tkinter.Entry(reponse_entry4_f8, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry4_f8.pack()

#entry5_f7 = tkinter.Entry(reponse_entry5_f7, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry5_f7.pack()

#entry6_f2 = tkinter.Entry(reponse_entry6_f2, font=("Comic sans Ms", 18, ""), width=5,highlightthickness=1, highlightbackground="orange")
#entry6_f2.pack()

#entry7_f2 = tkinter.Entry(reponse_entry7_f2, font=("Comic sans Ms", 18, ""), width=29,highlightthickness=1, highlightbackground="orange")
#entry7_f2.pack()

#entry8_f2 = tkinter.Entry(reponse_entry8_f2, font=("Comic sans Ms", 18, ""), width=10,highlightthickness=1, highlightbackground="orange")
#entry8_f2.pack()

# Create a button to check the answers
check_button_f5 = customtkinter.CTkButton(fenetre5, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f5.place(x=1050, y=380)

# Create other widgets

label_text_f5 = tkinter.Label(fenetre5, text="Trouve le chiffre manquant dans la suite de nombres ! ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

niveau = 1

propositions = [  
              
    ("250, 240, 230, ..., 210", 220),
    ("550, 560, 570, ..., 590", 580),
    ("4980, 4990, 5000, ..., 5020", 5010)
]

question_label = tkinter.Label(fenetre5, text=f"Niveau: {niveau}",font=("Comic sans Ms", 18, "bold"),bg="#FDFBFB",justify="left")
question_label.place(x=0, y=0, relx=0.685, rely=0.43, anchor="center")

proposition_label = tkinter.Label(fenetre5, text=propositions[niveau - 1][0], font=("Comic sans Ms", 18, "bold"),bg="#FDFBFB",justify="left")
proposition_label.place(x=0, y=0, relx=0.484, rely=0.46, anchor="center")

proposition_entry = tkinter.Entry(fenetre5, font=("Comic sans Ms", 18, ""), width=5,highlightthickness=1, highlightbackground="orange")
proposition_entry.place(x=0, y=0, relx=0.399, rely=0.58, anchor="center")
proposition_entry.focus_set()

#verifier_button = tkinter.Button(fenetre8, text="Vérifier", command=verifier_reponse)
#verifier_button.place(x=0, y=0, relx=0.685, rely=0.43, anchor="center")

niveau_suivant_button = tkinter.Button(fenetre5, text="Niveau suivant",  command=passer_au_niveau_suivant, font=("Comic sans Ms", 15),bg="#3BABE4",fg="white",justify="left", borderwidth=4,relief="ridge", cursor="hand2")
niveau_suivant_button.place(x=0, y=0, relx=0.685, rely=0.51, anchor="center")

reponse_label = tkinter.Label(fenetre5, text="")
reponse_label.pack()

# Position other widgets
label_text_f5.place(x=0, y=0, relx=0.43, rely=0.15, anchor="center")


# bouton suivant / précédent
bouton_precedent = customtkinter.CTkButton(fenetre5, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre5, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)
#bouton de reset


reset_img_f5=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f5=tkinter.Label(fenetre5, image=reset_img_f5)
 
# Create a button to clear the entries
clear_button_f5 = tkinter.Button(fenetre5, command=clear_entries_f5, image=reset_img_f5, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f5.place(x=1290, y=0)


# Use the lift() method to bring labels to the front

label_acess_f5.lift()
label_denied_f5.lift()
mon_label_img_f5.lift()
mon_label_img1_f5.lift()

label_text_f5.lift()
check_button_f5.lift()
reponse_entry1_f5.lift()
reponse_entry2_f5.lift()
reponse_entry3_f5.lift()
reponse_entry4_f5.lift()
reponse_entry5_f5.lift()
reponse_entry6_f5.lift()
#reponse_entry7_f7.lift()
reponse_entry8_f5.lift()

fenetre5.mainloop()