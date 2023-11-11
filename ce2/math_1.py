import random

def convert_to_meters(value, unit):
    if unit == 'km':
        return value * 1000
    elif unit == 'dm':
        return value / 10
    elif unit == 'cm':
        return value / 100
    elif unit == 'mm':
        return value / 1000
    else:
        return value

def play_game():
    target_values = [random.randint(1, 100) for _ in range(5)]
    units = ['dm', 'km', 'dm', 'cm', 'mm']

    for i in range(5):
        guess = float(input(f"Enter your guess in {units[i]} for the number {target_values[i]}: "))
        guess_meters = convert_to_meters(guess, units[i])

        if guess_meters == target_values[i]:
            print("Well done! You found it!")
        else:
            print("Try again!")
            retry = input("Would you like to try again? (yes/no): ")
            if retry.lower() != "yes":
                print("Better luck next time!")
                return

    print("Congratulations! You found all the numbers!")

play_game()