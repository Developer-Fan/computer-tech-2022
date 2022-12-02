import tkinter  # Just for the GUI
import random  # For the computer's choice
import time  # For the delay
import winsound  # For the sound
import json  # For user data, e.g username & highscore
import os  # Clear screens
import Modules.funcs as functions

# Prepare the user information
with open("./user.json", "r") as f:
    user = json.load(f)

# Detect if user has registered
if user["username"] == "":
    username = input("Register your username: ")
    user["username"] = username
    if len(username) > 15:
        user["username"] = username[:15]
    with open("./user.json", "w") as f:
        json.dump(user, f)
else:
    username = user["username"]
highscore = {"classic": 0, "king": 0, "parallel": 0}
highscore["classic"] = user["hi-c"]
highscore["king"] = user["hi-k"]
highscore["parallel"] = user["hi-p"]

# Set up defaults
def_font = ("Courier New", 20)
sec_def_font = ("Courier New", 15)
margin = 20
button_margin = 30
appelements = {}  # Dict array to store app elements

# Create window
window = tkinter.Tk()
window.title("Scissors Paper Rock Spock Lizard")
# Icon
window.iconbitmap("./Assets/Visual/icon.ico")
window.geometry("500x350")
window.resizable(False, False)


def clear():
    for i in appelements:
        appelements[i].destroy()


images = {
    "exit": tkinter.PhotoImage(file="./Assets/Visual/button1.png"),
    "back": tkinter.PhotoImage(file="./Assets/Visual/button2.png"),
    "submit": tkinter.PhotoImage(file="./Assets/Visual/button3.png"),
    "next": tkinter.PhotoImage(file="./Assets/Visual/next.png"),
    "new_game": tkinter.PhotoImage(file="./Assets/Visual/new_game.png"),
    "user_prof": tkinter.PhotoImage(file="./Assets/Visual/user_profile.png"),
    "how_to": tkinter.PhotoImage(file="./Assets/Visual/how_to.png"),
    "new_game1": tkinter.PhotoImage(file="./Assets/Visual/game1.png"),
    "new_game2": tkinter.PhotoImage(file="./Assets/Visual/game2.png"),
    "new_game3": tkinter.PhotoImage(file="./Assets/Visual/game3.png"),
    "rock": tkinter.PhotoImage(file="./Assets/Visual/rock.png"),
    "paper": tkinter.PhotoImage(file="./Assets/Visual/paper.png"),
    "scissors": tkinter.PhotoImage(file="./Assets/Visual/scissors.png"),
    "spock": tkinter.PhotoImage(file="./Assets/Visual/spock.png"),
    "lizard": tkinter.PhotoImage(file="./Assets/Visual/lizard.png"),
    "instructions": tkinter.PhotoImage(file="./Assets/Visual/instructions.png")
}

user_selections = {
    "rock": 0,
    "scissors": 0,
    "paper": 0,
    "lizard": 0,
    "spock": 0
}


def classic_game():
    for i in user_selections:
        user_selections[i] = 1
    var = appelements["input"].get()
    clear()
    try:
        rounds = int(var)
    except:
        rounds = 5
    if rounds < 1:
        rounds = 1
    elif rounds > 50:
        rounds = 50
    # Now play game
    # Set up defaults
    wins = 0
    losses = 0
    ties = 0
    currentround = 1
    classic_stat1(currentround, rounds, wins, losses, ties)


