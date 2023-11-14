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

def clear_entries_f8():
    entry1_f8.delete(0, 'end')
    entry2_f8.delete(0, 'end')
    entry3_f8.delete(0, 'end')
    entry4_f8.delete(0, 'end')
    #entry5_f7.delete(0, 'end')
    #entry6_f2.delete(0, 'end')
    #entry7_f2.delete(0, 'end')
    #entry8_f2.delete(0, 'end')
    
    label_denied_f8.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f8.place_forget()
#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------

# Create a function to check the answers

def check_answers():
    answer1_f8 = entry1_f8.get().strip()
    answer2_f8 = entry2_f8.get().strip()
    answer3_f8 = entry3_f8.get().strip()
    #answer4_f8 = entry4_f8.get().strip()
    #answer5_f7 = entry5_f7.get().strip()
    #answer6_f2 = entry6_f2.get().strip()
    #answer7_f2 = entry7_f2.get().strip()
    #answer8_f2 = entry7_f2.get().strip()

    if (
        answer1_f8 == "1" and
        answer2_f8 == "1" and
        answer3_f8 == "1" 
        #answer4_f8 == "1" 
        #answer5_f7 == "1" 
        #answer6_f2 == "1" and
        #answer7_f2 == "1" and
        #answer8_f2 == "1" 
        
    ):
        label_acess_f8.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f8.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f8.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")sé
    else:
        label_denied_f8.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f8.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f8.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

# Create the main window    
fenetre8 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre8.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre8.resizable(width=False, height=False)


img = ImageTk.PhotoImage(Image.open("max27.png"))
img1 = ImageTk.PhotoImage(Image.open("74.png"))

