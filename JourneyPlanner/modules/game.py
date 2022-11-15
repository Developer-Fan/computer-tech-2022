import random  # For computer randomised choice
from .questions import *  # For easier input from the user


def game(event):
    wins = 0
    losses = 0
    draws = 0
    # Reset the scores
    while True:
        # Will repeat until user says that the weather is not stormy
        avaliableChoices = ["scissors", "paper", "rock"]  # Choices avaliable
        q = question("What tool", avaliableChoices)
        ans = q.ask()
        randomNum = round(random.randint(0, 2))
        utensil = avaliableChoices[randomNum]
        # Computer randomises a number between 0 and 2, and then chooses the
        # corresponding tool
        if ans == "scissors":
            if utensil == "rock":
                print("You lost!")
                losses += 1
            elif utensil == "paper":
                print("You won!")
                wins += 1
            else:
                print("Draw!")
                draws += 1
        elif ans == "paper":
            if utensil == "rock":
                print("You won!")
                wins += 1
            elif utensil == "paper":
                print("Draw!")
                draws += 1
            else:
                print("Losses!")
                losses += 1
        else:
            if utensil == "rock":
                print("Draw!")
                draws += 1
            elif utensil == "scissors":
                print("You won!")
                wins += 1
            else:
                print("You lost!")
                losses += 1
        # The above decides who wins, and adds to the score
        print(f"You picked {ans} and the computer picked {utensil}.")
        # Tells the user what they picked and what the computer picked
        print(
            f"You won {wins} times, lost {losses} times, and drawed {draws} times."
        )
        # Tells the user their score
        # Asks if the weather is still stormy
        q2 = question("Is it still "+event, ["y", "n"])
        ans = q2.ask()
        if ans == "n":
            print("")
            break  # Break from the loop if the weather is not stormy
        else:
            print("")  # Print a new line if it is still stormy
