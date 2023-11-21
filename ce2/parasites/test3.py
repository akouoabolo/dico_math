import tkinter as tk
from tkinter import messagebox

# Créez une fonction pour vérifier les réponses
def check_answers():
    answer1 = entry1.get().strip()
    answer2a = entry2a.get().strip()
    answer2b = entry2b.get().strip()
    answer3 = entry3.get().strip()

    if (
        answer1 == "one hundred thirty" and
        answer2a == "meter" and
        answer2b == "1" and
        answer3 == "2000"
    ):
        messagebox.showinfo("Congratulations", "You got all the answers right! Well done!")
    else:
        messagebox.showerror("Try Again", "Sorry, please check your answers and try again.")

# Créez la fenêtre principale
root = tk.Tk()
root.title("Math Exercises")

# Créez la première frame pour le premier exercice
exercise1_frame = tk.LabelFrame(root, text="Exercice 1")
exercise1_frame.grid(row=0, column=0, padx=10, pady=10)

problem1_label = tk.Label(exercise1_frame, text="Votre père souhaite créer un potager sur un espace de 195 m de long dans sa concession. Pour ce faire, il achète 60 plans d’oranger, 30 plans de manguier et 40 plans d’avocatier. Il donne 2000 frs au vendeur. De retour au domicile, il s'aperçoit qu'il a oublié de prendre sa différence et vous commissionne. Il veut écrire le nombre total de projets en lettres mais il se trompe.", wraplength=250)
problem1_label.pack()

question1_label = tk.Label(exercise1_frame, text="Question 1: Écrivez le nombre total de plans en lettres :")
question1_label.pack()
entry1 = tk.Entry(exercise1_frame)
entry1.pack()

question2_label = tk.Label(exercise1_frame, text="Question 2: Les orangers et les manguiers sont séparés par 1 barrage les uns des autres.")
question2_label.pack()
question2a_label = tk.Label(exercise1_frame, text="a - Quelle unité de mesure de longueur doit-on utiliser pour mesurer cette distance ?")
question2a_label.pack()
entry2a = tk.Entry(exercise1_frame)
entry2a.pack()
question2b_label = tk.Label(exercise1_frame, text="b - Trouvez la longueur qui sépare les orangers et les manguiers :")
question2b_label.pack()
entry2b = tk.Entry(exercise1_frame)
entry2b.pack()

question3_label = tk.Label(exercise1_frame, text="Question 3: Trouvez les données parasites pour ce problème:")
question3_label.pack()
entry3 = tk.Entry(exercise1_frame)
entry3.pack()

check_button = tk.Button(exercise1_frame, text="Check Answers", command=check_answers)
check_button.pack()

# Créez une deuxième frame pour le deuxième exercice
exercise2_frame = tk.LabelFrame(root, text="Exercice 2")
exercise2_frame.grid(row=0, column=1, padx=10, pady=10)

# Ajoutez les éléments de l'exercice 2 (à personnaliser selon vos besoins)

root.mainloop()
