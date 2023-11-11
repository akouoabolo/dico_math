def ask_question(question, correct_answer):
    while True:
        answer = input(question)
        if answer == correct_answer:
            print("Congratulations!")
            break
        else:
            print("Incorrect answer. Try again.")

ask_question("What is the measure of a right angle? ", "90")
ask_question("What is the measure of a flat angle? ", "180")
ask_question("What is the measure of an obtuse angle? ", "120")
ask_question("What is the measure of an acute angle? ", "30")