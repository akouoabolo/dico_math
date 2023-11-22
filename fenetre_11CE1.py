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

def clear_entries_f11():
    entry1_f11.delete(0, 'end')
    entry2_f11.delete(0, 'end')
    entry3_f11.delete(0, 'end')
    #entry4_f9.delete(0, 'end')
    #entry5_f7.delete(0, 'end')
    #entry6_f2.delete(0, 'end')
    #entry7_f2.delete(0, 'end')
    #entry8_f2.delete(0, 'end')
    
    label_denied_f11.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f11.place_forget()

    label_acess_f11.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f11.place_forget()
#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------

# Create a function to check the answers

def check_answers():
    answer1_f11 = entry1_f11.get().strip()
    answer2_f11 = entry2_f11.get().strip()
    answer3_f11 = entry3_f11.get().strip()
    #answer4_f8 = entry4_f8.get().strip()
    #answer5_f7 = entry5_f7.get().strip()
    #answer6_f2 = entry6_f2.get().strip()
    #answer7_f2 = entry7_f2.get().strip()
    #answer8_f2 = entry7_f2.get().strip()

    if (
        answer1_f11 == "34°C" and
        answer2_f11 == "1/3" and
        answer3_f11 == "5"  
        #answer4_f8 == "1" 
        #answer5_f7 == "1" 
        #answer6_f2 == "1" and
        #answer7_f2 == "1" and
        #answer8_f2 == "1" 
        
    ):
        label_acess_f11.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f11.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f11.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")sé
    else:
        label_denied_f11.config(text='Oops! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f11.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f11.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

def precedent():
    fenetre11.destroy()
    subprocess.run(['python', 'fenetre_10CE1.py'])  
    
def suivant():
    fenetre11.destroy()
    subprocess.run(['python', 'fenetre_12CE1.py'])  

# Create the main window    
fenetre11 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre11.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre11.resizable(width=False, height=False)


img = ImageTk.PhotoImage(Image.open("max27.png"))
img1 = ImageTk.PhotoImage(Image.open("74.png"))

center_window(fenetre11, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f11 = ImageTk.PhotoImage(Image.open("font11.png"))

img_f11 = ImageTk.PhotoImage(Image.open("max27.png"))
img1_f11 = ImageTk.PhotoImage(Image.open("74.png"))

mon_label_img_f11=tkinter.Label(fenetre11, image=img, bg="#EAAC14")
mon_label_img1_f11=tkinter.Label(fenetre11, image=img1, bg="#EAAC14")
#mon_label_img.pack()
background_label_f11 = tkinter.Label(fenetre11, image=image_f11)
background_label_f11.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f11 = tkinter.Label(fenetre11, fg='white')
label_denied_f11 = tkinter.Label(fenetre11, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1_f11=tkinter.Label(fenetre11,text="")
reponse_entry1_f11.place(x=890, y=435)

reponse_entry2_f11=tkinter.Label(fenetre11,text="")
reponse_entry2_f11.place(x=470, y=575)

reponse_entry3_f11=tkinter.Label(fenetre11,text="")
reponse_entry3_f11.place(x=400, y=668)


reponse_entry4_f11=tkinter.Label(fenetre11,text="")
reponse_entry4_f11.place(x=740, y=705)


reponse_entry5_f11=tkinter.Label(fenetre11,text="")
reponse_entry5_f11.place(x=866, y=650)


reponse_entry6_f11=tkinter.Label(fenetre11,text="")
reponse_entry6_f11.place(x=866, y=650)


reponse_entry7_f11=tkinter.Label(fenetre11,text="")
reponse_entry7_f11.place(x=530, y=570)

reponse_entry8_f11=tkinter.Label(fenetre11,text="")
reponse_entry8_f11.place(x=600, y=620)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
question1_label_f11 = tkinter.Label(fenetre11, text="1- A quelles températures les produits sont-ils stockés ?:  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question1_label_f2 = tkinter.Label(fenetre6, text="1- Donne la dimension en longueur  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")#FDFBFB",justify="left")
question1_label_f11.place(x=0, y=0, relx=0.42, rely=0.61, anchor="center")

entry1_f11 = tkinter.Entry(reponse_entry1_f11, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry1_f11.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label_f11 = tkinter.Label(fenetre11, text="2- Il y a 15 cartons qui doivent être distribués à 3 centres de santé. \nÉcrivez la fraction qui représente la part de chaque \ncentre de santé ? : ",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f11 = tkinter.Label(fenetre11, text="3- Combien de cartons chaque centre de santé \nrecevra-t-il ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left" )
#question4_label_f11 = tkinter.Label(fenetre11, text="4- Le directeur de l'hôpital consulte 5 patients par jour la 1er \nsemaine. La deuxième semaine, il consulte la moitié de la première \nsemaine. Quel est le nombre de patients consultés la deuxième semaine ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385,
# rely=0.63, anchor="center")
question2_label_f11.place(x=0, y=0, relx=0.460, rely=0.745, anchor="center")
question3_label_f11.place(x=0, y=0, relx=0.370, rely=0.89, anchor="center")
#question4_label_f11.place(x=0, y=0, relx=0.412, rely=0.90, anchor="center")

entry2_f11 = tkinter.Entry(reponse_entry2_f11, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry2_f11.pack()



#question2b_label.pack()
entry3_f11 = tkinter.Entry(reponse_entry3_f11, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry3_f11.pack()

# Create question 3
question4_labe_f7 = tkinter.Label(fenetre11, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

#entry4_f11 = tkinter.Entry(reponse_entry4_f11, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry4_f11.pack()

#entry5_f7 = tkinter.Entry(reponse_entry5_f7, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
#entry5_f7.pack()

#entry6_f2 = tkinter.Entry(reponse_entry6_f2, font=("Comic sans Ms", 18, ""), width=5,highlightthickness=1, highlightbackground="orange")
#entry6_f2.pack()

#entry7_f2 = tkinter.Entry(reponse_entry7_f2, font=("Comic sans Ms", 18, ""), width=29,highlightthickness=1, highlightbackground="orange")
#entry7_f2.pack()

#entry8_f2 = tkinter.Entry(reponse_entry8_f2, font=("Comic sans Ms", 18, ""), width=10,highlightthickness=1, highlightbackground="orange")
#entry8_f2.pack()

# Create a button to check the answers
check_button_f11 = customtkinter.CTkButton(fenetre11, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f11.place(x=1050, y=380)

# Create other widgets

label_text_f11 = tkinter.Label(fenetre11, text="Regardez cette illustration et répondez aux questions suivantes:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#label_text2_f2 = tkinter.Label(fenetre2, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
btn_quitter_f11 = customtkinter.CTkButton(fenetre11, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre11.destroy)

# Position other widgets
label_text_f11.place(x=0, y=0, relx=0.446, rely=0.15, anchor="center")
#label_text2_f2.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")
#btn_quitter_f11.place(x=1050, y=680)


#config
# Création du bouton Suivant
# Création du bouton Précédent
bouton_precedent = customtkinter.CTkButton(fenetre11, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre11, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)

#bouton de reset

reset_img_f13=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f13=tkinter.Label(fenetre11, image=reset_img_f13)
 
# Create a button to clear the entries
clear_button_f13 = tkinter.Button(fenetre11, command=clear_entries_f11, image=reset_img_f13, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f13.place(x=1290, y=0)


# Use the lift() method to bring labels to the front

label_acess_f11.lift()
label_denied_f11.lift()
mon_label_img_f11.lift()
mon_label_img1_f11.lift()

label_text_f11.lift()
#label_text2_f2.lift()
#btn_quitter_f11.lift()
check_button_f11.lift()
reponse_entry1_f11.lift()
reponse_entry2_f11.lift()
reponse_entry3_f11.lift()
reponse_entry4_f11.lift()
reponse_entry5_f11.lift()
reponse_entry6_f11.lift()
#reponse_entry7_f7.lift()
reponse_entry8_f11.lift()

fenetre11.mainloop()