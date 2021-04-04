import random

name = input("Type your name here: ")
name_to_guess = random.rand(0, 10)

while(True):
    guess = input("Guess my number: ")
        if int(guess) > name_to_guess:
            print("Too high")
        if int(guess) < name_to_guess:
            print("Too low")
        if int(guess) == name_to_guess:
            print(f"You are so smart, {name}")
            break
