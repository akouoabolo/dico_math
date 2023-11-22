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
# Create a function to check the answers
def check_answers():
    answer1_f1 = entry1_f1.get().strip()
    answer2_f1 = entry2_f1.get().strip()
    answer3_f1 = entry3_f1.get().strip()
    answer4_f1 = entry3_f1.get().strip()

    if (
        answer1_f1 == "cent-trente" and
        answer2_f1 == "mètre" and
        answer3_f1 == "30m" and
        answer4_f1 == "129m"
      
    ):
        label_acess_f1.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f1.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f1.place(x=0, y=0, relx=0.87, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")
    else:
        label_denied_f1.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f1.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f1.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

# Fonction pour afficher la fenêtre secondaire et cacher la fenêtre principale
"""def afficher_fenetre2():
    fenetre1.withdraw() # Cacher la fenêtre principale
    fenetre2.deiconify() # Afficher la fenêtre secondaire

# Fonction pour afficher la fenêtre principale et cacher la fenêtre secondaire
def afficher_fenetre1():
    fenetre2.withdraw() # Cacher la fenêtre secondaire
    fenetre1.deiconify() # Afficher la fenêtre principale"""
    
# Function to clear entry fields
def clear_entries():
    entry1_f1.delete(0, 'end')
    entry2_f1.delete(0, 'end')
    entry3_f1.delete(0, 'end')
    entry4_f1.delete(0, 'end')
    
    label_denied_f1.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f1.place_forget()        
    label_acess_f1.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f1.place_forget()  
    
    #fenêtre2
def clear_entries_f2():
    entry1_f1.delete(0, 'end')
    entry2_f1.delete(0, 'end')
    entry3_f1.delete(0, 'end')
    entry4_f1.delete(0, 'end')
    
    label_denied_f1.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f1.place_forget()
    
     
    label_acess_f1.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f1.place_forget()
    
    
#fonction pour poisitionner les fenêtres au centre à l'ouverture
    
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = int((screen_width - width) / 2)
    y_position = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x_position}+{y_position}") 
 

# fonctions de précédent() et suivant()
def precedent():
    fenetre1.destroy()
    subprocess.run(['python', '0.py'])  
    
def suivant():
    fenetre1.destroy()
    subprocess.run(['python', 'fenetre_2CE1.py'])  

# Create the main window    
fenetre1 = customtkinter.CTk()
#fenetre1.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre1.title("dico_mathématique")
#fenetre1.geometry("1350x750")

window_width = 1350
window_height = 750

center_window(fenetre1, window_width, window_height) #position of windows1

fenetre1.resizable(width=False, height=False)

# Create a Label widget and set the image as its background
image_f1 = ImageTk.PhotoImage(Image.open("play768.png"))


img_f1 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f1 = ImageTk.PhotoImage(Image.open("74.png"))

mon_label_img_f1=tkinter.Label(fenetre1, image=img_f1, bg="#EAAC14")
mon_label_img1_f1=tkinter.Label(fenetre1, image=img1_f1, bg="#EAAC14")
#mon_label_img.pack()_f1

background_label_f1 = tkinter.Label(fenetre1, image=image_f1)
background_label_f1.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f1 = tkinter.Label(fenetre1, fg='white')
label_denied_f1 = tkinter.Label(fenetre1, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1_f1=tkinter.Label(fenetre1,text="")
reponse_entry1_f1.place(x=760, y=393)

reponse_entry2_f1=tkinter.Label(fenetre1,text="")
reponse_entry2_f1.place(x=600, y=540)

reponse_entry3_f1=tkinter.Label(fenetre1,text="")
reponse_entry3_f1.place(x=425, y=616)


reponse_entry4_f1=tkinter.Label(fenetre1,text="")
reponse_entry4_f1.place(x=816, y=660)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
question1_label_f1 = tkinter.Label(fenetre1, text="1- Écrivez le nombre total de plans en lettres :", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question1_label_f1.place(x=0, y=0, relx=0.37, rely=0.55, anchor="center")

entry1_f1 = tkinter.Entry(reponse_entry1_f1, font=("Comic sans Ms", 18, ""), width=10, highlightthickness=1, highlightbackground="orange")
entry1_f1.pack()

# Create question 2
question2_label_f1 = tkinter.Label(fenetre1, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2a_label_f1 = tkinter.Label(fenetre1, text="a - Quelle unité de mesure de longueur doit-on utiliser \n pour mesurer cette distance ?",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2b_label_f1 = tkinter.Label(fenetre1, text="b - Trouvez la longueur qui sépare les orangers et \n les manguiers :", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


question2_label_f1.place(x=0, y=0, relx=0.385, rely=0.63, anchor="center")
question2a_label_f1.place(x=0, y=0, relx=0.41, rely=0.72, anchor="center")
question2b_label_f1.place(x=0, y=0, relx=0.39, rely=0.82, anchor="center")


entry2_f1 = tkinter.Entry(reponse_entry2_f1, font=("Comic sans Ms", 18, ""), width=10, highlightthickness=1, highlightbackground="orange")
entry2_f1.pack()



#question2b_label.pack()
entry3_f1 = tkinter.Entry(reponse_entry3_f1, font=("Comic sans Ms", 18, ""), width=10,highlightthickness=1, highlightbackground="orange")
entry3_f1.pack()

# Create question 3
question3_label_f1 = tkinter.Label(fenetre1, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f1.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4_f1 = tkinter.Entry(reponse_entry4_f1, font=("Comic sans Ms", 18, ""), width=10, highlightthickness=1, highlightbackground="orange")
entry4_f1.pack()

# Create a button to check the answers
check_button_f1 = customtkinter.CTkButton(fenetre1, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers, border_width=0)
check_button_f1.place(x=1050, y=380)

# Create other widgets
label_text_f1 = tkinter.Label(fenetre1, text="Votre père souhaite créer un potager sur un espace de 195 m \n de long dans sa concession. Pour ce faire, il achète :\n ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
#btn_quitter = customtkinter.CTkButton(fenetre1, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre1.destroy)

# Position other widgets
label_text_f1.place(x=0, y=0, relx=0.43, rely=0.15, anchor="center")
#btn_quitter.place(x=1050, y=680)


# bouton suivant / précédent
bouton_precedent = customtkinter.CTkButton(fenetre1, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre1, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)

#bouton de reset

reset_img_f1=ImageTk.PhotoImage(Image.open("reset_1.png"))
reset_img_label_f1=tkinter.Label(fenetre1, image=reset_img_f1)
 
# Create a button to clear the entries
clear_button_f1 = tkinter.Button(fenetre1, command=clear_entries, image=reset_img_f1, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f1.place(x=1290, y=0)

# Use the lift() method to bring labels to the front
label_acess_f1.lift()
label_denied_f1.lift()
mon_label_img_f1.lift()
mon_label_img1_f1.lift()

label_text_f1.lift()
#btn_quitter.lift()
check_button_f1.lift()
reponse_entry2_f1.lift()
reponse_entry3_f1.lift()
reponse_entry4_f1.lift()
# Add widgets to the main window
#btn_nouvel_info.pack(pady=20)
#message_info.pack(pady=10, fill="x", expand="True", padx="15")

# Main event loop
fenetre1.mainloop()
