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
    entry1_f5.delete(0, 'end')
    entry2_f5.delete(0, 'end')
    entry3_f5.delete(0, 'end')
    entry4_f5.delete(0, 'end')
    entry5_f5.delete(0, 'end')
    entry6_f5.delete(0, 'end')
    entry7_f5.delete(0, 'end')
    entry8_f5.delete(0, 'end')
    
    label_denied_f5.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f5.place_forget()
    label_acess_f5.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f5.place_forget()
#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------

# Create a function to check the answers
def check_answers():
    answer1_f5 = entry1_f5.get().strip()
    answer2_f5 = entry2_f5.get().strip()
    answer3_f5 = entry3_f5.get().strip()
    answer4_f5 = entry4_f5.get().strip()
    answer5_f5 = entry5_f5.get().strip()
    answer6_f5 = entry6_f5.get().strip()
    answer7_f5 = entry7_f5.get().strip()
    answer8_f5 = entry7_f5.get().strip()

    if (
        answer1_f5 == "1" and
        answer2_f5 == "1" and
        answer3_f5 == "1" and
        answer4_f5 == "1" and
        answer5_f5 == "1" and
        answer6_f5 == "1" and
        answer7_f5 == "1" and
        answer8_f5 == "1" 
        
    ):
        label_acess_f5.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f5.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f5.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")sé
    else:
        label_denied_f5.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f5.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f5.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

def precedent():
    fenetre5.destroy()
    subprocess.run(['python', 'fenetre_4CE1.py'])  
    
def suivant():
    fenetre5.destroy()
    subprocess.run(['python', 'fenetre_6CE1.py'])  
# Create the main window    
# Create the main window    


# Create the main window    
fenetre5 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre5.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre5.resizable(width=False, height=False)


img_f5 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f5 = ImageTk.PhotoImage(Image.open("74.png"))

center_window(fenetre5, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f5 = ImageTk.PhotoImage(Image.open("back_5.png"))

img_f5 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f5 = ImageTk.PhotoImage(Image.open("74.png"))

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
reponse_entry1_f5.place(x=348, y=434)

reponse_entry2_f5=tkinter.Label(fenetre5,text="")
reponse_entry2_f5.place(x=560, y=434)

reponse_entry3_f5=tkinter.Label(fenetre5,text="")
reponse_entry3_f5.place(x=793, y=434)


reponse_entry4_f5=tkinter.Label(fenetre5,text="")
reponse_entry4_f5.place(x=210, y=470)


reponse_entry5_f5=tkinter.Label(fenetre5,text="")
reponse_entry5_f5.place(x=460, y=470)


reponse_entry6_f5=tkinter.Label(fenetre5,text="")
reponse_entry6_f5.place(x=675, y=469)


reponse_entry7_f5=tkinter.Label(fenetre5,text="")
reponse_entry7_f5.place(x=530, y=570)

reponse_entry8_f5=tkinter.Label(fenetre5,text="")
reponse_entry8_f5.place(x=600, y=620)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
question1_label_f5 = tkinter.Label(fenetre5, text="1- Il a vendu [______] tenues + [______] tableaux + [______] perles + \n [______]  bracelets + _____ masques =  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")#FDFBFB",justify="left")
question1_label_f5.place(x=0, y=0, relx=0.45, rely=0.63, anchor="center")

entry1_f5 = tkinter.Entry(reponse_entry1_f5, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry1_f5.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label_f5 = tkinter.Label(fenetre5, text="2- Quel est le nombre total des masques ? \n Ecris ce nombre en lettre :",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f5 = tkinter.Label(fenetre5, text="3- Quel est l'objet le plus vendu ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left" )
question4_label_f5 = tkinter.Label(fenetre5, text="4- Combien d'animaux possède Monsieur Tamo au total ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385, rely=0.63, anchor="center")
question2_label_f5.place(x=0, y=0, relx=0.33, rely=0.76, anchor="center")
question3_label_f5.place(x=0, y=0, relx=0.296, rely=0.86, anchor="center")
#question4_label_f2.place(x=0, y=0, relx=0.405, rely=0.91, anchor="center")

entry2_f5 = tkinter.Entry(reponse_entry2_f5, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry2_f5.pack()



#question2b_label.pack()
entry3_f5 = tkinter.Entry(reponse_entry3_f5, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry3_f5.pack()

# Create question 3
question4_labe_f2l = tkinter.Label(fenetre5, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4_f5 = tkinter.Entry(reponse_entry4_f5, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry4_f5.pack()

entry5_f5 = tkinter.Entry(reponse_entry5_f5, font=("Comic sans Ms", 18, ""), width=5,highlightthickness=1, highlightbackground="orange")
entry5_f5.pack()

entry6_f5 = tkinter.Entry(reponse_entry6_f5, font=("Comic sans Ms", 18, ""), width=5,highlightthickness=1, highlightbackground="orange")
entry6_f5.pack()

entry7_f5 = tkinter.Entry(reponse_entry7_f5, font=("Comic sans Ms", 18, ""), width=29,highlightthickness=1, highlightbackground="orange")
entry7_f5.pack()

entry8_f5 = tkinter.Entry(reponse_entry8_f5, font=("Comic sans Ms", 18, ""), width=10,highlightthickness=1, highlightbackground="orange")
entry8_f5.pack()

# Create a button to check the answers
check_button_f5 = customtkinter.CTkButton(fenetre5, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f5.place(x=1050, y=380)

# Create other widgets
label_text_f5 = tkinter.Label(fenetre5, text="Quel est le nombres d'objets vendus en janvier ? \nPour trouver la réponse complète l'égalité : \n ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#label_text2_f2 = tkinter.Label(fenetre2, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


# Position other widgets
label_text_f5.place(x=0, y=0, relx=0.34, rely=0.15, anchor="center")
#label_text2_f2.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")


# Association des fonctions aux boutons
#bouton_suivant.configure(command=afficher_fenetre2)
#bouton_precedent.configure(command=afficher_fenetre1)       

# Placement des boutoF
#bouton_suivant.pack(side=tkinter.RIGHT)
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
#label_text2_f2.lift()

check_button_f5.lift()
reponse_entry1_f5.lift()
reponse_entry2_f5.lift()
reponse_entry3_f5.lift()
reponse_entry4_f5.lift()
reponse_entry5_f5.lift()
reponse_entry6_f5.lift()
reponse_entry7_f5.lift()
reponse_entry8_f5.lift()

fenetre5.mainloop()