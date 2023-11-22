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

def clear_entries_f7():
    entry1_f7.delete(0, 'end')
    entry2_f7.delete(0, 'end')
    entry3_f7.delete(0, 'end')
    entry4_f7.delete(0, 'end')
    #entry5_f2.delete(0, 'end')
    #entry6_f2.delete(0, 'end')
    #entry7_f2.delete(0, 'end')
    #entry8_f2.delete(0, 'end')
    
    label_denied_f7.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f7.place_forget()
    
    label_acess_f7.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f7.place_forget()
#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------

# Create a function to check the answers

def check_answers():
    answer1_f7 = entry1_f7.get().strip()
    answer2_f7 = entry2_f7.get().strip()
    answer3_f7 = entry3_f7.get().strip()
    answer4_f7 = entry4_f7.get().strip()
    #answer5_f7 = entry5_f7.get().strip()
    #answer6_f2 = entry6_f2.get().strip()
    #answer7_f2 = entry7_f2.get().strip()
    #answer8_f2 = entry7_f2.get().strip()

    if (
        
        answer1_f7 == "123,156,345,349" and
        answer2_f7 == "729" and
        answer3_f7 == "530" and
        answer4_f7 == "509" 
        #answer6_f2 == "1" and
        #answer7_f2 == "1" and
        #answer8_f2 == "1" 
        
    ):
        label_acess_f7.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f7.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f7.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")sé
    else:
        label_denied_f7.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f7.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f7.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")


def precedent():
    fenetre7.destroy()
    subprocess.run(['python', 'fenetre_6CE1.py'])  
    
def suivant():
    fenetre7.destroy()
    subprocess.run(['python', 'fenetre_8CE1.py'])  
# Create the main window    
# Create the main window

# Create the main window    
fenetre7 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre7.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre7.resizable(width=False, height=False)


img_f7 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f7 = ImageTk.PhotoImage(Image.open("74.png"))

