import random

"""
Rock: 1
Paper: 2
Scissors: 3
"""

def game(x):
    cpus_choice = random.randint(1, 3)
    if player_choice == "rock" and cpus_choice == 1:
        print("Rock, draw")
    elif player_choice == "rock" and cpus_choice == 2:
        print("Paper, lose")
    elif player_choice == "rock" and cpus_choice == 3:
        print("Scissors, win")
    elif player_choice == "paper" and cpus_choice == 1:
        print("Rock, win")
    elif player_choice == "paper" and cpus_choice == 2:
        print("Paper, draw")
    elif player_choice == "paper" and cpus_choice == 3:
        print("Scissors, lose")
    elif player_choice == "scissors" and cpus_choice == 1:
        print("Rock, lose")
    elif player_choice == "scissors" and cpus_choice == 2:
        print("Paper, win")
    elif player_choice == "scissors" and cpus_choice == 3:
        print("Scissors, draw")
    else:
        print("Invalid input")

while True:
    player_choice = input("Choose rock, paper or scissors: ")
    game(player_choice)
    stop = input("Continue?(Y/N) ")
    if stop == "Y":
        pass
    elif stop == "N":
        break
