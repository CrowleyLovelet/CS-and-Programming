import random

def generate_secret_number():
    digits = list(range(10))
    secret_number = ""
    for _ in range(4):
        index = int(random.randint(0, len(digits) - 1))
        secret_number += str(digits.pop(index))
    return secret_number

def count_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def bulls_and_cows():
    while True:  
        secret_number = generate_secret_number()
        attempts = 0
        print("This is a guesing game. Try to gues a 4 dig number that i thought of. No repeating digits")

        while True:
            guess = ""
            
            while True:
                guess = input("Enter your guess: ")
                if len(guess) == 4:
                    valid = True
                    for ch in guess:
                        if ch not in "0123456789":
                            valid = False
                            break
                    for i in range(4):
                        for j in range(i + 1, 4):
                            if guess[i] == guess[j]:
                                valid = False
                                break
                    if valid:
                        break
                print("Invalid input. Do you know how numbers look?")

            attempts += 1
            bulls, cows = count_bulls_and_cows(secret_number, guess)
            print(f"Bulls: {bulls}, Cows: {cows}")

            if bulls == 4:
                print(f"Congrats! You took forever: you've guesed number {secret_number} in {attempts} tries.")
                break

            if attempts >= 5:
                print(f"Hahaha u loooooose! The number was {secret_number}.")
                break

        again = input("Do you want to play again? (yes/no/y/n): ").strip().lower()
        if again not in ("yes", "y"):
            print("Goodbye!")
            break
bulls_and_cows()

