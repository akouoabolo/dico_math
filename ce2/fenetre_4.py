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

def clear_entries_f4():
    
    label_denied_f4.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f4.place_forget()
    label_acess_f4.place_forget()
    mon_label_img_f4.place_forget()
    
    proposition_entry.delete(0, tkinter.END)


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
        label_denied_f4.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f4.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f4.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        niveau_suivant_button.config(state=tkinter.DISABLED)


    proposition = int(proposition)
    if proposition == propositions[niveau - 1][1]:
  
        label_acess_f4.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f4.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f4.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        niveau_suivant_button.config(state=tkinter.NORMAL)
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")sé
    else:
        label_denied_f4.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f4.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f4.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
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
    label_denied_f4.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f4.place_forget()
    label_acess_f4.place_forget()
    mon_label_img_f4.place_forget()
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
    fenetre4.destroy()
    subprocess.run(['python', 'fenetre_4.py'])
    
    
def suivant():
    fenetre4.destroy()
    subprocess.run(['python', 'fenetre_6.py'])
    

# Create the main window    
fenetre4 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre4.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre4.resizable(width=False, height=False)


center_window(fenetre4, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f4 = ImageTk.PhotoImage(Image.open("font5.png"))

img_f4 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f4 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f4=tkinter.Label(fenetre4, image=img_f4, bg="#EAAC14")
mon_label_img1_f4=tkinter.Label(fenetre4, image=img1_f4, bg="#EAAC14")
#mon_label_img.pack()
background_label_f4 = tkinter.Label(fenetre4, image=image_f4)
background_label_f4.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f4 = tkinter.Label(fenetre4, fg='white')
label_denied_f4 = tkinter.Label(fenetre4, fg='#AA2822')

#positionement des entry
reponse_entry1_f4=tkinter.Label(fenetre4,text="")
reponse_entry1_f4.place(x=450, y=429)

reponse_entry2_f4=tkinter.Label(fenetre4,text="")
reponse_entry2_f4.place(x=870, y=429)

reponse_entry3_f4=tkinter.Label(fenetre4,text="")
reponse_entry3_f4.place(x=470, y=510)


reponse_entry4_f4=tkinter.Label(fenetre4,text="")
reponse_entry4_f4.place(x=695, y=680)


reponse_entry5_f4=tkinter.Label(fenetre4,text="")
reponse_entry5_f4.place(x=866, y=650)


reponse_entry6_f4=tkinter.Label(fenetre4,text="")
reponse_entry6_f4.place(x=866, y=650)


reponse_entry7_f4=tkinter.Label(fenetre4,text="")
reponse_entry7_f4.place(x=530, y=570)

reponse_entry8_f4=tkinter.Label(fenetre4,text="")
reponse_entry8_f4.place(x=600, y=620)

# Create a label with the problem statement
question2_label_f4 = tkinter.Label(fenetre4, text="2- L'angle droit : ",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f4 = tkinter.Label(fenetre4, text="3- L'angle obtus :", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left" )
question4_label_f4 = tkinter.Label(fenetre4, text="4- Langle aigu : ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

# Create question 3
question4_labe_f4 = tkinter.Label(fenetre4, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


# Create a button to check the answers
check_button_f4 = customtkinter.CTkButton(fenetre4, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f4.place(x=1050, y=380)

# Create other widgets

label_text_f4 = tkinter.Label(fenetre4, text="Trouve le chiffre manquant dans la suite de nombres ! ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

niveau = 1

propositions = [  
              
    ("250, 240, 230, ..., 210", 220),
    ("550, 560, 570, ..., 590", 580),
    ("4980, 4990, 5000, ..., 5020", 5010)
]

question_label = tkinter.Label(fenetre4, text=f"Niveau: {niveau}",font=("Comic sans Ms", 18, "bold"),bg="#FDFBFB",justify="left")
question_label.place(x=0, y=0, relx=0.685, rely=0.43, anchor="center")

proposition_label = tkinter.Label(fenetre4, text=propositions[niveau - 1][0], font=("Comic sans Ms", 18, "bold"),bg="#FDFBFB",justify="left")
proposition_label.place(x=0, y=0, relx=0.484, rely=0.46, anchor="center")

proposition_entry = tkinter.Entry(fenetre4, font=("Comic sans Ms", 18, ""), width=5,highlightthickness=1, highlightbackground="orange")
proposition_entry.place(x=0, y=0, relx=0.399, rely=0.58, anchor="center")
proposition_entry.focus_set()

niveau_suivant_button = tkinter.Button(fenetre4, text="Niveau suivant",  command=passer_au_niveau_suivant, font=("Comic sans Ms", 15),bg="#3BABE4",fg="white",justify="left", borderwidth=4,relief="ridge", cursor="hand2")
niveau_suivant_button.place(x=0, y=0, relx=0.685, rely=0.51, anchor="center")

reponse_label = tkinter.Label(fenetre4, text="")
reponse_label.pack()

# Position other widgets
label_text_f4.place(x=0, y=0, relx=0.43, rely=0.15, anchor="center")


# bouton suivant / précédent
bouton_precedent = customtkinter.CTkButton(fenetre4, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre4, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)
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
check_button_f4.lift()
reponse_entry1_f4.lift()
reponse_entry2_f4.lift()
reponse_entry3_f4.lift()
reponse_entry4_f4.lift()
reponse_entry5_f4.lift()
reponse_entry6_f4.lift()

reponse_entry8_f4.lift()

fenetre4.mainloop()