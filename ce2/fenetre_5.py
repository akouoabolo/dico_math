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
    
    label_denied_f5.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f5.place_forget()
    
    label_acess_f5.place_forget()
    mon_label_img_f5.place_forget()
#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------

# Create a function to check the answers

def check_answers():

    try:
        user_input_value = float(user_input.get())
    except ValueError:
        label_denied_f5.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f5.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f5.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")  
    

    if (
 
    checkbox_var_kg.get() and user_input_value == random_number / 1000
         
    ):
        label_acess_f5.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f5.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f5.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
       #messagebox.showinfo("Félicitations", "Vous avez toutes les bonnes réponses ! Bien joué !")
 
    elif(
    checkbox_var_hg.get() and user_input_value == random_number / 100
    ):
        label_acess_f5.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f5.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f5.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")     
        
    elif(
    checkbox_var_hg.get() and user_input_value == random_number / 10
    ):
        label_acess_f5.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f5.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f5.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")     
    elif(
    checkbox_var_g.get() and user_input_value == random_number
    ):
        label_acess_f5.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f5.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f5.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")         
    else:    
        label_denied_f5.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f5.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f5.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
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

def precedent():
    fenetre5.destroy()
    subprocess.run(['python', '1.py'])
    
    
def suivant():
    fenetre5.destroy()
    subprocess.run(['python', 'fenetre_9.py'])

#------------------------------------------------------------------------------------------------------------------

# Create the main window    
fenetre5 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre5.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre5.resizable(width=False, height=False)

center_window(fenetre5, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f5 = ImageTk.PhotoImage(Image.open("font6.png"))

img_f5 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f5 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f5=tkinter.Label(fenetre5, image=img_f5, bg="#EAAC14")
mon_label_img1_f5=tkinter.Label(fenetre5, image=img1_f5, bg="#EAAC14")
#mon_label_img.pack()
background_label_f5 = tkinter.Label(fenetre5, image=image_f5)
background_label_f5.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f5 = tkinter.Label(fenetre5, fg='white')
label_denied_f5 = tkinter.Label(fenetre5, fg='#AA2822')


# Générer un nombre aléatoire entre 1 et 100
random_number = random.randint(1, 100)

# Variables pour stocker les entrées utilisateur
user_input = tkinter.StringVar()
result_label = tkinter.StringVar()

# Créer les éléments d'interface utilisateur
label_instruction = tkinter.Label(
    fenetre5, text=f"Convertir {random_number} grammes en:",  font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
label_instruction.place(x=300, y=80)

checkbox_var_kg = tkinter.BooleanVar()
checkbox_var_hg = tkinter.BooleanVar()
checkbox_var_dag = tkinter.BooleanVar()
checkbox_var_g = tkinter.BooleanVar()

checkbox_kg = tkinter.Checkbutton(fenetre5, text="Kilogramme", variable=checkbox_var_kg, font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
checkbox_hg = tkinter.Checkbutton(fenetre5, text="Hectogramme", variable=checkbox_var_hg,font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
checkbox_dag = tkinter.Checkbutton(fenetre5, text="Decagramme", variable=checkbox_var_dag, font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
checkbox_g = tkinter.Checkbutton(fenetre5, text="Gramme", variable=checkbox_var_g, font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")

label_user_input = tkinter.Label(fenetre5, text="Entrez la conversion:", font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
entry_user_input = tkinter.Entry(fenetre5, textvariable=user_input, font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left",highlightthickness=1, highlightbackground="orange")

#label_result = tkinter.Label(fenetre5   , textvariable=result_label)


#-------------------------------------------------------------------------
# Placer les éléments dans la grille

checkbox_kg.place(x="180", y="400")
checkbox_hg.place(x="400", y="400")
checkbox_dag.place(x="630", y="400")
checkbox_g.place(x="830", y="400")

label_user_input.place(x="310", y="500",)
entry_user_input.place(x="560", y="500",)

#label_result.pack()

# Create question 
question4_labe_f5 = tkinter.Label(fenetre5, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

# Create a button to check the answers
check_button_f5 = customtkinter.CTkButton(fenetre5, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f5.place(x=1050, y=380)

# bouton suivant / précédent
bouton_precedent = customtkinter.CTkButton(fenetre5, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre5, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)
#bouton de reset


reset_img_f5=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f5=tkinter.Label(fenetre5, image=reset_img_f5)
 
# Create a button to clear the entries
clear_button_f5 = tkinter.Button(fenetre5, command=clear_entries_f8, image=reset_img_f5, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f5.place(x=1290, y=0)


# Use the lift() method to bring labels to the front

label_acess_f5.lift()
label_denied_f5.lift()
mon_label_img_f5.lift()
mon_label_img1_f5.lift()

check_button_f5.lift()

fenetre5.mainloop()