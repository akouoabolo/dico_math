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
    entry1_f3.delete(0, 'end')
    entry2_0f3.delete(0, 'end')
    entry2_1f3.delete(0, 'end')
    entry2_2f3.delete(0, 'end')
    entry3_f3.delete(0, 'end')
    entry4_f3.delete(0, 'end')
    
    label_denied_f3.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f3.place_forget()
    
    label_acess_f3.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f3.place_forget()

# Create a function to check the answers
def check_answers():
    answer1_f3 = entry1_f3.get().strip()
    
    answer2_0f3 = entry2_0f3.get().strip()   
    answer2_1f3 = entry2_1f3.get().strip()  
    answer2_2f3 = entry2_2f3.get().strip()
    
    
    answer3_f3 = entry3_f3.get().strip()
    answer4_f3 = entry4_f3.get().strip()
    

    if (
        answer1_f3 == "14cm,55cm,200cm" and
        
        answer2_0f3 == "200cm" and
        answer2_1f3 == "14cm" and
        answer2_2f3 == "55cm" and

        answer3_f3 == "14,200" and
        answer4_f3 == "100g,500g,1kg"
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
def precedent():
    fenetre3.destroy()
    subprocess.run(['python', 'fenetre_2CE1.py'])  
    
def suivant():
    fenetre3.destroy()
    subprocess.run(['python', 'fenetre_4CE1.py'])  
# Create the main window    
fenetre3 =customtkinter.CTk()
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
reponse_entry1_f3.place(x=630, y=430)

reponse_entry2_0f3=tkinter.Label(fenetre3,text="")
reponse_entry2_0f3.place(x=212, y=260)
reponse_entry2_1f3=tkinter.Label(fenetre3,text="")
reponse_entry2_1f3.place(x=340, y=420)
reponse_entry2_2f3=tkinter.Label(fenetre3,text="")
reponse_entry2_2f3.place(x=75, y=558)

reponse_entry3_f3=tkinter.Label(fenetre3,text="")
reponse_entry3_f3.place(x=605, y=560)

reponse_entry4_f3=tkinter.Label(fenetre3,text="")
reponse_entry4_f3.place(x=605, y=660)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

entry1_f3 = tkinter.Entry(reponse_entry1_f3, font=("Comic sans Ms", 18, ""), width=10, highlightthickness=1, highlightbackground="orange")
entry1_f3.pack()

entry2_0f3 = tkinter.Entry(reponse_entry2_0f3, font=("Comic sans Ms", 18, ""), width=6, highlightthickness=1, highlightbackground="orange")
entry2_0f3.pack()

entry2_1f3 = tkinter.Entry(reponse_entry2_1f3, font=("Comic sans Ms", 18, ""), width=6, highlightthickness=1, highlightbackground="orange")
entry2_1f3.pack()

entry2_2f3 = tkinter.Entry(reponse_entry2_2f3, font=("Comic sans Ms", 18, ""), width=6, highlightthickness=1, highlightbackground="orange")
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
entry3_f3 = tkinter.Entry(reponse_entry3_f3, font=("Comic sans Ms", 18, ""), width=10, highlightthickness=1, highlightbackground="orange")
entry3_f3.pack()

# Create question 3
question4_label_f3 = tkinter.Label(fenetre3, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4_f3 = tkinter.Entry(reponse_entry4_f3, font=("Comic sans Ms", 18, ""), width=10, highlightthickness=1, highlightbackground="orange")
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
#btn_quitter_f3.place(x=1050, y=680)


# bouton suivant / précédent
bouton_precedent = customtkinter.CTkButton(fenetre3, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre3, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)

#bouton de reset

reset_img_f3=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f3=tkinter.Label(fenetre3, image=reset_img_f3)
 
# Create a button to clear the entries
clear_button_f3 = tkinter.Button(fenetre3, command=clear_entries_f2, image=reset_img_f3, bg="white", borderwidth=0, cursor="hand2" )
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

# Main event loop
fenetre3.mainloop()
