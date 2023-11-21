import tkinter 
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
import subprocess
import random

window_width = 1350
window_height = 750
# créer une fenêtre
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = int((screen_width - width) / 2)
    y_position = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x_position}+{y_position}") 



def i1():
      fenetre0.destroy()
      subprocess.call(["python", "fenetre_7.py"])
def i2():
      fenetre0.destroy()
      subprocess.call(["python", "fenetre_9.py"])

def i3():
      fenetre0.destroy()
      subprocess.call(["python", "fenetre_8.py"])
      
"""def precedent():
    fenetre0.destroy()
    subprocess.run(['python', '0.py'])  
    
def suivant():
    fenetre0.destroy()
    subprocess.run(['python', '1.py'])  
"""
fenetre0 =customtkinter.CTk()
center_window(fenetre0, window_width, window_height) #position of windows2

# ajouter un titre
fenetre0.title("dico_mathématique")
fenetre0.resizable(width=False, height=False)
# modifier la taille
#screen.geometry("1920x1080")

# Create a Label widget and set the image as its background
image_f0 = ImageTk.PhotoImage(Image.open("00.png"))




reset_img_f3=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f3=tkinter.Label(fenetre0, image=reset_img_f3)

"""img_f0 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f0 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f0=tkinter.Label(fenetre0, image=img_f0, bg="#EAAC14")
mon_label_img1_f8=tkinter.Label(fenetre0, image=img1_f0, bg="#EAAC14")"""
#mon_label_img.pack()
background_label_f0 = tkinter.Label(fenetre0, image=image_f0)
background_label_f0.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f0 = tkinter.Label(fenetre0, fg='white')
label_denied_f0 = tkinter.Label(fenetre0, fg='#AA2822')

#config
# Création du bouton Suivant
"""bouton_precedent = customtkinter.CTkButton(fenetre0, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre0, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)"""

# Création du bouton avec l'image de fond
start = customtkinter.CTkButton(fenetre0,text=" ",image=img, font=('Lucida Handwriting', 30),command=i1)

"""verifi2 = tkinter.Button(fenetre0,text="Découvrir ", font=('Lucida Handwriting', 30), bg='white',command=i2)
verifi2.place(x=960, y=740)

verifi3 = tkinter.Button(fenetre0,text="Découvrir ", font=('Lucida Handwriting', 30), bg='white',command=i3)
verifi3.place(x=1430, y=740)"""

start.lift()

"""verifi2.lift()
verifi3.lift()"""
fenetre0.mainloop()