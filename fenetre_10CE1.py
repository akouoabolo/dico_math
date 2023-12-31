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

def clear_entries_f10():
    entry1_f10.delete(0, 'end')
    entry2_f10.delete(0, 'end')
    entry3_f10.delete(0, 'end')
  
    #entry5_f7.delete(0, 'end')
    #entry6_f2.delete(0, 'end')
    #entry7_f2.delete(0, 'end')
    #entry8_f2.delete(0, 'end')
    
    label_denied_f10.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f10.place_forget()
    
    label_acess_f10.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f10.place_forget() 
#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------

# Create a function to check the answers

def check_answers():
    answer1_f10 = entry1_f10.get().strip()
    answer2_f10 = entry2_f10.get().strip()
    answer3_f10 = entry3_f10.get().strip()
    #answer4_f8 = entry4_f8.get().strip()
    #answer5_f7 = entry5_f7.get().strip()
    #answer6_f2 = entry6_f2.get().strip()
    #answer7_f2 = entry7_f2.get().strip()
    #answer8_f2 = entry7_f2.get().strip()

    if (
        answer1_f10 == "(1,5)" and
        answer2_f10 == "(2,4)" and
        answer3_f10 == "(3,2)" 
        #answer4_f8 == "1" 
        #answer5_f7 == "1" 
        #answer6_f2 == "1" and
        #answer7_f2 == "1" and
        #answer8_f2 == "1" 
        
    ):
        label_acess_f10.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f10.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f10.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")sé
    else:
        label_denied_f10.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f10.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f10.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")


def precedent():
    fenetre10.destroy()
    subprocess.run(['python', 'fenetre_9CE1.py'])  
    
def suivant():
    fenetre10.destroy()
    subprocess.run(['python', 'fenetre_11CE1.py'])  

# Create the main window    
fenetre10 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre10.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre10.resizable(width=False, height=False)


img_f10 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f10 = ImageTk.PhotoImage(Image.open("74.png"))

center_window(fenetre10, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f10 = ImageTk.PhotoImage(Image.open("font10.png"))

#img_f12 = ImageTk.PhotoImage(Image.open("max27.png"))
#img1_f12 = ImageTk.PhotoImage(Image.open("74.png"))

mon_label_img_f10=tkinter.Label(fenetre10, image=img_f10, bg="#EAAC14")
mon_label_img1_f10=tkinter.Label(fenetre10, image=img1_f10, bg="#EAAC14")
#mon_label_img.pack()
background_label_f10 = tkinter.Label(fenetre10, image=image_f10)
background_label_f10.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f10 = tkinter.Label(fenetre10, fg='white')
label_denied_f10 = tkinter.Label(fenetre10, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1_f10=tkinter.Label(fenetre10,text="")
reponse_entry1_f10.place(x=558, y=185)

reponse_entry2_f10=tkinter.Label(fenetre10,text="")
reponse_entry2_f10.place(x=600, y=230)

reponse_entry3_f10=tkinter.Label(fenetre10,text="")
reponse_entry3_f10.place(x=650, y=330)


reponse_entry4_f10=tkinter.Label(fenetre10,text="")
reponse_entry4_f10.place(x=695, y=680)


reponse_entry5_f10=tkinter.Label(fenetre10,text="")
reponse_entry5_f10.place(x=866, y=650)


reponse_entry6_f10=tkinter.Label(fenetre10,text="")
reponse_entry6_f10.place(x=866, y=650)


reponse_entry7_f10=tkinter.Label(fenetre10,text="")
reponse_entry7_f10.place(x=530, y=570)
reponse_entry8_f10=tkinter.Label(fenetre10,text="")
reponse_entry8_f10.place(x=600, y=620)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
question1_label_f10 = tkinter.Label(fenetre10, text="1- Donnez les coordonnées géométriques des points\n A, B et C sur le schéma : ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question1_label_f2 = tkinter.Label(fenetre6, text="1- Donne la dimension en longueur  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")#FDFBFB",justify="left")
question1_label_f10.place(x=0, y=0, relx=0.417, rely=0.75, anchor="center")

entry1_f10 = tkinter.Entry(reponse_entry1_f10, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry1_f10.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label_f10 = tkinter.Label(fenetre10, text="2- Quelle est Le nombre total de passagers \ntransportés ce jour là ? : ",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f10 = tkinter.Label(fenetre10, text="3- Quelle serait la distance, si nous avions \n le double de la distance actuelle parcourue ?   ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left" )
question4_label_f10 = tkinter.Label(fenetre10, text="4- Regardez les chiffres ci-dessus ! \nCombien d’élèves y a-t-il dans le cercle A ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385,
# rely=0.63, anchor="center")
#question2_label_f12.place(x=0, y=0, relx=0.34, rely=0.70, anchor="center")
#question3_label_f12.place(x=0, y=0, relx=0.353, rely=0.81, anchor="center")
#question4_label_f8.place(x=0, y=0, relx=0.335, rely=0.91, anchor="center")

entry2_f10 = tkinter.Entry(reponse_entry2_f10, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry2_f10.pack()



#question2b_label.pack()
entry3_f10 = tkinter.Entry(reponse_entry3_f10, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry3_f10.pack()

# Create question 3
question4_labe_f10 = tkinter.Label(fenetre10, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

"""entry4_f8 = tkinter.Entry(reponse_entry4_f8, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry4_f8.pack()"""

#entry5_f7 = tkinter.Entry(reponse_entry5_f7, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry5_f7.pack()



# Create a button to check the answers
check_button_f10 = customtkinter.CTkButton(fenetre10, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f10.place(x=1050, y=380)

# Create other widgets

label_text_f10 = tkinter.Label(fenetre10, text="Observez le graphe ci-dessous et répondez à la question \nsuivante :", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#label_text2_f2 = tkinter.Label(fenetre2, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


# Position other widgets
label_text_f10.place(x=0, y=0, relx=0.40, rely=0.14, anchor="center")
#label_text2_f2.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")



#config
# Création du bouton Suivant
#bouton_suivant = customtkinter.CTkButton(fenetre1, text="Suivant", width=3, font=("Comic Sans Ms", 16), border_spacing=0, border_width=0)
# Création du bouton Précédent
bouton_precedent = customtkinter.CTkButton(fenetre10, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre10, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)
#bouton de reset

reset_img_f10=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f10=tkinter.Label(fenetre10, image=reset_img_f10)
 
# Create a button to clear the entries
clear_button_f10 = tkinter.Button(fenetre10, command=clear_entries_f10, image=reset_img_f10, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f10.place(x=1290, y=0)


# Use the lift() method to bring labels to the front

label_acess_f10.lift()
label_denied_f10.lift()
mon_label_img_f10.lift()
mon_label_img1_f10.lift()

label_text_f10.lift()
#label_text2_f2.lift()

check_button_f10.lift()
reponse_entry1_f10.lift()
reponse_entry2_f10.lift()
reponse_entry3_f10.lift()
reponse_entry4_f10.lift()
reponse_entry5_f10.lift()


fenetre10.mainloop()