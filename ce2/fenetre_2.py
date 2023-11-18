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
    
# Les fonctions de conversion

def convert_to_meters(value, unit):
    if unit == 'km':
        return value * 1000
    elif unit == 'hm':
        return value * 100
    elif unit == 'dam':
        return value * 10
    elif unit == 'm':
        return value
    elif unit == 'dm':
        return value / 10
    elif unit == 'cm':
        return value / 100
    elif unit == 'mm':
        return value / 1000
    else:
        return None

def convert_to_hm(value, unit):
    meters = convert_to_meters(value, unit)
    if meters is not None:
        return meters / 100
    else:
        return None

def convert_to_dam(value, unit):
    meters = convert_to_meters(value, unit)
    if meters is not None:
        return meters / 10
    else:
        return None

def convert_to_cm(value, unit):
    meters = convert_to_meters(value, unit)
    if meters is not None:
        return meters * 100
    else:
        return None

def convert_to_mm(value, unit):
    meters = convert_to_meters(value, unit)
    if meters is not None:
        return meters * 1000
    else:
        return None

def convert_to_km(value, unit):
    mm = convert_to_mm(value, unit)
    km = mm / 1e+6  # 1 million de millimètres équivaut à 1 kilomètre
    return km

def convert_to_dm(value, unit):
    meters = convert_to_meters(value, unit)
    if meters is not None:
        return meters * 10
    else:
        return None

# Fonction pour vérifier la réponse
def check_answer(value, unit, answer):
    meters = convert_to_meters(value, unit)
    return meters == answer
# Fonction pour générer un nombre aléatoire et une unité de mesure aléatoire
def generate_random_number():
    return random.randint(1, 200)

def generate_random_unit():
    units = ['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm']
    return random.choice(units)


value = generate_random_number()
unit = generate_random_unit()

km_correct = convert_to_km(value, unit)
hm_correct = convert_to_hm(value, unit)
dam_correct = convert_to_dam(value, unit)
m_correct = convert_to_meters(value, unit)
dm_correct = convert_to_dm(value, unit)
cm_correct = convert_to_cm(value, unit)
mm_correct = convert_to_mm(value, unit)



