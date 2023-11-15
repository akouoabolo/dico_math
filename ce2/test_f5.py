import tkinter as tk

def ask_question(question, correct_answer):
    user_answer = tk.StringVar()

    def check_answer():
        answer = user_entry.get()
        if answer == correct_answer:
            result_label.config(text="Congratulations!")
        else:
            result_label.config(text="Incorrect answer. Try again.")

    question_label = tk.Label(root, text=question)
    question_label.pack()

    user_entry = tk.Entry(root, textvariable=user_answer)
    user_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=check_answer)
    submit_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

root = tk.Tk()
root.title("Geometry Quiz")

ask_question("What is the measure of a right angle? ", "90")
ask_question("What is the measure of a flat angle? ", "180")
ask_question("What is the measure of an obtuse angle? ", "120")
ask_question("What is the measure of an acute angle? ", "30")

root.mainloop()
