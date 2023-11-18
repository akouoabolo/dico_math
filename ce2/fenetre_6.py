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

def clear_entries_f8():
    #entry1_f6.delete(0, 'end')
    #entry2_f6.delete(0, 'end')
    #entry3_f6.delete(0, 'end')
    #entry4_f6.delete(0, 'end')
    #entry5_f7.delete(0, 'end')
    #entry6_f2.delete(0, 'end')
    #entry7_f2.delete(0, 'end')
    #entry8_f2.delete(0, 'end')
    global random_number
    random_number = random.randint(1, 100)
    checkbox_var_kg.set(False)
    checkbox_var_hg.set(False)
    checkbox_var_dag.set(False)
    checkbox_var_g.set(False)
    user_input.set("")
    result_label.set("")
    label_instruction.config(text=f"Convertir {random_number} grammes en:", font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
    label_instruction.place(x=300, y=80)
    
    label_denied_f6.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f6.place_forget()
    
    label_acess_f6.place_forget()
    mon_label_img_f6.place_forget()
#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------

# Create a function to check the answers

def check_answers():
    #answer1_f6 = entry1_f6.get().strip()
    #answer2_f6 = entry2_f6.get().strip()
    #answer3_f6 = entry3_f6.get().strip()
    #answer4_f6 = entry4_f6.get().strip()
    #answer5_f7 = entry5_f7.get().strip()
    #answer6_f2 = entry6_f2.get().strip()
    #answer7_f2 = entry7_f2.get().strip()
    #answer8_f2 = entry7_f2.get().strip()
    try:
        user_input_value = float(user_input.get())
    except ValueError:
        label_denied_f6.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f6.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f6.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")  
    

    if (
       # answer1_f6 == "1" and
       # answer2_f6 == "1" and
       # answer3_f6 == "1" and
        #answer4_f6 == "1" 
        #answer5_f7 == "1" 
        #answer6_f2 == "1" and
        #answer7_f2 == "1" and
        #answer8_f2 == "1" 
    checkbox_var_kg.get() and user_input_value == random_number / 1000
         
    ):
        label_acess_f6.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f6.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f6.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")
 
    elif(
    checkbox_var_hg.get() and user_input_value == random_number / 100
    ):
        label_acess_f6.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f6.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f6.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")     
        
    elif(
    checkbox_var_hg.get() and user_input_value == random_number / 10
    ):
        label_acess_f6.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f6.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f6.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")     
    elif(
    checkbox_var_g.get() and user_input_value == random_number
    ):
        label_acess_f6.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f6.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f6.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")         
    else:    
        label_denied_f6.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f6.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f6.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")
#----------------------------------------------------------------------------------------------------------------
"""def check_conversion():
    try:
        user_input_value = float(user_input.get())
    except ValueError:
        result_label.set("Veuillez entrer un nombre valide.")
        return

    if checkbox_var_kg.get() and user_input_value == random_number / 1000:
        result_label.set("Bravo!")
    elif checkbox_var_hg.get() and user_input_value == random_number / 100:
        result_label.set("Bravo!")
    elif checkbox_var_dag.get() and user_input_value == random_number / 10:
        result_label.set("Bravo!")
    elif checkbox_var_g.get() and user_input_value == random_number:
        result_label.set("Bravo!")
    else:
        result_label.set("Dommage, essayez encore.")
"""
#def reset_exercise():
    #global random_number
    #random_number = random.randint(1, 100)
    #checkbox_var_kg.set(False)
    #checkbox_var_hg.set(False)
    #checkbox_var_dag.set(False)
    #checkbox_var_g.set(False)
    #user_input.set("")
    #result_label.set("")
    #label_instruction.config(text=f"Convertir {random_number} grammes en:", font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
    #label_instruction.place(x=300, y=80)

#------------------------------------------------------------------------------------------------------------------

# Create the main window    
fenetre6 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre6.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre6.resizable(width=False, height=False)


#img = ImageTk.PhotoImage(Image.open("font.png"))
#mg1 = ImageTk.PhotoImage(Image.open("74.png"))

center_window(fenetre6, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f6 = ImageTk.PhotoImage(Image.open("font.png"))

img_f6 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f6 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f6=tkinter.Label(fenetre6, image=img_f6, bg="#EAAC14")
mon_label_img1_f6=tkinter.Label(fenetre6, image=img1_f6, bg="#EAAC14")
#mon_label_img.pack()
background_label_f6 = tkinter.Label(fenetre6, image=image_f6)
background_label_f6.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f6 = tkinter.Label(fenetre6, fg='white')
label_denied_f6 = tkinter.Label(fenetre6, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

# Créer la fenêtre principale

# Générer un nombre aléatoire entre 1 et 100
#--------------------------------------------------
# Générer un nombre aléatoire entre 1 et 100
random_number = random.randint(1, 100)

# Variables pour stocker les entrées utilisateur
user_input = tkinter.StringVar()
result_label = tkinter.StringVar()

# Créer les éléments d'interface utilisateur
label_instruction = tkinter.Label(
    fenetre6, text=f"Convertir {random_number} grammes en:",  font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
label_instruction.place(x=300, y=80)

checkbox_var_kg = tkinter.BooleanVar()
checkbox_var_hg = tkinter.BooleanVar()
checkbox_var_dag = tkinter.BooleanVar()
checkbox_var_g = tkinter.BooleanVar()

checkbox_kg = tkinter.Checkbutton(fenetre6, text="Kilogramme", variable=checkbox_var_kg, font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
checkbox_hg = tkinter.Checkbutton(fenetre6, text="Hectogramme", variable=checkbox_var_hg,font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
checkbox_dag = tkinter.Checkbutton(fenetre6, text="Decagramme", variable=checkbox_var_dag, font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
checkbox_g = tkinter.Checkbutton(fenetre6, text="Gramme", variable=checkbox_var_g, font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")

label_user_input = tkinter.Label(fenetre6, text="Entrez la conversion:", font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
entry_user_input = tkinter.Entry(fenetre6, textvariable=user_input, font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left",highlightthickness=1, highlightbackground="orange")

#button_check = tkinter.Button(fenetre6, text="Vérifier", command=check_conversion)
#button_reset = tkinter.Button(fenetre6, text="Réinitialiser", command=reset_exercise)

label_result = tkinter.Label(fenetre6   , textvariable=result_label)










#-------------------------------------------------------------------------
# Placer les éléments dans la grille
#label_instruction.pack()
checkbox_kg.place(x="180", y="400")
checkbox_hg.place(x="400", y="400")
checkbox_dag.place(x="630", y="400")
checkbox_g.place(x="830", y="400")

label_user_input.place(x="310", y="500",)
entry_user_input.place(x="560", y="500",)

#button_check.pack()
#button_reset.pack()

label_result.pack()






#reponse_entry1_f6=tkinter.Label(fenetre6,text="")
#eponse_entry1_f6.place(x=450, y=429)

#reponse_entry2_f6=tkinter.Label(fenetre6,text="")
#reponse_entry2_f6.place(x=870, y=429)
#reponse_entry3_f6=tkinter.Label(fenetre6,text="")
#reponse_entry3_f6.place(x=470, y=510)


#reponse_entry4_f6=tkinter.Label(fenetre6,text="")
#reponse_entry4_f6.place(x=695, y=680)

#reponse_entry5_f6=tkinter.Label(fenetre6,text="")
#reponse_entry5_f6.place(x=866, y=650)


#reponse_entry6_f6=tkinter.Label(fenetre6,text="")
#reponse_entry6_f6.place(x=866, y=650)


#reponse_entry7_f6=tkinter.Label(fenetre6,text="")
#reponse_entry7_f6.place(x=530, y=570)

#reponse_entry8_f6=tkinter.Label(fenetre6,text="")
#reponse_entry8_f6.place(x=600, y=620)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
#question1_label_f6 = tkinter.Label(fenetre6, text="1- l'angle plat :  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question1_label_f2 = tkinter.Label(fenetre6, text="1- Donne la dimension en longueur  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")#FDFBFB",justify="left")
#question1_label_f6.place(x=0, y=0, relx=0.27, rely=0.60, anchor="center")

#entry1_f6 = tkinter.Entry(reponse_entry1_f6, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry1_f6.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question2_label_f6 = tkinter.Label(fenetre6, text="2- L'angle droit : ",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question3_label_f6 = tkinter.Label(fenetre6, text="3- L'angle obtus :", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left" )
#question4_label_f6 = tkinter.Label(fenetre6, text="4- Langle aigu : ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385,
# rely=0.63, anchor="center")
#question2_label_f6.place(x=0, y=0, relx=0.274, rely=0.70, anchor="center")
#question3_label_f6.place(x=0, y=0, relx=0.567, rely=0.60, anchor="center")
#question4_label_f6.place(x=0, y=0, relx=0.561, rely=0.70, anchor="center")

#entry2_f6 = tkinter.Entry(reponse_entry2_f6, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry2_f6.pack()



#question2b_label.pack()
#entry3_f6 = tkinter.Entry(reponse_entry3_f6, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry3_f6.pack()

# Create question 3
question4_labe_f6 = tkinter.Label(fenetre6, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

#entry4_f8 = tkinter.Entry(reponse_entry4_f6, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
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
check_button_f6 = customtkinter.CTkButton(fenetre6, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f6.place(x=1050, y=380)

# Create other widgets

#label_text_f6 = tkinter.Label(fenetre6, text="Choisi l'unité de conversion ! ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#label_text2_f2 = tkinter.Label(fenetre2, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
btn_quitter_f6 = customtkinter.CTkButton(fenetre6, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre6.destroy)

# Position other widgets
#label_text_f6.place(x=0, y=0, relx=0.33, rely=0.15, anchor="center")
#label_text2_f2.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")
btn_quitter_f6.place(x=1050, y=680)


#config
# Création du bouton Suivant
#bouton_suivant = customtkinter.CTkButton(fenetre1, text="Suivant", width=3, font=("Comic Sans Ms", 16), border_spacing=0, border_width=0)
# Création du bouton Précédent
def precedent():
    fenetre6.destroy()
    subprocess.run(['python', 'fenetre_7.py'])

bouton_precedent = customtkinter.CTkButton(fenetre6, text="Précédent", command=precedent, width=3, font=("Comic Sans Ms", 16))
bouton_precedent.pack(side=tkinter.LEFT)

def suivant():
    fenetre6.destroy()
    subprocess.run(['python', 'fenetre_9.py'])

bouton_suivant = customtkinter.CTkButton(fenetre6, text="Suivant", command=suivant, width=3, font=("Comic Sans Ms", 16))
bouton_suivant.pack(side=tkinter.RIGHT)

#bouton de reset

reset_img_f6=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f6=tkinter.Label(fenetre6, image=reset_img_f6)
 
# Create a button to clear the entries
clear_button_f6 = tkinter.Button(fenetre6, command=clear_entries_f8, image=reset_img_f6, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f6.place(x=1290, y=0)


# Use the lift() method to bring labels to the front

label_acess_f6.lift()
label_denied_f6.lift()
mon_label_img_f6.lift()
mon_label_img1_f6.lift()

#label_text_f6.lift()
#label_text2_f2.lift()
btn_quitter_f6.lift()
check_button_f6.lift()
#reponse_entry1_f6.lift()
#reponse_entry2_f6.lift()
#reponse_entry3_f6.lift()
#reponse_entry4_f6.lift()
#reponse_entry5_f6.lift()
#reponse_entry6_f6.lift()
#reponse_entry7_f7.lift()
#reponse_entry8_f6.lift()

fenetre6.mainloop()