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

    if (
        answer1_f7 == "1" and
        answer2_f7 == "1" and
        answer3_f7 == "1" and
        answer4_f7 == "1" 
        #answer5_f7 == "1" 
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
    subprocess.run(['python', 'fenetre_7.py'])
    
    
def suivant():
    fenetre7.destroy()
    subprocess.run(['python', 'fenetre_9.py'])
    
    #------------------------------------------------------------------------
# Create the main window    
fenetre7 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre7.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre7.resizable(width=False, height=False)


center_window(fenetre7, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f7 = ImageTk.PhotoImage(Image.open("font8.png"))

img_f7 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f7 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f7=tkinter.Label(fenetre7, image=img_f7, bg="#EAAC14")
mon_label_img1_f7=tkinter.Label(fenetre7, image=img1_f7, bg="#EAAC14")
#mon_label_img.pack()
background_label_f7 = tkinter.Label(fenetre7, image=image_f7)
background_label_f7.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f7 = tkinter.Label(fenetre7, fg='white')
label_denied_f7 = tkinter.Label(fenetre7, fg='#AA2822')

#position des entrer
reponse_entry1_f7=tkinter.Label(fenetre7,text="")
reponse_entry1_f7.place(x=250, y=439)

reponse_entry2_f7=tkinter.Label(fenetre7,text="")
reponse_entry2_f7.place(x=742, y=445)

reponse_entry3_f7=tkinter.Label(fenetre7,text="")
reponse_entry3_f7.place(x=330, y=640)


reponse_entry4_f7=tkinter.Label(fenetre7,text="")
reponse_entry4_f7.place(x=695, y=640)

# Create question 1
Lable1_label_f7 = tkinter.Label(fenetre7, text="FigureA  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
#question1_label_f2 = tkinter.Label(fenetre6, text="1- Donne la dimension en longueur  ",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")#FDFBFB",justify="left")
Lable1_label_f7.place(x=0, y=0, relx=0.25, rely=0.55, anchor="center")

entry1_f7 = tkinter.Entry(reponse_entry1_f7, font=("Comic sans Ms", 18, ""), width=10,highlightthickness=1, highlightbackground="orange")
entry1_f7.pack()

# Create question 2
#question2_label = tkinter.Label(fenetre, text="2- Les orangers et les manguiers sont séparés par \n 1 barrage les uns des autres." , font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
Label2_label_f7 = tkinter.Label(fenetre7, text="FigureB  ",  font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
question3_label_f7 = tkinter.Label(fenetre7, text="\n\n1- Entre dans les champs la nature des figures géométriques", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left" )
question4_label_f7 = tkinter.Label(fenetre7, text="2- Donne le périmètre : \n\nFigureA: \t\t\t FigureB:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


#question2_label.place(x=0, y=0, relx=0.385,
# rely=0.63, anchor="center")
Label2_label_f7.place(x=0, y=0, relx=0.61, rely=0.55, anchor="center")
question3_label_f7.place(x=0, y=0, relx=0.4, rely=0.68, anchor="center")
question4_label_f7.place(x=0, y=0, relx=0.323, rely=0.84, anchor="center")

entry2_f7 = tkinter.Entry(reponse_entry2_f7, font=("Comic sans Ms", 18, ""), width=10,highlightthickness=1, highlightbackground="orange")
entry2_f7.pack()



#question2b_label.pack()
entry3_f7 = tkinter.Entry(reponse_entry3_f7, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry3_f7.pack()

entry4_f7 = tkinter.Entry(reponse_entry4_f7, font=("Comic sans Ms", 18, ""), width=7,highlightthickness=1, highlightbackground="orange")
entry4_f7.pack()

# Create a button to check the answers
check_button_f7 = customtkinter.CTkButton(fenetre7, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f7.place(x=1050, y=380)

# Create other widgets

label_text_f7 = tkinter.Label(fenetre7, text="Observe les figures ci-dessous et répond au questionnaire\n . ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

#btn_quitter_f7 = customtkinter.CTkButton(fenetre7, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre7.destroy)

# Position other widgets
label_text_f7.place(x=0, y=0, relx=0.41, rely=0.18, anchor="center")

#btn_quitter_f7.place(x=1050, y=680)

# Création du bouton Précédent
# bouton suivant / précédent
bouton_precedent = customtkinter.CTkButton(fenetre7, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre7, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)

#bouton de reset

reset_img_f7=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f7=tkinter.Label(fenetre7, image=reset_img_f7)
 
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

fenetre7.mainloop()