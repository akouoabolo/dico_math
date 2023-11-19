import tkinter 
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
import subprocess
import random

window_width = 1350
window_height = 750

# Déclarer les variables globales
num1, num2 = 0, 0
label_numbers = None


def generate_numbers():
    global num1, num2, label_numbers
    
    # Générer les nombres aléatoires
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Si label_numbers n'est pas encore créé, créez-le
    if label_numbers is None:
        label_numbers = tkinter.Label(fenetre7, text="")
        label_numbers.place(x=300, y=80)

    # Mettre à jour le texte du label avec les nouveaux nombres
    label_numbers.config(text=f"Effectue les opérations sur les nombres suivant: \n\n Nombre1 : {num1}\tNombre2 : {num2}")

def check_answers():
    try:
        user_answer = float(entry_answer.get())  # Utilisez float pour permettre des réponses décimales

        # Vérifier quelle opération a été sélectionnée
        if operation_addition.get():
            correct_answer = num1 + num2
        elif operation_soustraction.get():
            correct_answer = num1 - num2
        elif operation_multiplication.get():
            correct_answer = num1 * num2
        elif operation_division.get():
            correct_answer = num1 / num2
        else:
           label_denied_f7.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
           label_denied_f7.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
           mon_label_img1_f7.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")  

        # Comparer la réponse de l'utilisateur avec la réponse correcte
        if user_answer == correct_answer:
             label_acess_f7.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
             label_acess_f7.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
             mon_label_img_f7.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
        else:
            label_denied_f7.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
            label_denied_f7.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
            mon_label_img1_f7.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")  
    except ValueError:
           label_denied_f7.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
           label_denied_f7.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
           mon_label_img1_f7.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")  




# Fonctions Utiles
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = int((screen_width - width) / 2)
    y_position = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x_position}+{y_position}") 

def clear_entries_f7():
    
    global label_numbers
    
    # Régénérer les nombres aléatoires
    generate_numbers()
    # Effacer la réponse précédente
    entry_answer.delete(0, tkinter.END)
    

    # Masquer les messages sans pour autant détruire leur context
    label_denied_f7.place_forget() 
    mon_label_img1_f7.place_forget()
    
    label_acess_f7.place_forget()
    mon_label_img_f7.place_forget()
#-----------------------------------------DEUXIEME FENETRE-----------------------------------------------------------------


def precedent():
    fenetre7.destroy()
    subprocess.run(['python', 'fenetre_6.py'])
    
    
def suivant():
    fenetre7.destroy()
    subprocess.run(['python', 'fenetre_8.py'])

#------------------------------------------------------------------------------------------------------------------
# Create the main window    
fenetre7 =customtkinter.CTk()
#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre7.title("dico_mathématique")
#fenetre2.geometry("1350x750")
fenetre7.resizable(width=False, height=False)

generate_numbers()

center_window(fenetre7, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f6 = ImageTk.PhotoImage(Image.open("font7.png"))

img_f7 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f7 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f7=tkinter.Label(fenetre7, image=img_f7, bg="#EAAC14")
mon_label_img1_f7=tkinter.Label(fenetre7, image=img1_f7, bg="#EAAC14", font=("Comic sans Ms", 18, ""),justify="left")
#mon_label_img.pack()
background_label_f7 = tkinter.Label(fenetre7, image=image_f6)
background_label_f7.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f7 = tkinter.Label(fenetre7, fg='white')
label_denied_f7 = tkinter.Label(fenetre7, fg='#AA2822')

# Variables pour les opérations
operation_addition = tkinter.BooleanVar()
operation_soustraction = tkinter.BooleanVar()
operation_multiplication = tkinter.BooleanVar()
operation_division = tkinter.BooleanVar()

# Créer les éléments d'interface utilisateur
label_operation = tkinter.Label(fenetre7, text="Choisir l'opération:",font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
checkbox_addition = tkinter.Checkbutton(fenetre7, text="Addition", variable=operation_addition,font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
checkbox_soustraction = tkinter.Checkbutton(fenetre7, text="Soustraction", variable=operation_soustraction,font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
checkbox_multiplication = tkinter.Checkbutton(fenetre7, text="Multiplication", variable=operation_multiplication,font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
checkbox_division = tkinter.Checkbutton(fenetre7, text="Division", variable=operation_division ,font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")


# Placer les éléments dans la grille
label_operation.place(x=250, y=320)
checkbox_addition.place(x=300, y=390)
checkbox_soustraction.place(x=460, y=390)
checkbox_multiplication.place(x=660, y=390)
checkbox_division.place(x=880, y=390)

#--------------------------------------------------
# Générer un nombre aléatoire entre 1 et 100
random_number = random.randint(1, 100)

# Variables pour stocker les entrées utilisateur
user_input = tkinter.StringVar()
result_label = tkinter.StringVar()

# Créer les éléments d'interface utilisateur
label_numbers = tkinter.Label(fenetre7, text=f"Effectue les opérations sur les nombres suivant: \n\n Nombre1 : {num1}\tNombre2 : {num2}", font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
label_numbers.place(x=300, y=80)

label_entry_answer = tkinter.Label(fenetre7, text="Entrez le résultat:", font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left")
entry_answer  = tkinter.Entry(fenetre7, textvariable=user_input, font=("Comic Sans Ms",18, ""), bg="#FDFBFB",justify="left",highlightthickness=1, highlightbackground="orange")


#-------------------------------------------------------------------------
label_entry_answer.place(x="310", y="500",)
entry_answer.place(x="560", y="500",)

# Create a label to display the question
question4_labe_f7 = tkinter.Label(fenetre7, text="3- Trouvez les données parasites pour ce problème:", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")

# Create a button to check the answers
check_button_f7 = customtkinter.CTkButton(fenetre7, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f7.place(x=1050, y=380)

# Create a button to check the answers
check_button_f7 = customtkinter.CTkButton(fenetre7, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f7.place(x=1050, y=380)

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
check_button_f7.lift()

fenetre7.mainloop()
