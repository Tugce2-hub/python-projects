# Number Guessing Game

import random

secret_number = random.randint(1, 10)
attempts = 0

print("Guess the number between 1 and 10!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You found the number.")
        print("Attempts:", attempts)
        break
