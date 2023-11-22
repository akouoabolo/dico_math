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

def clear_entries_f3():
    entry1_f3.delete(0, 'end')
    entry2_f3.delete(0, 'end')
    entry3_f3.delete(0, 'end')
    entry4_f3.delete(0, 'end')

    
    label_denied_f3.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f3.place_forget()
    
    label_acess_f3.place_forget()
    mon_label_img_f3.place_forget()


# Create a function to check the answers
def check_answers():
    answer1_f3 = entry1_f3.get().strip()
    answer2_f3 = entry2_f3.get().strip()
    answer3_f3 = entry3_f3.get().strip()
    answer4_f3 = entry4_f3.get().strip()

    if (
        answer1_f3 == "D" and
        answer2_f3 == "B" and
        answer3_f3 == "C" and
        answer4_f3 == "A"      
    ):
        label_acess_f3.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f3.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f3.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")sé
    else:
        label_denied_f3.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f3.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f3.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        #messagebox.showerror("Essayez à nouveau", "Désolé, veuillez vérifier vos réponses et réessayer.")
def precedent():
    fenetre3.destroy()
    subprocess.run(['python', '2.py'])
    
    
def suivant():
    fenetre3.destroy()
    subprocess.run(['python', 'fenetre_4.py'])
    
# Create the main window    
fenetre3 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre3.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre3.resizable(width=False, height=False)

# center the window

center_window(fenetre3, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f3 = ImageTk.PhotoImage(Image.open("font4.png"))

img_f3 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f3 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f3=tkinter.Label(fenetre3, image=img_f3, bg="#EAAC14")
mon_label_img1_f3=tkinter.Label(fenetre3, image=img1_f3, bg="#EAAC14")

#mon_label_img.pack()
background_label_f3 = tkinter.Label(fenetre3, image=image_f3)
background_label_f3.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f3 = tkinter.Label(fenetre3, fg='white')
label_denied_f3 = tkinter.Label(fenetre3, fg='#AA2822')

reponse_entry1_f3=tkinter.Label(fenetre3,text="")
reponse_entry1_f3.place(x=450, y=505)

reponse_entry2_f3=tkinter.Label(fenetre3,text="")
reponse_entry2_f3.place(x=470, y=620)

reponse_entry3_f3=tkinter.Label(fenetre3,text="")
reponse_entry3_f3.place(x=870, y=505)


reponse_entry4_f3=tkinter.Label(fenetre3,text="")
reponse_entry4_f3.place(x=870, y=620)


reponse_entry5_f3=tkinter.Label(fenetre3,text="")
reponse_entry5_f3.place(x=866, y=650)


reponse_entry6_f3=tkinter.Label(fenetre3,text="")
reponse_entry6_f3.place(x=866, y=650)


reponse_entry7_f3=tkinter.Label(fenetre3,text="")
reponse_entry7_f3.place(x=530, y=570)

reponse_entry8_f3=tkinter.Label(fenetre3,text="")
reponse_entry8_f3.place(x=600, y=620)


# Create question 1
question1_label_f3 = tkinter.Label(fenetre3, text="1- l'angle plat :  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question1_label_f2 = tkinter.Label(fenetre6, text="1- Donne la dimension en longueur  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")#FDFBFB",justify="left")
question1_label_f3.place(x=0, y=0, relx=0.27, rely=0.70, anchor="center")

entry1_f3 = tkinter.Entry(reponse_entry1_f3, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry1_f3.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question2_label_f3 = tkinter.Label(fenetre3, text="2- L'angle droit : ",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f3 = tkinter.Label(fenetre3, text="3- L'angle obtus :", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left" )
question4_label_f3 = tkinter.Label(fenetre3, text="4- Langle aigu : ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385,
# rely=0.63, anchor="center")
question2_label_f3.place(x=0, y=0, relx=0.274, rely=0.85, anchor="center")
question3_label_f3.place(x=0, y=0, relx=0.567, rely=0.70, anchor="center")
question4_label_f3.place(x=0, y=0, relx=0.561, rely=0.85, anchor="center")

entry2_f3 = tkinter.Entry(reponse_entry2_f3, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry2_f3.pack()


#question2b_label.pack()
entry3_f3 = tkinter.Entry(reponse_entry3_f3, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry3_f3.pack()

# Create question 3
question4_labe_f3 = tkinter.Label(fenetre3, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question4_label.place(x=0, y=0, relx=0.388, rely=0.90, anchor="center")

entry4_f3 = tkinter.Entry(reponse_entry4_f3, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry4_f3.pack()

# Create a button to check the answers
check_button_f3 = customtkinter.CTkButton(fenetre3, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f3.place(x=1050, y=380)

# Create other widgets

label_text_f3 = tkinter.Label(fenetre3, text="Observe les figures ci-dessous et entre la lettre correspondant\n à l'angle . ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_quitter_f3 = customtkinter.CTkButton(fenetre3, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre3.destroy)

# Position other widgets
label_text_f3.place(x=0, y=0, relx=0.43, rely=0.15, anchor="center")

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
clear_button_f3 = tkinter.Button(fenetre3, command=clear_entries_f3, image=reset_img_f3, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f3.place(x=1290, y=0)


# Use the lift() method to bring labels to the front

label_acess_f3.lift()
label_denied_f3.lift()
mon_label_img_f3.lift()
mon_label_img1_f3.lift()

label_text_f3.lift()
#btn_quitter_f3.lift()
check_button_f3.lift()
reponse_entry1_f3.lift()
reponse_entry2_f3.lift()
reponse_entry3_f3.lift()
reponse_entry4_f3.lift()
reponse_entry5_f3.lift()
reponse_entry6_f3.lift()
reponse_entry8_f3.lift()

fenetre3.mainloop()