def check_answers():
    km_value = float(km_entry.get()) if km_entry.get() else 0
    hm_value = float(hm_entry.get()) if hm_entry.get() else 0
    dam_value = float(dam_entry.get()) if dam_entry.get() else 0
    m_value = float(m_entry.get()) if m_entry.get() else 0
    dm_value = float(dm_entry.get()) if dm_entry.get() else 0
    cm_value = float(cm_entry.get()) if cm_entry.get() else 0
    mm_value = float(mm_entry.get()) if mm_entry.get() else 0

    if (
          km_value == km_correct and
          hm_value == hm_correct and
          dam_value == dam_correct and
          m_value == m_correct and
          dm_value == dm_correct and
          cm_value == cm_correct and
          mm_value == mm_correct
      
    ):
        #result_label.config(text="Bravo! Toutes les réponses sont correctes.")
        
        label_acess_f2.config(text="Félicitations !!!", font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_acess_f2.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img_f2.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
    else:
       # result_label.config(text="Désolé, au moins une des réponses est incorrecte. Veuillez réessayer.")
        label_denied_f2.config(text='Oups! Vérifie \n tes réponses.', font=("Comic Sans Ms",20, "bold"), bg="#EAAC14")
        label_denied_f2.place(x=0, y=0, relx=0.86, rely=0.06, anchor="center")
        mon_label_img1_f2.place(x=0, y=0, relx=0.86, rely=0.72, anchor="center")
    





def clear_entries_f2():
    global value, unit, km_correct, hm_correct, dam_correct, m_correct, dm_correct, cm_correct, mm_correct
    # Réinitialiser les champs de saisie
    km_entry.delete(0, tkinter.END)
    hm_entry.delete(0, tkinter.END)
    dam_entry.delete(0, tkinter.END)
    m_entry.delete(0, tkinter.END)
    dm_entry.delete(0, tkinter.END)
    cm_entry.delete(0, tkinter.END)
    mm_entry.delete(0, tkinter.END)
    
    label_denied_f2.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img1_f2.place_forget()
    
    label_acess_f2.place_forget() # masquer les widgets sans pour autant détruire leur context!
    mon_label_img_f2.place_forget()
 
     # Réinitialiser les valeurs aléatoires et les réponses correctes
    value = generate_random_number()
    unit = generate_random_unit()
    km_correct = convert_to_km(value, unit)
    hm_correct = convert_to_hm(value, unit)
    dam_correct = convert_to_dam(value, unit)
    m_correct = convert_to_meters(value, unit)
    dm_correct = convert_to_dm(value, unit)
    cm_correct = convert_to_cm(value, unit)
    mm_correct = convert_to_mm(value, unit)
    
  # Afficher la nouvelle mesure à convertir
    random_number_label.config(text=f"Converti la mesure {value} {unit} en : ")  
    
# fonctions de précédent() et suivant()
def precedent():
    fenetre2.destroy()
    subprocess.run(['python', 'fenetre_1.py'])  
    
def suivant():
    fenetre2.destroy()
    subprocess.run(['python', 'fenetre_3.py'])  
    
# close function
def on_closing():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter?"):
        # Changer l'icône ou effectuer d'autres actions de fermeture
        fenetre2.iconbitmap("close.ico")
        fenetre2.destroy()

fenetre2 =customtkinter.CTk()

#fenetre2.iconbitmap("logo01.ico")
customtkinter.set_appearance_mode("light")
fenetre2.title("dico_mathématique")
fenetre2.resizable(width=False, height=False)


center_window(fenetre2, window_width, window_height) #position of windows2
# Create a Label widget and set the image as its background
image_f2 = ImageTk.PhotoImage(Image.open("font2.png"))


img_f2 = ImageTk.PhotoImage(Image.open("succes.png"))
img1_f2 = ImageTk.PhotoImage(Image.open("down.png"))

mon_label_img_f2=tkinter.Label(fenetre2, image=img_f2, bg="#EAAC14")
mon_label_img1_f2=tkinter.Label(fenetre2, image=img1_f2, bg="#EAAC14")
#mon_label_img.pack()

background_label_f2 = tkinter.Label(fenetre2, image=image_f2)
background_label_f2.place(x=0, y=0, relwidth=1, relheight=1)

label_acess_f2 = tkinter.Label(fenetre2, fg='white')
label_denied_f2 = tkinter.Label(fenetre2, fg='#AA2822')

# Création des champs de saisie
km_entry = tkinter.Entry(fenetre2, width=10, font=("Comic sans Ms", 18, ""), highlightthickness=1, highlightbackground="orange")
hm_entry = tkinter.Entry(fenetre2, width=10, font=("Comic sans Ms", 18, ""), highlightthickness=1, highlightbackground="orange")
dam_entry = tkinter.Entry(fenetre2, width=10, font=("Comic sans Ms", 18, ""), highlightthickness=1, highlightbackground="orange")
m_entry = tkinter.Entry(fenetre2, width=10, font=("Comic sans Ms", 18, ""), highlightthickness=1, highlightbackground="orange")
dm_entry = tkinter.Entry(fenetre2, width=10, font=("Comic sans Ms", 18, ""), highlightthickness=1, highlightbackground="orange")
cm_entry = tkinter.Entry(fenetre2, width=10, font=("Comic sans Ms", 18, ""), highlightthickness=1, highlightbackground="orange")
mm_entry = tkinter.Entry(fenetre2, width=10, font=("Comic sans Ms", 18, ""), highlightthickness=1, highlightbackground="orange")

# Placement des champs de saisie
km_entry.place(x=360, y=270)
hm_entry.place(x=360, y=340)
dam_entry.place(x=360, y=410)
m_entry.place(x=360, y=480)
dm_entry.place(x=360, y=550)
cm_entry.place(x=360, y=620)
mm_entry.place(x=360, y=690)

# Création des étiquettes
tkinter.Label(fenetre2, text='km', font=("Comic sans Ms", 18), bg="#FDFBFB").place(x=300, y=270)
tkinter.Label(fenetre2, text='hm', font=("Comic sans Ms", 18), bg="#FDFBFB").place(x=300, y=340)
tkinter.Label(fenetre2, text='dam', font=("Comic sans Ms", 18), bg="#FDFBFB").place(x=300, y=410)
tkinter.Label(fenetre2, text='m', font=("Comic sans Ms", 18), bg="#FDFBFB").place(x=300, y=480)
tkinter.Label(fenetre2, text='dm', font=("Comic sans Ms", 18), bg="#FDFBFB").place(x=300, y=550)
tkinter.Label(fenetre2, text='cm', font=("Comic sans Ms", 18), bg="#FDFBFB").place(x=300, y=620)
tkinter.Label(fenetre2, text='mm', font=("Comic sans Ms", 18), bg="#FDFBFB").place(x=300, y=690)



reponse_entry4_f2=tkinter.Label(fenetre2,text="")
reponse_entry4_f2.place(x=866, y=660)



# Create a button to check the answers
check_button_f2 = customtkinter.CTkButton(fenetre2, text="Vérifier les réponses", font=("Comic Sans Ms", 16), command=check_answers)
check_button_f2.place(x=1050, y=380)

# Create other widgets
label_text_f2 = tkinter.Label(fenetre2, text="Entre les bonnes valeurs de mesure dans les champs requis : \n ", font=("Comic sans Ms", 18, ""),bg="#FDFBFB",justify="left")
label_text_f2.place(x=0, y=0, relx=0.42, rely=0.15, anchor="center")

# Ajout du code pour afficher le nombre aléatoire et son unité
random_number_label = tkinter.Label(fenetre2, text=f"Converti la mesure  {value} {unit} en : ",  font=("Comic sans Ms", 18), bg="#FDFBFB")
random_number_label.place(x=300, y=160)

# Position other widgets


"""btn_quitter_f2 = customtkinter.CTkButton(fenetre2, text="Quitter", font=("Comic Sans Ms", 16), command=fenetre2.destroy)
btn_quitter_f2.place(x=1050, y=680)"""


# bouton suivant / précédent
bouton_precedent = customtkinter.CTkButton(fenetre2, text="<<", command=precedent, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_precedent.place(x=1049, y=698)

bouton_suivant = customtkinter.CTkButton(fenetre2, text=">>", command=suivant, width=3, font=("Comic Sans Ms", 19,"bold"))
bouton_suivant.place(x=1100, y=698)

#bouton de reset
reset_img_f2=ImageTk.PhotoImage(Image.open("reset_2.png"))
reset_img_label_f2=tkinter.Label(fenetre2, image=reset_img_f2)
 
# Create a button to clear the entries
clear_button_f2 = tkinter.Button(fenetre2, command=clear_entries_f2, image=reset_img_f2, bg="white", borderwidth=0, cursor="hand2" )
clear_button_f2.place(x=1290, y=0)


correct_answers_label = tkinter.Label(
    fenetre2,
    text=f"Réponses correctes : km = {km_correct}, hm = {hm_correct}, dam = {dam_correct}, m = {m_correct}, "
         f"dm = {dm_correct}, cm = {cm_correct}, mm = {mm_correct}"
)

print(f"km = {km_correct}, hm = {hm_correct}, dam = {dam_correct}, m = {m_correct}, "
      f"dm = {dm_correct}, cm = {cm_correct}, mm = {mm_correct}")

#je fais passer certains composants  au dessus du font canvas
label_acess_f2.lift()
label_denied_f2.lift()
mon_label_img_f2.lift()
mon_label_img1_f2.lift()

label_text_f2.lift()
#btn_quitter_f2.lift()
check_button_f2.lift()
reponse_entry4_f2.lift()

fenetre2.mainloop()