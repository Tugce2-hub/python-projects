# Rock Paper Scissors

import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)

if user_choice not in choices:
    print("Invalid choice!")
elif user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors")
    or (user_choice == "paper" and computer_choice == "rock")
    or (user_choice == "scissors" and computer_choice == "paper")
):
    print("You win!")
else:
    print("You lose!")
