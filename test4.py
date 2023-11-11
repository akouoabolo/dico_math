import tkinter 
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image

# Create a function to check the answers
def check_answers():
    answer1 = entry1.get().strip()
    answer2 = entry2.get().strip()
    answer3 = entry3.get().strip()
    answer4 = entry3.get().strip()

    if (
        answer1 == "1" and
        answer2 == "1" and
        answer3 == "1" and
        answer4 == "1"
    ):
        label_acess.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img.place(x=0, y=0, relx=0.87, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")
    else:
        label_denied.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

# Fonction pour afficher la fenêtre secondaire et cacher la fenêtre principale
def afficher_fenetre2():
    fenetre1.withdraw() # Cacher la fenêtre principale
    fenetre2.deiconify() # Afficher la fenêtre secondaire

# Fonction pour afficher la fenêtre principale et cacher la fenêtre secondaire
def afficher_fenetre1():
    fenetre2.withdraw() # Cacher la fenêtre secondaire
    fenetre1.deiconify() # Afficher la fenêtre principale
    
# Function to clear entry fields
def clear_entries():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    
    label_denied.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1.place_forget()
    
    #fenêtre2
def clear_entries_f2():
    entry1_f2.delete(0, 'end')
    entry2_f2.delete(0, 'end')
    entry3_f2.delete(0, 'end')
    entry4_f2.delete(0, 'end')
    
    label_denied_f2.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f2.place_forget()
    
#fonction pour poisitionner les fenêtres au centre à l'ouverture
    
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = int((screen_width - width) / 2)
    y_position = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x_position}+{y_position}") 
 

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
image = ImageTk.PhotoImage(Image.open("play768.png"))


img = ImageTk.PhotoImage(Image.open("max27.png"))
img1 = ImageTk.PhotoImage(Image.open("74.png"))

mon_label_img=tkinter.Label(fenetre1, image=img, bg="#EAAC14")
mon_label_img1=tkinter.Label(fenetre1, image=img1, bg="#EAAC14")
#mon_label_img.pack()