center_window(fenetre7, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f7 = ImageTk.PhotoImage(Image.open("font7.png"))

img_f7 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f7 = ImageTk.PhotoImage(Image.open("74.png"))

mon_label_img_f7=tkinter.Label(fenetre7, image=img_f7, bg="#EAAC14")
mon_label_img1_f7=tkinter.Label(fenetre7, image=img1_f7, bg="#EAAC14")
#mon_label_img.pack()
background_label_f7 = tkinter.Label(fenetre7, image=image_f7)
background_label_f7.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f7 = tkinter.Label(fenetre7, fg='white')
label_denied_f7 = tkinter.Label(fenetre7, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1_f7=tkinter.Label(fenetre7,text="")
reponse_entry1_f7.place(x=588, y=427)

reponse_entry2_f7=tkinter.Label(fenetre7,text="")
reponse_entry2_f7.place(x=355, y=545)

reponse_entry3_f7=tkinter.Label(fenetre7,text="")
reponse_entry3_f7.place(x=590, y=545)


reponse_entry4_f7=tkinter.Label(fenetre7,text="")
reponse_entry4_f7.place(x=838, y=545)


reponse_entry5_f7=tkinter.Label(fenetre7,text="")
reponse_entry5_f7.place(x=866, y=650)


reponse_entry6_f7=tkinter.Label(fenetre7,text="")
reponse_entry6_f7.place(x=866, y=650)


reponse_entry7_f7=tkinter.Label(fenetre7,text="")
reponse_entry7_f7.place(x=530, y=570)

reponse_entry8_f7=tkinter.Label(fenetre7,text="")
reponse_entry8_f7.place(x=600, y=620)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
question1_label_f7 = tkinter.Label(fenetre7, text="1- Du plus petit au plus grand :  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question1_label_f2 = tkinter.Label(fenetre6, text="1- Donne la dimension en longueur  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")#FDFBFB",justify="left")
question1_label_f7.place(x=0, y=0, relx=0.31, rely=0.60, anchor="center")

entry1_f7 = tkinter.Entry(reponse_entry1_f7, font=("Comic sans Ms", 18, ""), width=18,highlightthickness=1, highlightbackground="orange")
entry1_f7.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label_f7 = tkinter.Label(fenetre7, text="2- Saisie le résultat des opérations suivantes :\n 243x3 = \t\t 106x5 = \t\t 475+34= ",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question3_label_f7 = tkinter.Label(fenetre7, text="3- Pour entouré le musée, Mbarga pense qu'il faut utiliser l'aire et \n Kambouo pense au périmetre. lequel des deux a raison ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left" )
#question4_label_f2 = tkinter.Label(fenetre6, text="4- Pour entouré le musée, Mbarga pense qu'il faut utiliser l'aire et \n Kambouo pense au périmetre. lequel des deux a raison?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385,
# rely=0.63, anchor="center")
question2_label_f7.place(x=0, y=0, relx=0.40, rely=0.73, anchor="center")
#question3_label_f7.place(x=0, y=0, relx=0.444, rely=0.87, anchor="center")
#question4_label_f2.place(x=0, y=0, relx=0.405, rely=0.91, anchor="center")

entry2_f7 = tkinter.Entry(reponse_entry2_f7, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry2_f7.pack()



#question2b_label.pack()
entry3_f7 = tkinter.Entry(reponse_entry3_f7, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry3_f7.pack()

# Create question 3
question4_labe_f7 = tkinter.Label(fenetre7, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4_f7 =tkinter.Entry(reponse_entry4_f7, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry4_f7.pack()
"""
entry5_f7 = tkinter.Entry(reponse_entry5_f7, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry5_f7.pack()
"""
#entry6_f2 = tkinter.Entry(reponse_entry6_f2, font=("Comic sans Ms", 18, ""), width=5,highlightthickness=1, highlightbackground="orange")
#entry6_f2.pack()

#entry7_f2 = tkinter.Entry(reponse_entry7_f2, font=("Comic sans Ms", 18, ""), width=29,highlightthickness=1, highlightbackground="orange")
#entry7_f2.pack()

#entry8_f2 = tkinter.Entry(reponse_entry8_f2, font=("Comic sans Ms", 18, ""), width=10,highlightthickness=1, highlightbackground="orange")
#entry8_f2.pack()

# Create a button to check the answers
check_button_f7 = customtkinter.CTkButton(fenetre7, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f7.place(x=1050, y=380)

# Create other widgets
label_text_f7 = tkinter.Label(fenetre7, text="Classe les nombres suivant \n en les séparant par des virgules: 156 ,  345 ,  123, 349  \n ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#label_text2_f2 = tkinter.Label(fenetre2, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
btn_quitter_f7 = customtkinter.CTkButton(fenetre7, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre7.destroy)

# Position other widgets
label_text_f7.place(x=0, y=0, relx=0.46, rely=0.15, anchor="center")


#config
# Création du bouton Suivant
#bouton_suivant = customtkinter.CTkButton(fenetre1, text="Suivant", width=3, font=("Comic Sans Ms", 16), border_spacing=0, border_width=0)
# Création du bouton Précédent
bouton_precedent = customtkinter.CTkButton(fenetre7, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre7, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)

#bouton de reset

reset_img_f7=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_7=tkinter.Label(fenetre7, image=reset_img_f7)
 
# Create a butt8.place(x=1290, y=0)
# Create a button to clear the entries
clear_button_f7 = tkinter.Button(fenetre7, command=clear_entries_f7, image=reset_img_f7, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f7.place(x=1290, y=0)


# Use the lift() method to bring labels to the front

label_acess_f7.lift()
label_denied_f7.lift()
mon_label_img_f7.lift()
mon_label_img1_f7.lift()

label_text_f7.lift()

check_button_f7.lift()
reponse_entry1_f7.lift()
reponse_entry2_f7.lift()
reponse_entry3_f7.lift()
reponse_entry4_f7.lift()
reponse_entry5_f7.lift()
reponse_entry6_f7.lift()
#reponse_entry7_f7.lift()
reponse_entry8_f7.lift()

fenetre7.mainloop()