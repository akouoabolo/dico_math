import tkinter 
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
import subprocess
import random


window_width = 1350
window_height = 750

# Fonctions Utiles
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = int((screen_width - width) / 2)
    y_position = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x_position}+{y_position}") 


    #fenêtre2
def clear_entries_f2():
    entry1_f2.delete(0, 'end')
    entry2_f2.delete(0, 'end')
    entry3_f2.delete(0, 'end')
    entry4_f2.delete(0, 'end')
    
    label_denied_f2.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f2.place_forget()
    
    label_acess_f2.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f2.place_forget()
    
# Create a function to check the answers
def check_answers():
    answer1_f2 = entry1_f2.get().strip()
    answer2_f2 = entry2_f2.get().strip()
    answer3_f2 = entry3_f2.get().strip()
    answer4_f2 = entry4_f2.get().strip()
    

    if (
        answer1_f2 == "le rectangle"and
        answer2_f2 == "oui" and
        answer3_f2 == "trop haut" and
        answer4_f2 == "173"
    ):
        label_acess_f2.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f2.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f2.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")
    else:
        label_denied_f2.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f2.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f2.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")
def precedent():
    fenetre2.destroy()
    subprocess.run(['python', 'fenetre_1CE1.py'])  
    
def suivant():
    fenetre2.destroy()
    subprocess.run(['python', 'fenetre_3CE1.py'])  

# Create the main window    
fenetre2 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre2.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre2.resizable(width=False, height=False)

center_window(fenetre2, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f2 = ImageTk.PhotoImage(Image.open("pub13.png"))


img_f2 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f2 = ImageTk.PhotoImage(Image.open("74.png"))

mon_label_img_f2=tkinter.Label(fenetre2, image=img_f2, bg="#EAAC14")
mon_label_img1_f2=tkinter.Label(fenetre2, image=img1_f2, bg="#EAAC14")
#mon_label_img.pack()

background_label_f2 = tkinter.Label(fenetre2, image=image_f2)
background_label_f2.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f2 = tkinter.Label(fenetre2, fg='white')
label_denied_f2 = tkinter.Label(fenetre2, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1_f2=tkinter.Label(fenetre2,text="")
reponse_entry1_f2.place(x=770, y=455)

reponse_entry2_f2=tkinter.Label(fenetre2,text="")
reponse_entry2_f2.place(x=930, y=500)

reponse_entry3_f2=tkinter.Label(fenetre2,text="")
reponse_entry3_f2.place(x=660, y=615)


reponse_entry4_f2=tkinter.Label(fenetre2,text="")
reponse_entry4_f2.place(x=866, y=660)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
question1_label_f2 = tkinter.Label(fenetre2, text="1- Les abreuvoirs ont la forme de quels solide ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question1_label_f2.place(x=0, y=0, relx=0.37, rely=0.63, anchor="center")

entry1_f2 = tkinter.Entry(reponse_entry1_f2, font=("Comic sans Ms", 18, ""), width=10, highlightthickness=1, highlightbackground="orange")
entry1_f2.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label_f2 = tkinter.Label(fenetre2, text="2- Peut-on fabriquer des abreuvoirs sous frome cylindriques ?",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f2 = tkinter.Label(fenetre2, text="3- Supposons que les abreuvoirs fassent 2 mètres de haut,\n que se passera-t-il ? \n l'eau déborde - trop haut - trop bas", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question4_label_f2 = tkinter.Label(fenetre2, text="4- Combien d'animaux possède Monsieur Tamo au total ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385, rely=0.63, anchor="center")
question2_label_f2.place(x=0, y=0, relx=0.43, rely=0.69, anchor="center")
question3_label_f2.place(x=0, y=0, relx=0.416, rely=0.80, anchor="center")
question4_label_f2.place(x=0, y=0, relx=0.405, rely=0.91, anchor="center")

entry2_f2 = tkinter.Entry(reponse_entry2_f2, font=("Comic sans Ms", 18, ""), width=6, highlightthickness=1, highlightbackground="orange")
entry2_f2.pack()



#question2b_label.pack()
entry3_f2 = tkinter.Entry(reponse_entry3_f2, font=("Comic sans Ms", 18, ""), width=10, highlightthickness=1, highlightbackground="orange")
entry3_f2.pack()

# Create question 3
question4_labe_f2l = tkinter.Label(fenetre2, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4_f2 = tkinter.Entry(reponse_entry4_f2, font=("Comic sans Ms", 18, ""), width=10, highlightthickness=1, highlightbackground="orange")
entry4_f2.pack()

# Create a button to check the answers
check_button_f2 = customtkinter.CTkButton(fenetre2, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f2.place(x=1050, y=380)

# Create other widgets
label_text_f2 = tkinter.Label(fenetre2, text="Monsieur Tamo posséde dans sa ferme : \n ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
label_text2_f2 = tkinter.Label(fenetre2, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
#btn_quitter_f2 = customtkinter.CTkButton(fenetre2, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre2.destroy)

# Position other widgets
label_text_f2.place(x=0, y=0, relx=0.34, rely=0.15, anchor="center")
label_text2_f2.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")
#btn_quitter_f2.place(x=1050, y=680)


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


# Use the lift() method to bring labels to the front

label_acess_f2.lift()
label_denied_f2.lift()
mon_label_img_f2.lift()
mon_label_img1_f2.lift()

label_text_f2.lift()
label_text2_f2.lift()
check_button_f2.lift()
reponse_entry2_f2.lift()
reponse_entry3_f2.lift()
reponse_entry4_f2.lift()
# Add widgets to the main window
#btn_nouvel_info.pack(pady=20)
#message_info.pack(pady=10, fill="x", expand="True", padx="15")

# Main event loop
#------------------------------------------------------------------------------------------------------------------------------------------------

# Add widgets to the main window
#btn_nouvel_info.pack(pady=20)
#message_info.pack(pady=10, fill="x", expand="True", padx="15")

# Main event loop
fenetre2.mainloop()
