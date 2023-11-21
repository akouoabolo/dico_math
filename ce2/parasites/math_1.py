import tkinter as tk
import random

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

def retry():
    # Réinitialiser les champs de saisie
    km_entry.delete(0, tk.END)
    hm_entry.delete(0, tk.END)
    dam_entry.delete(0, tk.END)
    m_entry.delete(0, tk.END)
    dm_entry.delete(0, tk.END)
    cm_entry.delete(0, tk.END)
    mm_entry.delete(0, tk.END)
    
value = generate_random_number()
unit = generate_random_unit()

def check_answers(km_correct, hm_correct, dam_correct, m_correct, dm_correct, cm_correct, mm_correct):
    global value  # Ajout de cette ligne pour indiquer que vous utilisez la variable globale 'value'
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
        result_label.config(text="Bravo! Toutes les réponses sont correctes.")
    else:
        result_label.config(text="Désolé, au moins une des réponses est incorrecte. Veuillez réessayer.")

    

# Création de la fenêtre
window = tk.Tk()
window.geometry('400x400')
window.title('Convertisseur d\'unités')

# Génération des nombres aléatoires et des unités de mesure
km_correct = convert_to_km(value, unit)
hm_correct = convert_to_hm(value, unit)
dam_correct = convert_to_dam(value, unit)
m_correct = convert_to_meters(value, unit)
dm_correct = convert_to_dm(value, unit)
cm_correct = convert_to_cm(value, unit)
mm_correct = convert_to_mm(value, unit)

# Ajout du code pour afficher le nombre aléatoire et son unité
random_number_label = tk.Label(window, text=f"Convertir le nombre {value} {unit} ")
random_number_label.grid(column=0, row=9, columnspan=2)

# Création des champs de saisie
km_entry = tk.Entry(window, width=10)
hm_entry = tk.Entry(window, width=10)
dam_entry = tk.Entry(window, width=10)
m_entry = tk.Entry(window, width=10)
dm_entry = tk.Entry(window, width=10)
cm_entry = tk.Entry(window, width=10)
mm_entry = tk.Entry(window, width=10)

# Placement des champs de saisie
km_entry.grid(column=1, row=0)
hm_entry.grid(column=1, row=1)
dam_entry.grid(column=1, row=2)
m_entry.grid(column=1, row=3)
dm_entry.grid(column=1, row=4)
cm_entry.grid(column=1, row=5)
mm_entry.grid(column=1, row=6)

# Création des étiquettes
tk.Label(window, text='km').grid(column=0, row=0)
tk.Label(window, text='hm').grid(column=0, row=1)
tk.Label(window, text='dam').grid(column=0, row=2)
tk.Label(window, text='m').grid(column=0, row=3)
tk.Label(window, text='dm').grid(column=0, row=4)
tk.Label(window, text='cm').grid(column=0, row=5)
tk.Label(window, text='mm').grid(column=0, row=6)

# Ajout du code pour afficher les bonnes réponses
correct_answers_label = tk.Label(
    window,
    text=f"Réponses correctes : km = {km_correct}, hm = {hm_correct}, dam = {dam_correct}, m = {m_correct}, "
         f"dm = {dm_correct}, cm = {cm_correct}, mm = {mm_correct}",
)
correct_answers_label.grid(column=10, row=0, columnspan=2)

# Bouton pour vérifier les réponses
# Création du bouton de vérification
check_button = tk.Button(window, text="Vérifier les réponses", command=lambda: check_answers(km_correct, hm_correct, dam_correct, m_correct, dm_correct, cm_correct, mm_correct))
check_button.grid(column=1, row=7)

# Bouton pour réessayer
retry_button = tk.Button(window, text="Réessayer", command=retry)
retry_button.grid(column=1, row=8)

# Étiquette pour afficher le résultat
result_label = tk.Label(window, text="", fg='black')
result_label.grid(column=0, row=9, columnspan=2)

# Lancement de la boucle principale de la fenêtre
window.mainloop()
