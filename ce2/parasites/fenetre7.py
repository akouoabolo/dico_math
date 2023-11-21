import tkinter as tk
from tkinter import messagebox
import random

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
        label_numbers = tk.Label(root, text="")
        label_numbers.grid(row=0, column=0, columnspan=2, pady=10)

    # Mettre à jour le texte du label avec les nouveaux nombres
    label_numbers.config(text=f"Nombre 1: {num1}\nNombre 2: {num2}")

def check_answer():
    try:
        user_answer = int(entry_answer.get())
        
        # Vérifier quelle opération a été sélectionnée
        if operation_addition.get():
            correct_answer = num1 + num2
        elif operation_soustraction.get():
            correct_answer = num1 - num2
        elif operation_multiplication.get():
            correct_answer = num1 * num2
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner une opération.")
            return

        # Comparer la réponse de l'utilisateur avec la réponse correcte
        if user_answer == correct_answer:
            result_label.config(text="Bravo!")
        else:
            result_label.config(text="Désolé, il faut recommencer.")
    except ValueError:
        result_label.config(text="Veuillez entrer un nombre valide.")

def reset_operation():
    entry_answer.delete(0, tk.END)
    result_label.config(text="")
    generate_numbers()

# Créer la fenêtre principale
root = tk.Tk()
root.title("Opérations Mathématiques")

# Générer les nombres initiaux
generate_numbers()

# Variables pour les opérations
operation_addition = tk.BooleanVar()
operation_soustraction = tk.BooleanVar()
operation_multiplication = tk.BooleanVar()

# Créer les éléments d'interface utilisateur
label_operation = tk.Label(root, text="Choisir l'opération:")
checkbox_addition = tk.Checkbutton(root, text="Addition", variable=operation_addition)
checkbox_soustraction = tk.Checkbutton(root, text="Soustraction", variable=operation_soustraction)
checkbox_multiplication = tk.Checkbutton(root, text="Multiplication", variable=operation_multiplication)

label_answer = tk.Label(root, text="Réponse:")
entry_answer = tk.Entry(root)
button_check = tk.Button(root, text="Vérifier", command=check_answer)
button_reset = tk.Button(root, text="Réinitialiser", command=reset_operation)
result_label = tk.Label(root, text="")

# Placer les éléments dans la grille
label_operation.grid(row=1, column=0, pady=10)
checkbox_addition.grid(row=1, column=1)
checkbox_soustraction.grid(row=1, column=2)
checkbox_multiplication.grid(row=1, column=3)

label_answer.grid(row=2, column=0, pady=10)
entry_answer.grid(row=2, column=1, pady=10)
button_check.grid(row=3, column=0, columnspan=4, pady=10)
button_reset.grid(row=4, column=0, columnspan=4, pady=10)
result_label.grid(row=5, column=0, columnspan=4, pady=10)

# Lancer la boucle principale
root.mainloop()
