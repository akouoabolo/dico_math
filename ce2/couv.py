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
      subprocess.call(["python", "0.py"])


fenetre0 =customtkinter.CTk()
center_window(fenetre0, window_width, window_height) #position of windows2

# ajouter un titre
fenetre0.title("dico_mathématique")
fenetre0.resizable(width=False, height=False)
# modifier la taille
#screen.geometry("1920x1080")

# Create a Label widget and set the image as its background
image_f0 = ImageTk.PhotoImage(Image.open("couv.png"))




img=ImageTk.PhotoImage(Image.open("bouton.png"))
Label_img=tkinter.Label(fenetre0, image=img)

#mon_label_img.pack()
background_label_f0 = tkinter.Label(fenetre0, image=image_f0)
background_label_f0.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f0 = tkinter.Label(fenetre0, fg='white')
label_denied_f0 = tkinter.Label(fenetre0, fg='#AA2822')


# Création du bouton avec l'image de fond
start = tkinter.Button(fenetre0,text=" ",image=img, font=('Lucida Handwriting', 30),command=i1, relief="flat", bg='white')
start.place(x=1210, y=540)


start.lift()

"""verifi2.lift()
verifi3.lift()"""
fenetre0.mainloop()