center_window(fenetre8, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f8 = ImageTk.PhotoImage(Image.open("back_5.png"))

img_f8 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f8 = ImageTk.PhotoImage(Image.open("74.png"))

mon_label_img_f8=tkinter.Label(fenetre8, image=img, bg="#EAAC14")
mon_label_img1_f8=tkinter.Label(fenetre8, image=img1, bg="#EAAC14")
#mon_label_img.pack()
background_label_f8 = tkinter.Label(fenetre8, image=image_f8)
background_label_f8.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f8 = tkinter.Label(fenetre8, fg='white')
label_denied_f8 = tkinter.Label(fenetre8, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1_f8=tkinter.Label(fenetre8,text="")
reponse_entry1_f8.place(x=758, y=427)

reponse_entry2_f8=tkinter.Label(fenetre8,text="")
reponse_entry2_f8.place(x=498, y=521)

reponse_entry3_f8=tkinter.Label(fenetre8,text="")
reponse_entry3_f8.place(x=699, y=605)


reponse_entry4_f8=tkinter.Label(fenetre8,text="")
reponse_entry4_f8.place(x=695, y=680)


reponse_entry5_f8=tkinter.Label(fenetre8,text="")
reponse_entry5_f8.place(x=866, y=650)


reponse_entry6_f8=tkinter.Label(fenetre8,text="")
reponse_entry6_f8.place(x=866, y=650)


reponse_entry7_f8=tkinter.Label(fenetre8,text="")
reponse_entry7_f8.place(x=530, y=570)

reponse_entry8_f8=tkinter.Label(fenetre8,text="")
reponse_entry8_f8.place(x=600, y=620)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
question1_label_f8 = tkinter.Label(fenetre8, text="1- Quelle est la distance parcourue ce jour là ?:  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question1_label_f2 = tkinter.Label(fenetre6, text="1- Donne la dimension en longueur  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")#FDFBFB",justify="left")
question1_label_f8.place(x=0, y=0, relx=0.36, rely=0.60, anchor="center")

entry1_f8 = tkinter.Entry(reponse_entry1_f8, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry1_f8.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label_f8 = tkinter.Label(fenetre8, text="2- Quelle est Le nombre total de passagers \ntransportés ce jour là ? : ",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f8 = tkinter.Label(fenetre8, text="3- Quelle serait la distance, si nous avions \n le double de la distance actuelle parcourue ?   ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left" )
question4_label_f8 = tkinter.Label(fenetre8, text="4- Regardez les chiffres ci-dessus ! \nCombien d’élèves y a-t-il dans le cercle A ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385,
# rely=0.63, anchor="center")
question2_label_f8.place(x=0, y=0, relx=0.34, rely=0.70, anchor="center")
question3_label_f8.place(x=0, y=0, relx=0.353, rely=0.81, anchor="center")
#question4_label_f8.place(x=0, y=0, relx=0.335, rely=0.91, anchor="center")

entry2_f8 = tkinter.Entry(reponse_entry2_f8, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry2_f8.pack()



#question2b_label.pack()
entry3_f8 = tkinter.Entry(reponse_entry3_f8, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry3_f8.pack()

# Create question 3
question4_labe_f7 = tkinter.Label(fenetre8, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4_f8 = tkinter.Entry(reponse_entry4_f8, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry4_f8.pack()

#entry5_f7 = tkinter.Entry(reponse_entry5_f7, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry5_f7.pack()

#entry6_f2 = tkinter.Entry(reponse_entry6_f2, font=("Comic sans Ms", 18, ""), width=5,highlightthickness=1, highlightbackground="orange")
#entry6_f2.pack()

#entry7_f2 = tkinter.Entry(reponse_entry7_f2, font=("Comic sans Ms", 18, ""), width=29,highlightthickness=1, highlightbackground="orange")
#entry7_f2.pack()

#entry8_f2 = tkinter.Entry(reponse_entry8_f2, font=("Comic sans Ms", 18, ""), width=10,highlightthickness=1, highlightbackground="orange")
#entry8_f2.pack()

# Create a button to check the answers
check_button_f8 = customtkinter.CTkButton(fenetre8, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f8.place(x=1050, y=380)

# Create other widgets

label_text_f8 = tkinter.Label(fenetre8, text="Un chauffeur qui a un bus de 25 places a fait deux tours \n alert et retour sur la route de Mfou Yaoundé longue de 30 km", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#label_text2_f2 = tkinter.Label(fenetre2, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
btn_quitter_f8 = customtkinter.CTkButton(fenetre8, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre8.destroy)

# Position other widgets
label_text_f8.place(x=0, y=0, relx=0.41, rely=0.15, anchor="center")
#label_text2_f2.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")
btn_quitter_f8.place(x=1050, y=680)


#config
# Création du bouton Suivant
#bouton_suivant = customtkinter.CTkButton(fenetre1, text="Suivant", width=3, font=("Comic Sans Ms", 16), border_spacing=0, border_width=0)
# Création du bouton Précédent
def precedent():
    fenetre8.destroy()
    subprocess.run(['python', 'fenetre_8.py'])

bouton_precedent = customtkinter.CTkButton(fenetre8, text="Précédent", command=precedent, width=3, font=("Comic Sans Ms", 16))
bouton_precedent.pack(side=tkinter.LEFT)

def suivant():
    fenetre8.destroy()
    subprocess.run(['python', 'fenetre_10.py'])

bouton_suivant = customtkinter.CTkButton(fenetre8, text="Suivant", command=suivant, width=3, font=("Comic Sans Ms", 16))
bouton_suivant.pack(side=tkinter.RIGHT)

#bouton de reset

reset_img_f8=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f8=tkinter.Label(fenetre8, image=reset_img_f8)
 
# Create a button to clear the entries
clear_button_f8 = tkinter.Button(fenetre8, command=clear_entries_f8, image=reset_img_f8, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f8.place(x=1290, y=0)


# Use the lift() method to bring labels to the front

label_acess_f9.lift()
label_denied_f9.lift()
mon_label_img_f8.lift()
mon_label_img1_f9.lift()

label_text_f8.lift()
#label_text2_f2.lift()
btn_quitter_f9.lift()
check_button_f9.lift()
reponse_entry1_f9.lift()
reponse_entry2_f9.lift()
reponse_entry3_f9.lift()
reponse_entry4_f9.lift()
reponse_entry5_f9.lift()
reponse_entry6_f9.lift()
#reponse_entry7_f7.lift()
reponse_entry8_f9.lift()

fenetre8.mainloop()