background_label = tkinter.Label(fenetre1, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_acess = tkinter.Label(fenetre1, fg='white')
label_denied = tkinter.Label(fenetre1, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1=tkinter.Label(fenetre1,text="")
reponse_entry1.place(x=760, y=393)

reponse_entry2=tkinter.Label(fenetre1,text="")
reponse_entry2.place(x=600, y=540)

reponse_entry3=tkinter.Label(fenetre1,text="")
reponse_entry3.place(x=425, y=616)


reponse_entry4=tkinter.Label(fenetre1,text="")
reponse_entry4.place(x=816, y=660)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
question1_label = tkinter.Label(fenetre1, text="1- Écrivez le nombre total de plans en lettres :", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question1_label.place(x=0, y=0, relx=0.37, rely=0.55, anchor="center")

entry1 = tkinter.Entry(reponse_entry1, font=("Comic sans Ms", 18, ""), width=10)
entry1.pack()

# Create question 2
question2_label = tkinter.Label(fenetre1, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2a_label = tkinter.Label(fenetre1, text="a - Quelle unité de mesure de longueur doit-on utiliser \n pour mesurer cette distance ?",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2b_label = tkinter.Label(fenetre1, text="b - Trouvez la longueur qui sépare les orangers et \n les manguiers :", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


question2_label.place(x=0, y=0, relx=0.385, rely=0.63, anchor="center")
question2a_label.place(x=0, y=0, relx=0.41, rely=0.72, anchor="center")
question2b_label.place(x=0, y=0, relx=0.39, rely=0.82, anchor="center")


entry2 = tkinter.Entry(reponse_entry2, font=("Comic sans Ms", 18, ""), width=10)
entry2.pack()



#question2b_label.pack()
entry3 = tkinter.Entry(reponse_entry3, font=("Comic sans Ms", 18, ""), width=10)
entry3.pack()

# Create question 3
question3_label = tkinter.Label(fenetre1, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4 = tkinter.Entry(reponse_entry4, font=("Comic sans Ms", 18, ""), width=10)
entry4.pack()

# Create a button to check the answers
check_button = customtkinter.CTkButton(fenetre1, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers, border_width=0)
check_button.place(x=1050, y=380)

# Create other widgets
label_text = tkinter.Label(fenetre1, text="Votre père souhaite créer un potager sur un espace de 195 m \n de long dans sa concession. Pour ce faire, il achète :\n ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
btn_quitter = customtkinter.CTkButton(fenetre1, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre1.destroy)

# Position other widgets
label_text.place(x=0, y=0, relx=0.43, rely=0.15, anchor="center")
btn_quitter.place(x=1050, y=680)

#bouton de reset

reset_img=ImageTk.PhotoImage(Image.open("reset_1.png"))
reset_img_label=tkinter.Label(fenetre1, image=reset_img)
 
# Create a button to clear the entries
clear_button = tkinter.Button(fenetre1, command=clear_entries, image=reset_img, bg="white", borderwidth=0, cursor="hand2" )
clear_button.place(x=1290, y=0)

# Use the lift() method to bring labels to the front
label_acess.lift()
label_denied.lift()
mon_label_img.lift()
mon_label_img1.lift()

label_text.lift()
btn_quitter.lift()
check_button.lift()
reponse_entry2.lift()
reponse_entry3.lift()
reponse_entry4.lift()
# Add widgets to the main window
#btn_nouvel_info.pack(pady=20)
#message_info.pack(pady=10, fill="x", expand="True", padx="15")

# Main event loop


#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------


# Create a function to check the answers
def check_answers():
    answer1_f2 = entry1_f2.get().strip()
    answer2_f2 = entry2_f2.get().strip()
    answer3_f2 = entry3_f2.get().strip()
    answer4_f2 = entry4_f2.get().strip()
    

    if (
        answer1_f2 == "1" and
        answer2_f2 == "1" and
        answer3_f2 == "1" and
        answer4_f2 == "1"
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

# Create the main window    
fenetre2 =customtkinter.CTkToplevel(fenetre1)
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

mon_label_img_f2=tkinter.Label(fenetre2, image=img, bg="#EAAC14")
mon_label_img1_f2=tkinter.Label(fenetre2, image=img1, bg="#EAAC14")
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

entry1_f2 = tkinter.Entry(reponse_entry1_f2, font=("Comic sans Ms", 18, ""), width=10)
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

entry2_f2 = tkinter.Entry(reponse_entry2_f2, font=("Comic sans Ms", 18, ""), width=6)
entry2_f2.pack()



#question2b_label.pack()
entry3_f2 = tkinter.Entry(reponse_entry3_f2, font=("Comic sans Ms", 18, ""), width=10)
entry3_f2.pack()

# Create question 3
question4_labe_f2l = tkinter.Label(fenetre2, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4_f2 = tkinter.Entry(reponse_entry4_f2, font=("Comic sans Ms", 18, ""), width=10)
entry4_f2.pack()

# Create a button to check the answers
check_button_f2 = customtkinter.CTkButton(fenetre2, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f2.place(x=1050, y=380)

# Create other widgets
label_text_f2 = tkinter.Label(fenetre2, text="Monsieur Tamo posséde dans sa ferme : \n ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
label_text2_f2 = tkinter.Label(fenetre2, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
btn_quitter_f2 = customtkinter.CTkButton(fenetre2, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre2.destroy)

# Position other widgets
label_text_f2.place(x=0, y=0, relx=0.34, rely=0.15, anchor="center")
label_text2_f2.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")
btn_quitter_f2.place(x=1050, y=680)


#config
# Création du bouton Suivant
bouton_suivant = customtkinter.CTkButton(fenetre1, text="Suivant", width=3, font=("Comic Sans Ms", 16), border_spacing=0, border_width=0)
# Création du bouton Précédent
bouton_precedent = customtkinter.CTkButton(fenetre2, text="Précédent", width=3, font=("Comic Sans Ms", 16))

# Association des fonctions aux boutons
bouton_suivant.configure(command=afficher_fenetre2)
bouton_precedent.configure(command=afficher_fenetre1)       

# Placement des boutons
bouton_suivant.pack(side=tkinter.RIGHT)
bouton_precedent.pack(side=tkinter.LEFT)

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
btn_quitter_f2.lift()
check_button_f2.lift()
reponse_entry2_f2.lift()
reponse_entry3_f2.lift()
reponse_entry4_f2.lift()
# Add widgets to the main window
#btn_nouvel_info.pack(pady=20)
#message_info.pack(pady=10, fill="x", expand="True", padx="15")

# Main event loop
#------------------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------TROISIEME FENETRE-----------------------------------------------------------------
# Fonction pour afficher la fenêtre secondaire et cacher la fenêtre principale
def afficher_fenetre3():
    fenetre2.withdraw() # Cacher la fenêtre principale
    fenetre3.deiconify() # Afficher la fenêtre secondaire

# Fonction pour afficher la fenêtre principale et cacher la fenêtre secondaire
def afficher_fenetre2_():
    fenetre3.withdraw() # Cacher la fenêtre secondaire
    fenetre2.deiconify() # Afficher la fenêtre principale

# Create a function to check the answers
def check_answers():
    answer1_f3 = entry1_f2.get().strip()
    
    answer2_0f3 = entry2_0f3.get().strip()   
    answer2_1f3 = entry2_1f3.get().strip()  
    answer2_2f3 = entry2_2f3.get().strip()
    
    
    answer3_f3 = entry3_f2.get().strip()
    answer4_f3 = entry4_f2.get().strip()
    

    if (
        answer1_f3 == "1" and
        
        answer2_0f3 == "1" and
        answer2_1f3 == "1" and
        answer2_2f3 == "1" and

        answer3_f3 == "1" and
        answer4_f3 == "1"
    ):
        label_acess_f3.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f3.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f3.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")
    else:
        label_denied_f3.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f3.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f3.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

# Create the main window    
fenetre3 =customtkinter.CTkToplevel(fenetre1)
#fenetre3.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre3.title("dico_mathématique")
#fenetre3.geometry("1350x750")
fenetre3.resizable(width=False, height=False)

center_window(fenetre3, window_width, window_height) #position of windows1
# Create a Label widget and set the image as its background
image_f3 = ImageTk.PhotoImage(Image.open("pub14.png"))


img_f3 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f3 = ImageTk.PhotoImage(Image.open("74.png"))

mon_label_img_f3=tkinter.Label(fenetre3, image=img_f3, bg="#EAAC14")
mon_label_img1_f3=tkinter.Label(fenetre3, image=img1_f3, bg="#EAAC14")
#mon_label_img.pack()

background_label_f3 = tkinter.Label(fenetre3, image=image_f3)
background_label_f3.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f3 = tkinter.Label(fenetre3, fg='white')
label_denied_f3 = tkinter.Label(fenetre3, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1_f3=tkinter.Label(fenetre3,text="")
reponse_entry1_f3.place(x=640, y=434)

reponse_entry2_0f3=tkinter.Label(fenetre3,text="")
reponse_entry2_0f3.place(x=93, y=407)
reponse_entry2_1f3=tkinter.Label(fenetre3,text="")
reponse_entry2_1f3.place(x=930, y=480)
reponse_entry2_2f3=tkinter.Label(fenetre3,text="")
reponse_entry2_2f3.place(x=930, y=488)

reponse_entry3_f3=tkinter.Label(fenetre3,text="")
reponse_entry3_f3.place(x=605, y=560)

reponse_entry4_f3=tkinter.Label(fenetre3,text="")
reponse_entry4_f3.place(x=605, y=660)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

entry1_f3 = tkinter.Entry(reponse_entry1_f3, font=("Comic sans Ms", 18, ""), width=10)
entry1_f3.pack()

entry2_0f3 = tkinter.Entry(reponse_entry2_0f3, font=("Comic sans Ms", 18, ""), width=6)
entry2_0f3.pack()

entry2_1f3 = tkinter.Entry(reponse_entry2_1f3, font=("Comic sans Ms", 18, ""), width=6)
entry2_1f3.pack()

entry2_2f3 = tkinter.Entry(reponse_entry2_2f3, font=("Comic sans Ms", 18, ""), width=6)
entry2_2f3.pack()
# Create question 1
question1_label_f3 = tkinter.Label(fenetre3, text="1- Classe les dimensions de l'échelle de la plus petite \n à la plus grande:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question1_label_f3.place(x=0, y=0, relx=0.54, rely=0.58, anchor="center")



# Create question 2
#question2_label_f3 = tkinter.Label(fenetre3, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label_f3 = tkinter.Label(fenetre3, text="2- Compléte les dimensions sur l 'échelle.",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f3 = tkinter.Label(fenetre3, text="3- Entre deux numéros de droites perpendiculaires \n sur l'échelle:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question4_label_f3 = tkinter.Label(fenetre3, text="4- Classe les caissons selon l'ordre de grandeur:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.383, rely=0.63, anchor="center")
question2_label_f3.place(x=0, y=0, relx=0.489, rely=0.66, anchor="center")
question3_label_f3.place(x=0, y=0, relx=0.530, rely=0.75, anchor="center")
question4_label_f3.place(x=0, y=0, relx=0.515, rely=0.85, anchor="center")




#question2b_label.pack()
entry3_f3 = tkinter.Entry(reponse_entry3_f3, font=("Comic sans Ms", 18, ""), width=10)
entry3_f3.pack()

# Create question 3
question4_label_f3 = tkinter.Label(fenetre3, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4_f3 = tkinter.Entry(reponse_entry4_f3, font=("Comic sans Ms", 18, ""), width=10)
entry4_f3.pack()

# Create a button to check the answers
check_button_f3 = customtkinter.CTkButton(fenetre3, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f3.place(x=1050, y=380)

# Create other widgets
label_text_f3 = tkinter.Label(fenetre3, text="Des ouvriers du batiment ont fabriqué une échelle.\n En utilsiant 8 pièces de lattes de longueurs: \n 200cm, 55cm et 14cm. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#label_text2_f3 = tkinter.Label(fenetre3, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
btn_quitter_f3 = customtkinter.CTkButton(fenetre3, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre3.destroy)

# Position other widgets
label_text_f3.place(x=0, y=0, relx=0.435, rely=0.15, anchor="center")
#label_text2_f3.place(x=0, y=0, relx=0.41, rely=0.56, anchor="center")
btn_quitter_f3.place(x=1050, y=680)


#config
# Création du bouton Suivant
bouton_suivant = customtkinter.CTkButton(fenetre2, text="Suivant", width=3, font=("Comic Sans Ms", 16), border_spacing=0, border_width=0)
# Création du bouton Précédent
bouton_precedent = customtkinter.CTkButton(fenetre3, text="Précédent", width=3, font=("Comic Sans Ms", 16))

# Association des fonctions aux boutons
bouton_suivant.configure(command=afficher_fenetre3)
bouton_precedent.configure(command=afficher_fenetre2_)       

# Placement des boutons
bouton_suivant.pack(side=tkinter.RIGHT)
bouton_precedent.pack(side=tkinter.LEFT)

#bouton de reset

reset_img_f3=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f3=tkinter.Label(fenetre2, image=reset_img_f2)
 
# Create a button to clear the entries
clear_button_f3 = tkinter.Button(fenetre2, command=clear_entries_f2, image=reset_img_f3, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f3.place(x=1290, y=0)


# Use the lift() method to bring labels to the front


label_acess_f3.lift()
label_denied_f3.lift()
mon_label_img_f3.lift()
mon_label_img1_f3.lift()

label_text_f3.lift()
#label_text2_f3.lift()
btn_quitter_f3.lift()
check_button_f3.lift()
reponse_entry1_f3.lift()

reponse_entry2_0f3.lift()
reponse_entry2_1f3.lift()
reponse_entry2_2f3.lift()


reponse_entry3_f3.lift()
reponse_entry4_f3.lift()
# Add widgets to the main window
#btn_nouvel_info.pack(pady=20)
#message_info.pack(pady=10, fill="x", expand="True", padx="15")

# Main event loop
#------------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------QUATRIEME FENETRE-----------------------------------------------------------------

# Fonction pour afficher la fenêtre secondaire et cacher la fenêtre principale
def afficher_fenetre4():
    fenetre3.withdraw() # Cacher la fenêtre principale
    fenetre4.deiconify() # Afficher la fenêtre secondaire

# Fonction pour afficher la fenêtre principale et cacher la fenêtre secondaire
def afficher_fenetre3_():
    fenetre4.withdraw() # Cacher la fenêtre secondaire
    fenetre3.deiconify() # Afficher la fenêtre principale



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
fenetre4 =customtkinter.CTkToplevel(fenetre1)
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre4.title("dico_mathématique")
#fenetre4.geometry("1350x750")
fenetre4.resizable(width=False, height=False)

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
bouton_suivant = customtkinter.CTkButton(fenetre3, text="Suivant", width=3, font=("Comic Sans Ms", 16), border_spacing=0, border_width=0)
# Création du bouton Précédent
bouton_precedent = customtkinter.CTkButton(fenetre4, text="Précédent", width=3, font=("Comic Sans Ms", 16))

# Association des fonctions aux boutons
bouton_suivant.configure(command=afficher_fenetre4)
bouton_precedent.configure(command=afficher_fenetre3_)       

# Placement des boutons
bouton_suivant.pack(side=tkinter.RIGHT)
bouton_precedent.pack(side=tkinter.LEFT)

#bouton de reset

reset_img_f4=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f4=tkinter.Label(fenetre2, image=reset_img_f2)
 
# Create a button to clear the entries
clear_button_f4 = tkinter.Button(fenetre4, command=clear_entries_f2, image=reset_img_f4, bg="white", borderwidth=0, cursor="hand2" )
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






# Cacher la fenêtre 2,3,4 au début
fenetre4.withdraw()
fenetre3.withdraw()
fenetre2.withdraw()

fenetre1.mainloop()