def classic_stat1(current, total, wins, losses, ties):
    clear()
    if current > total:
        # Display end screen
        string = f"Game over!"
        strlen = functions.calcLetters(string)
        appelements["end_label"] = tkinter.Label(text=string, font=def_font)
        appelements["end_label"].place(x=((500-strlen)/2), y=margin)

        string = f"You won {wins} times,"
        strlen = functions.cCalcLetters(string, 15)
        appelements["wins_label"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["wins_label"].place(x=((500-strlen)/2), y=margin+40)

        string = f"lost {losses} times,"
        strlen = functions.cCalcLetters(string, 15)
        appelements["losses_label"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["losses_label"].place(x=((500-strlen)/2), y=margin+30*2+10)

        string = f"and tied {ties} times."
        strlen = functions.cCalcLetters(string, 15)
        appelements["ties_label"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["ties_label"].place(x=((500-strlen)/2), y=margin+30*3+10)

        winner = False

        if wins > losses:
            string = f"In total, {username} won,"
            strlen = functions.cCalcLetters(string, 15)
            # wins/total*100
            winrate = round(wins/total*100, 2)
            winner = True
        elif wins < losses:
            string = f"In total, computer won,"
            strlen = functions.cCalcLetters(string, 15)
            winrate = round(losses/total*100, 2)
        else:
            string = f"In total, it was a tie,"
            strlen = functions.cCalcLetters(string, 15)
            winrate = 50.00
        appelements["winrate_label1"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["winrate_label1"].place(
            x=((500-strlen)/2), y=margin+30*4+10)
        string = f"with a winrate of {winrate}%."
        strlen = functions.cCalcLetters(string, 15)
        appelements["winrate_label2"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["winrate_label2"].place(
            x=((500-strlen)/2), y=margin+30*5+10)

        appelements["back"] = tkinter.Button(
            window,
            image=images["back"],
            command=lambda: startScreen(),
            borderwidth=0
        )

        appelements["back"].place(x=500-75-margin, y=350-30-margin)

        if total >= 5 and winner:
            # Save score
            if highscore["classic"] < winrate:
                highscore["classic"] = winrate
                functions.write_to_user_data("hi-c", winrate)
    else:
        # Display round number
        string = f"Round {current}/{total}"
        strlen = functions.calcLetters(string)
        appelements["round_label"] = tkinter.Label(text=string, font=def_font)
        appelements["round_label"].place(x=((500-strlen)/2), y=margin)
        string = f"Choose your weapon."
        strlen = functions.calcLetters(string)
        appelements["choose_label"] = tkinter.Label(text=string, font=def_font)
        appelements["choose_label"].place(x=((500-strlen)/2), y=margin+50)
        # Display buttons
        appelements["rock"] = tkinter.Button(
            window,
            image=images["rock"],
            command=lambda: classic_stat2(
                "rock", current, total, wins, losses, ties),
            borderwidth=0
        )
        appelements["rock"].place(x=margin, y=margin+120)
        appelements["paper"] = tkinter.Button(
            window,
            image=images["paper"],
            command=lambda: classic_stat2(
                "paper", current, total, wins, losses, ties),
            borderwidth=0
        )
        appelements["paper"].place(x=margin+95, y=margin+120)
        appelements["scissors"] = tkinter.Button(
            window,
            image=images["scissors"],
            command=lambda: classic_stat2(
                "scissors", current, total, wins, losses, ties),
            borderwidth=0
        )
        appelements["scissors"].place(x=margin+190, y=margin+120)
        appelements["spock"] = tkinter.Button(
            window,
            image=images["spock"],
            command=lambda: classic_stat2(
                "spock", current, total, wins, losses, ties),
            borderwidth=0
        )
        appelements["spock"].place(x=margin+285, y=margin+120)
        appelements["lizard"] = tkinter.Button(
            window,
            image=images["lizard"],
            command=lambda: classic_stat2(
                "lizard", current, total, wins, losses, ties),
            borderwidth=0
        )
        appelements["lizard"].place(x=margin+380, y=margin+120)
        appelements["back"] = tkinter.Button(
            window,
            image=images["back"],
            command=lambda: startScreen(),
            borderwidth=0
        )

        appelements["back"].place(x=500-75-margin, y=350-30-margin)


def classic_stat2(weapon, current, total, wins, losses, ties):

    results = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "spock": ["rock", "scissors"],
        "lizard": ["paper", "spock"]
    }

    user_sum = 0

    for i in user_selections:
        user_sum += user_selections[i]

    ran_num = random.randint(1, user_sum)

    a = user_selections["rock"]
    b = user_selections["scissors"]
    c = user_selections["paper"]
    d = user_selections["lizard"]
    e = user_selections["spock"]

    if ran_num >= 1 and ran_num <= a:
        computer_choice = random.choice(["rock", "paper", "spock"])
    elif ran_num > a and ran_num <= a+b:
        computer_choice = random.choice(["scissors", "rock", "spock"])
    elif ran_num > a+b and ran_num <= a+b+c:
        computer_choice = random.choice(["paper", "scissors", "lizard"])
    elif ran_num > a+b+c and ran_num <= a+b+c+d:
        computer_choice = random.choice(["lizard", "spock", "rock"])
    else:
        computer_choice = random.choice(["paper", "spock", "scissors"])
    clear()
    # Display round number
    string = f"Results for round {current}/{total}"
    strlen = functions.calcLetters(string)
    appelements["round_label"] = tkinter.Label(text=string, font=def_font)
    appelements["round_label"].place(x=((500-strlen)/2), y=margin)
    # Display player choice
    string = f"You chose {weapon}."
    strlen = functions.calcLetters(string)
    appelements["player_choice"] = tkinter.Label(text=string, font=def_font)
    appelements["player_choice"].place(x=((500-strlen)/2), y=margin+50)
    # Display computer choice
    string = f"The computer chose {computer_choice}."
    strlen = functions.calcLetters(string)
    appelements["computer_choice"] = tkinter.Label(text=string, font=def_font)
    appelements["computer_choice"].place(x=((500-strlen)/2), y=margin+100)
    # Display result
    current += 1
    if weapon == computer_choice:
        string = "You tied!"
        ties += 1
    elif computer_choice in results[weapon]:
        string = "You won!"
        wins += 1
    else:
        string = "You lost!"
        losses += 1
    strlen = functions.calcLetters(string)
    appelements["result"] = tkinter.Label(text=string, font=def_font)
    appelements["result"].place(x=((500-strlen)/2), y=margin+150)
    # Display buttons
    appelements["next"] = tkinter.Button(
        window,
        image=images["next"],
        command=lambda: classic_stat1(current, total, wins, losses, ties),
        borderwidth=0
    )
    appelements["next"].place(x=(500-100)/2, y=margin+200)
    appelements["back"] = tkinter.Button(
        window,
        image=images["back"],
        command=lambda: startScreen(),
        borderwidth=0
    )
    appelements["back"].place(x=500-75-margin, y=350-30-margin)


def parallel_game():
    for i in user_selections:
        user_selections[i] = 1
    var = appelements["input"].get()
    clear()
    try:
        rounds = int(var)
    except:
        rounds = 5
    if rounds < 1:
        rounds = 1
    elif rounds > 50:
        rounds = 50
    # Now play game
    # Set up defaults
    wins = 0
    losses = 0
    ties = 0
    currentround = 1
    parallel_stat_1(currentround, rounds, wins, losses, ties)


def parallel_stat_1(current, total, wins, losses, ties):
    clear()
    if current > total:
        # Display end screen
        string = f"Game over!"
        strlen = functions.calcLetters(string)
        appelements["end_label"] = tkinter.Label(text=string, font=def_font)
        appelements["end_label"].place(x=((500-strlen)/2), y=margin)

        string = f"You won {wins} times,"
        strlen = functions.cCalcLetters(string, 15)
        appelements["wins_label"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["wins_label"].place(x=((500-strlen)/2), y=margin+40)

        string = f"lost {losses} times,"
        strlen = functions.cCalcLetters(string, 15)
        appelements["losses_label"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["losses_label"].place(x=((500-strlen)/2), y=margin+30*2+10)

        string = f"and tied {ties} times."
        strlen = functions.cCalcLetters(string, 15)
        appelements["ties_label"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["ties_label"].place(x=((500-strlen)/2), y=margin+30*3+10)

        winner = False

        if wins > losses:
            string = f"In total, {username} won,"
            strlen = functions.cCalcLetters(string, 15)
            winrate = round(wins/total*100, 2)
            winner = True
        elif wins < losses:
            string = f"In total, computer won,"
            strlen = functions.cCalcLetters(string, 15)
            winrate = round(losses/total*100, 2)
        else:
            string = f"In total, it was a tie,"
            strlen = functions.cCalcLetters(string, 15)
            winrate = 50.00
        appelements["winrate_label1"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["winrate_label1"].place(
            x=((500-strlen)/2), y=margin+30*4+10)
        string = f"with a winrate of {winrate}%."
        strlen = functions.cCalcLetters(string, 15)
        appelements["winrate_label2"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["winrate_label2"].place(
            x=((500-strlen)/2), y=margin+30*5+10)

        appelements["back"] = tkinter.Button(
            window,
            image=images["back"],
            command=lambda: startScreen(),
            borderwidth=0
        )

        appelements["back"].place(x=500-75-margin, y=350-30-margin)

        if total >= 5 and winner:
            # Save score
            if highscore["parallel"] < winrate:
                highscore["parallel"] = winrate
                functions.write_to_user_data("hi-p", winrate)
    else:
        # Display round number
        string = f"Round {current}/{total}"
        strlen = functions.calcLetters(string)
        appelements["round_label"] = tkinter.Label(text=string, font=def_font)
        appelements["round_label"].place(x=((500-strlen)/2), y=margin)
        string = f"Choose your weapon."
        strlen = functions.calcLetters(string)
        appelements["choose_label"] = tkinter.Label(text=string, font=def_font)
        appelements["choose_label"].place(x=((500-strlen)/2), y=margin+50)
        # Display buttons
        appelements["rock"] = tkinter.Button(
            window,
            image=images["rock"],
            command=lambda: parallel_stat_2(
                "rock", current, total, wins, losses, ties),
            borderwidth=0
        )
        appelements["rock"].place(x=margin, y=margin+120)
        appelements["paper"] = tkinter.Button(
            window,
            image=images["paper"],
            command=lambda: parallel_stat_2(
                "paper", current, total, wins, losses, ties),
            borderwidth=0
        )
        appelements["paper"].place(x=margin+95, y=margin+120)
        appelements["scissors"] = tkinter.Button(
            window,
            image=images["scissors"],
            command=lambda: parallel_stat_2(
                "scissors", current, total, wins, losses, ties),
            borderwidth=0
        )
        appelements["scissors"].place(x=margin+190, y=margin+120)
        appelements["spock"] = tkinter.Button(
            window,
            image=images["spock"],
            command=lambda: parallel_stat_2(
                "spock", current, total, wins, losses, ties),
            borderwidth=0
        )
        appelements["spock"].place(x=margin+285, y=margin+120)
        appelements["lizard"] = tkinter.Button(
            window,
            image=images["lizard"],
            command=lambda: parallel_stat_2(
                "lizard", current, total, wins, losses, ties),
            borderwidth=0
        )
        appelements["lizard"].place(x=margin+380, y=margin+120)
        appelements["back"] = tkinter.Button(
            window,
            image=images["back"],
            command=lambda: startScreen(),
            borderwidth=0
        )

        appelements["back"].place(x=500-75-margin, y=350-30-margin)


def parallel_stat_2(weapon, current, total, wins, losses, ties):

    results = {
        "rock": ["paper", "spock"],
        "paper": ["scissors", "lizard"],
        "scissors": ["rock", "spock"],
        "spock": ["lizard", "paper"],
        "lizard": ["scissors", "paper"]
    }

    user_sum = 0

    for i in user_selections:
        user_sum += user_selections[i]

    ran_num = random.randint(1, user_sum)

    a = user_selections["rock"]
    b = user_selections["scissors"]
    c = user_selections["paper"]
    d = user_selections["lizard"]
    e = user_selections["spock"]

    if ran_num >= 1 and ran_num <= a:
        computer_choice = random.choice(["rock", "lizard", "scissors"])
    elif ran_num > a and ran_num <= a+b:
        computer_choice = random.choice(["scissors", "paper", "lizard"])
    elif ran_num > a+b and ran_num <= a+b+c:
        computer_choice = random.choice(["paper", "rock", "spock"])
    elif ran_num > a+b+c and ran_num <= a+b+c+d:
        computer_choice = random.choice(["lizard", "scissors", "paper"])
    else:
        computer_choice = random.choice(["spock", "rock", "lizard"])
    clear()
    # Display round number
    string = f"Results for round {current}/{total}"
    strlen = functions.calcLetters(string)
    appelements["round_label"] = tkinter.Label(text=string, font=def_font)
    appelements["round_label"].place(x=((500-strlen)/2), y=margin)
    # Display player choice
    string = f"You chose {weapon}."
    strlen = functions.calcLetters(string)
    appelements["player_choice"] = tkinter.Label(text=string, font=def_font)
    appelements["player_choice"].place(x=((500-strlen)/2), y=margin+50)
    # Display computer choice
    string = f"The computer chose {computer_choice}."
    strlen = functions.calcLetters(string)
    appelements["computer_choice"] = tkinter.Label(text=string, font=def_font)
    appelements["computer_choice"].place(x=((500-strlen)/2), y=margin+100)
    # Display result
    current += 1
    if weapon == computer_choice:
        string = "You tied!"
        ties += 1
    elif computer_choice in results[weapon]:
        string = "You won!"
        wins += 1
    else:
        string = "You lost!"
        losses += 1
    strlen = functions.calcLetters(string)
    appelements["result"] = tkinter.Label(text=string, font=def_font)
    appelements["result"].place(x=((500-strlen)/2), y=margin+150)
    # Display buttons
    appelements["next"] = tkinter.Button(
        window,
        image=images["next"],
        command=lambda: parallel_stat_1(current, total, wins, losses, ties),
        borderwidth=0
    )
    appelements["next"].place(x=(500-100)/2, y=margin+200)
    appelements["back"] = tkinter.Button(
        window,
        image=images["back"],
        command=lambda: startScreen(),
        borderwidth=0
    )
    appelements["back"].place(x=500-75-margin, y=350-30-margin)


def points_game():
    for i in user_selections:
        user_selections[i] = 1
    var = appelements["input"].get()
    clear()
    try:
        rounds = int(var)
    except:
        rounds = 5
    if rounds < 1:
        rounds = 1
    elif rounds > 25:
        rounds = 25
    # Now play game
    # Set up defaults
    wins = 0
    losses = 0
    ties = 0
    points_stat_1(0, 0, rounds, wins, losses, ties, 1, 0)


def points_stat_1(computer, player, points, wins, losses, ties, current, total):
    clear()
    if computer == points or player == points:
        # Display end screen
        string = f"Game over!"
        strlen = functions.calcLetters(string)
        appelements["end_label"] = tkinter.Label(text=string, font=def_font)
        appelements["end_label"].place(x=((500-strlen)/2), y=margin)

        string = f"You won {wins} times,"
        strlen = functions.cCalcLetters(string, 15)
        appelements["wins_label"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["wins_label"].place(x=((500-strlen)/2), y=margin+40)

        string = f"lost {losses} times,"
        strlen = functions.cCalcLetters(string, 15)
        appelements["losses_label"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["losses_label"].place(x=((500-strlen)/2), y=margin+30*2+10)

        string = f"and tied {ties} times."
        strlen = functions.cCalcLetters(string, 15)
        appelements["ties_label"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["ties_label"].place(x=((500-strlen)/2), y=margin+30*3+10)

        winner = False

        if wins > losses:
            string = f"In total, {username} won,"
            strlen = functions.cCalcLetters(string, 15)
            winrate = round(wins/total*100, 2)
            winner = True
        elif wins < losses:
            string = f"In total, computer won,"
            strlen = functions.cCalcLetters(string, 15)
            winrate = round(losses/total*100, 2)
        else:
            string = f"In total, it was a tie,"
            strlen = functions.cCalcLetters(string, 15)
            winrate = 50.00
        appelements["winrate_label1"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["winrate_label1"].place(
            x=((500-strlen)/2), y=margin+30*4+10)
        string = f"with a winrate of {winrate}%."
        strlen = functions.cCalcLetters(string, 15)
        appelements["winrate_label2"] = tkinter.Label(
            text=string, font=sec_def_font)
        appelements["winrate_label2"].place(
            x=((500-strlen)/2), y=margin+30*5+10)

        appelements["back"] = tkinter.Button(
            window,
            image=images["back"],
            command=lambda: startScreen(),
            borderwidth=0
        )

        appelements["back"].place(x=500-75-margin, y=350-30-margin)
        if total >= 5 and winner:
            # Save score
            if highscore["king"] < winrate:
                highscore["king"] = winrate
                functions.write_to_user_data("hi-k", winrate)
    else:
        # Display round number
        string = f"Round {current}"
        strlen = functions.calcLetters(string)
        appelements["round_label"] = tkinter.Label(text=string, font=def_font)
        appelements["round_label"].place(x=((500-strlen)/2), y=margin)
        string = f"Choose your weapon."
        strlen = functions.calcLetters(string)
        appelements["choose_label"] = tkinter.Label(text=string, font=def_font)
        appelements["choose_label"].place(x=((500-strlen)/2), y=margin+50)
        # Display buttons
        appelements["rock"] = tkinter.Button(
            window,
            image=images["rock"],
            command=lambda: points_stat_2(
                "rock", computer, player, points, wins, losses, ties, current, total),
            borderwidth=0
        )
        appelements["rock"].place(x=margin, y=margin+120)
        appelements["paper"] = tkinter.Button(
            window,
            image=images["paper"],
            command=lambda: points_stat_2(
                "paper", computer, player, points, wins, losses, ties, current, total),
            borderwidth=0
        )
        appelements["paper"].place(x=margin+95, y=margin+120)
        appelements["scissors"] = tkinter.Button(
            window,
            image=images["scissors"],
            command=lambda: points_stat_2(
                "scissors", computer, player, points, wins, losses, ties, current, total),
            borderwidth=0
        )
        appelements["scissors"].place(x=margin+190, y=margin+120)
        appelements["spock"] = tkinter.Button(
            window,
            image=images["spock"],
            command=lambda: points_stat_2(
                "spock", computer, player, points, wins, losses, ties, current, total),
            borderwidth=0
        )
        appelements["spock"].place(x=margin+285, y=margin+120)
        appelements["lizard"] = tkinter.Button(
            window,
            image=images["lizard"],
            command=lambda: points_stat_2(
                "lizard", computer, player, points, wins, losses, ties, current, total),
            borderwidth=0
        )
        appelements["lizard"].place(x=margin+380, y=margin+120)
        appelements["back"] = tkinter.Button(
            window,
            image=images["back"],
            command=lambda: startScreen(),
            borderwidth=0
        )

        appelements["back"].place(x=500-75-margin, y=350-30-margin)


def points_stat_2(weapon, computer, player, points, wins, losses, ties, current, total):
    total += 1
    results = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "spock": ["rock", "scissors"],
        "lizard": ["paper", "spock"]
    }

    user_sum = 0

    for i in user_selections:
        user_sum += user_selections[i]

    ran_num = random.randint(1, user_sum)

    a = user_selections["rock"]
    b = user_selections["scissors"]
    c = user_selections["paper"]
    d = user_selections["lizard"]
    e = user_selections["spock"]

    if ran_num >= 1 and ran_num <= a:
        computer_choice = random.choice(["rock", "paper", "spock"])
    elif ran_num > a and ran_num <= a+b:
        computer_choice = random.choice(["scissors", "rock", "spock"])
    elif ran_num > a+b and ran_num <= a+b+c:
        computer_choice = random.choice(["paper", "scissors", "lizard"])
    elif ran_num > a+b+c and ran_num <= a+b+c+d:
        computer_choice = random.choice(["lizard", "spock", "rock"])
    else:
        computer_choice = random.choice(["paper", "spock", "scissors"])
    clear()
    # Display round number
    string = f"Results for round {current}"
    strlen = functions.calcLetters(string)
    appelements["round_label"] = tkinter.Label(text=string, font=def_font)
    appelements["round_label"].place(x=((500-strlen)/2), y=margin)
    # Display player choice
    string = f"You chose {weapon}."
    strlen = functions.calcLetters(string)
    appelements["player_choice"] = tkinter.Label(text=string, font=def_font)
    appelements["player_choice"].place(x=((500-strlen)/2), y=margin+30)
    # Display computer choice
    string = f"The computer chose {computer_choice}."
    strlen = functions.calcLetters(string)
    appelements["computer_choice"] = tkinter.Label(text=string, font=def_font)
    appelements["computer_choice"].place(x=((500-strlen)/2), y=margin+60)
    # Display result
    current += 1
    if weapon == computer_choice:
        string = "You tied!"
        ties += 1
        computer += 1
        player += 1
    elif computer_choice in results[weapon]:
        string = "You won!"
        wins += 1
        player += 1
    else:
        string = "You lost!"
        losses += 1
        computer += 1
    strlen = functions.calcLetters(string)
    appelements["result"] = tkinter.Label(text=string, font=def_font)
    appelements["result"].place(x=((500-strlen)/2), y=margin+90)

    string = f"You've now got {player} points."
    strlen = functions.calcLetters(string)
    appelements["yove"] = tkinter.Label(text=string, font=def_font)
    appelements["yove"].place(x=((500-strlen)/2), y=margin+120)

    string = f"Computer's now got {computer} points."
    strlen = functions.calcLetters(string)
    appelements["comve"] = tkinter.Label(text=string, font=def_font)
    appelements["comve"].place(x=((500-strlen)/2), y=margin+150)

    # Display buttons
    appelements["next"] = tkinter.Button(
        window,
        image=images["next"],
        command=lambda: points_stat_1(
            computer, player, points, wins, losses, ties, current, total),
        borderwidth=0
    )
    appelements["next"].place(x=(500-100)/2, y=margin+200)
    appelements["back"] = tkinter.Button(
        window,
        image=images["back"],
        command=lambda: startScreen(),
        borderwidth=0
    )
    appelements["back"].place(x=500-75-margin, y=350-30-margin)


def game(gamemode):
    clear()
    # Game based on gamemode, integer from 1 to 3
    if gamemode == 1 or gamemode == 3:
        label = "How many rounds to play?"
        strlen = functions.calcLetters(label)
        appelements["gamemode_label"] = tkinter.Label(
            text=label, font=def_font)
        appelements["gamemode_label"].place(x=((500-strlen)/2), y=margin)
        appelements["input"] = tkinter.Entry(window, font=def_font, width=28)
        appelements["input"].place(x=20, y=75)
        if gamemode == 1:
            appelements["submit"] = tkinter.Button(
                window,
                text="Submit",
                image=images["submit"],
                font=def_font,
                command=lambda: classic_game(),
                borderwidth=0
            )
        else:
            appelements["submit"] = tkinter.Button(
                window,
                text="Submit",
                image=images["submit"],
                font=def_font,
                command=lambda: parallel_game(),
                borderwidth=0
            )
        appelements["submit"].place(x=(500-100)/2, y=120)
        appelements["back"] = tkinter.Button(
            window,
            image=images["back"],
            command=lambda: startScreen(),
            borderwidth=0
        )
        appelements["back"].place(x=500-75-margin, y=350-30-margin)
        pass
    elif gamemode == 2:
        label = "How many points to win?"
        strlen = functions.calcLetters(label)
        appelements["gamemode_label"] = tkinter.Label(
            text=label, font=def_font)
        appelements["gamemode_label"].place(x=((500-strlen)/2), y=margin)
        appelements["input"] = tkinter.Entry(window, font=def_font, width=28)
        appelements["input"].place(x=20, y=75)
        appelements["submit"] = tkinter.Button(
            window,
            text="Submit",
            image=images["submit"],
            font=def_font,
            command=lambda: points_game(),
            borderwidth=0
        )
        appelements["submit"].place(x=(500-100)/2, y=120)
        appelements["back"] = tkinter.Button(
            window,
            image=images["back"],
            command=lambda: startScreen(),
            borderwidth=0
        )
        appelements["back"].place(x=500-75-margin, y=350-30-margin)
        pass


def new_game():
    clear()

    appelements["back"] = tkinter.Button(
        window,
        image=images["back"],
        command=lambda: startScreen(),
        borderwidth=0
    )

    appelements["back"].place(x=500-75-margin, y=350-30-margin)

    appelements["game1"] = tkinter.Button(
        window,
        image=images["new_game1"],
        command=lambda: game(1),
        borderwidth=0
    )

    appelements["game1"].place(x=20, y=75)

    appelements["game2"] = tkinter.Button(
        window,
        image=images["new_game2"],
        command=lambda: game(2),
        borderwidth=0
    )

    appelements["game2"].place(x=(500-150)/2, y=75)

    appelements["game3"] = tkinter.Button(
        window,
        image=images["new_game3"],
        command=lambda: game(3),
        borderwidth=0
    )

    appelements["game3"].place(x=500-150-20, y=75)

    string = f"Choose your gamemode."
    strlen = functions.calcLetters(string)
    appelements["gamemode_label"] = tkinter.Label(text=string, font=def_font)
    appelements["gamemode_label"].place(x=((500-strlen)/2), y=margin)


def change_username():
    new_username = appelements["input"].get()
    if new_username == "":
        new_username = "Player"
    if len(new_username) > 15:
        new_username = new_username[:15]
    functions.write_to_user_data("username", new_username)
    user["username"] = new_username
    global username
    username = user["username"]
    user_prof()


def user_prof():
    clear()

    appelements["back"] = tkinter.Button(
        window,
        image=images["back"],
        command=lambda: startScreen(),
        borderwidth=0
    )

    appelements["back"].place(x=500-75-margin, y=350-30-margin)

    string = "Welcome to your profile!"
    strlen = functions.calcLetters(string)
    appelements["welcome"] = tkinter.Label(text=string, font=def_font)
    appelements["welcome"].place(x=((500-strlen)/2), y=margin)

    string = f"Your username is {username}."
    strlen = functions.calcLetters(string)
    appelements["username"] = tkinter.Label(text=string, font=def_font)
    appelements["username"].place(x=((500-strlen)/2), y=margin+40)

    appelements["input"] = tkinter.Entry(window, font=def_font, width=28)
    appelements["input"].place(x=20, y=95)

    appelements["submit"] = tkinter.Button(
        window,
        text="Submit",
        image=images["submit"],
        font=def_font,
        command=lambda: change_username(),
        borderwidth=0
    )

    appelements["submit"].place(x=(500-100)/2, y=140)

    string = "Highscores(winrates):"
    strlen = functions.calcLetters(string)
    appelements["highscores"] = tkinter.Label(text=string, font=def_font)
    appelements["highscores"].place(x=((500-strlen)/2), y=margin+180)

    appelements["highscoresc"] = tkinter.Label(
        text="Classic: "+str(highscore["classic"])+"%", font=sec_def_font
    )
    strlen = functions.cCalcLetters(
        appelements["highscoresc"].cget("text"), 15)
    appelements["highscoresc"].place(x=(500-strlen)/2, y=margin+220)

    appelements["highscoresk"] = tkinter.Label(
        text="King: "+str(highscore["king"])+"%", font=sec_def_font
    )
    strlen = functions.cCalcLetters(
        appelements["highscoresk"].cget("text"), 15)
    appelements["highscoresk"].place(x=(500-strlen)/2, y=margin+250)

    appelements["highscoresp"] = tkinter.Label(
        text="King: "+str(highscore["parallel"])+"%", font=sec_def_font
    )
    strlen = functions.cCalcLetters(
        appelements["highscoresp"].cget("text"), 15)
    appelements["highscoresp"].place(x=(500-strlen)/2, y=margin+280)


def how_to():
    clear()
    appelements["label1"] = tkinter.Button(
        window,
        image=images["instructions"],
        borderwidth=0
    )

    appelements["label1"].place(x=0, y=0)

    appelements["back"] = tkinter.Button(
        window,
        image=images["back"],
        command=lambda: startScreen(),
        borderwidth=0
    )

    appelements["back"].place(x=500-75-margin, y=350-30-margin)


def startScreen():
    clear()

    appelements["exit"] = tkinter.Button(
        window,
        text="Leave",
        image=images["exit"],
        command=lambda: window.quit(),
        borderwidth=0
    )

    appelements["exit"].place(x=500-75-margin, y=350-30-margin)

    appelements["new_game"] = tkinter.Button(
        window,
        text="New Game",
        image=images["new_game"],
        command=lambda: new_game(),
        borderwidth=0
    )

    appelements["new_game"].place(x=20, y=75)

    appelements["user_prof"] = tkinter.Button(
        window,
        text="New Game",
        image=images["user_prof"],
        command=lambda: user_prof(),
        borderwidth=0
    )

    appelements["user_prof"].place(x=500-150-20, y=75)

    appelements["how_to"] = tkinter.Button(
        window,
        text="New Game",
        image=images["how_to"],
        command=lambda: how_to(),
        borderwidth=0
    )

    appelements["how_to"].place(x=(500-150)/2, y=75)

    string = f"Welcome, {username}!"
    strlen = functions.calcLetters(string)
    appelements["welcome_label"] = tkinter.Label(text=string, font=def_font)
    appelements["welcome_label"].place(x=((500-strlen)/2), y=margin)


startScreen()

# Open window
window.mainloop()
