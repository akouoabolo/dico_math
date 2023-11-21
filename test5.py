import tkinter 
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image

# Create a function to check the answers
def check_answers():
    answer1 = entry1.get().strip()
    answer2 = entry2.get().strip()
    answer3 = entry3.get().strip()
    answer4 = entry4.get().strip()

    if (
        answer1 == "1" and
        answer2 == "1" and
        answer3 == "1" and
        answer4 == "1"
    ):
        label_acess.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")
    else:
        label_denied.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")

# Create the main window    
fenetre = customtkinter.CTk()
fenetre.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre.title("dico_mathématique")
fenetre.geometry("1350x750")
fenetre.resizable(width=False, height=False)

# Create a Label widget and set the image as its background
image = ImageTk.PhotoImage(Image.open("play76.png"))


img = ImageTk.PhotoImage(Image.open("max27.png"))
img1 = ImageTk.PhotoImage(Image.open("74.png"))

mon_label_img=tkinter.Label(fenetre, image=img, bg="#EAAC14")
mon_label_img1=tkinter.Label(fenetre, image=img1, bg="#EAAC14")
#mon_label_img.pack()

background_label = tkinter.Label(fenetre, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_acess = tkinter.Label(fenetre, fg='white')
label_denied = tkinter.Label(fenetre, fg='#AA2822')
# Create a frame for the exercise
#exercise_frame = tkinter.LabelFrame(fenetre, text="")
#exercise_frame.place(x=300, y=200)

reponse_entry1=tkinter.Label(fenetre,text="")
reponse_entry1.place(x=770, y=455)

reponse_entry2=tkinter.Label(fenetre,text="")
reponse_entry2.place(x=930, y=500)

reponse_entry3=tkinter.Label(fenetre,text="")
reponse_entry3.place(x=700, y=615)


reponse_entry4=tkinter.Label(fenetre,text="")
reponse_entry4.place(x=816, y=660)
# Create a label with the problem statement
#problem_label = tkinter.Label(exercise_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur.\\nDe retour au domicile il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne.\\nIl veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
#problem_label.pack()

# Create question 1
question1_label = tkinter.Label(fenetre, text="1- Les abreuvoirs ont la forme de quels solide ?", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question1_label.place(x=0, y=0, relx=0.37, rely=0.63, anchor="center")

entry1 = tkinter.Entry(reponse_entry1, font=("Comic sans Ms", 18, ""), width=10)
entry1.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label = tkinter.Label(fenetre, text="2- Peut-on fabriquer des abreuvoirs sous frome cylindriques ?",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label = tkinter.Label(fenetre, text="3- Supposons que les abreuvoirs fassent 2 mètres de haut,\n que se passera-t-il ? \n  l'eau va déborder - trop haut - trop bas", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#question2_label.place(x=0, y=0, relx=0.385, rely=0.63, anchor="center")
question2_label.place(x=0, y=0, relx=0.43, rely=0.69, anchor="center")
question3_label.place(x=0, y=0, relx=0.418, rely=0.80, anchor="center")


entry2 = tkinter.Entry(reponse_entry2, font=("Comic sans Ms", 18, ""), width=6)
entry2.pack()



#question2b_label.pack()
entry3 = tkinter.Entry(reponse_entry3, font=("Comic sans Ms", 18, ""), width=10)
entry3.pack()

# Create question 3
question4_label = tkinter.Label(fenetre, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4 = tkinter.Entry(reponse_entry4, font=("Comic sans Ms", 18, ""), width=10)
entry4.pack()

# Create a button to check the answers
check_button = customtkinter.CTkButton(fenetre, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button.place(x=1050, y=380)

# Create other widgets
label_text = tkinter.Label(fenetre, text="Un agriculteur du village posséde dans sa ferme : \n ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
label_text2 = tkinter.Label(fenetre, text="Chaque jour, ces animaux consomment 285 kg de nourriture. ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_nouvel_info = customtkinter.CTkButton(fenetre, text="Afficher une nouvelle info", font=("Comic Sans Ms", 24))
#message_info = tkinter.Message(fenetre, relief="sunken", width=650, font=(14))
btn_quitter = customtkinter.CTkButton(fenetre, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre.destroy)

# Position other widgets
label_text.place(x=0, y=0, relx=0.43, rely=0.15, anchor="center")
label_text2.place(x=0, y=0, relx=0.43, rely=0.56, anchor="center")
btn_quitter.place(x=1050, y=680)

# Use the lift() method to bring labels to the front
label_acess.lift()
label_denied.lift()
mon_label_img.lift()
mon_label_img1.lift()

label_text.lift()
label_text2.lift()
btn_quitter.lift()
check_button.lift()
reponse_entry2.lift()
reponse_entry3.lift()
reponse_entry4.lift()
# Add widgets to the main window
#btn_nouvel_info.pack(pady=20)
#message_info.pack(pady=10, fill="x", expand="True", padx="15")

# Main event loop
fenetre.mainloop()

