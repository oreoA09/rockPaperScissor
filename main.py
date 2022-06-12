# Instructions:

# Create a new Python file and call it main.py. Inside it you'll create your game.
# Create a list to store all possible options:
# "R" for "rock", 
# "P" for "paper", 
# "S" for "scissors".

# When the program is run, ask the user to pick an option between "R", "P" or "S"
# If user input is invalid (not amongst our options), print an error, and ask for their input again (should be a loop)
# Use the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).
# Print both player's moves in the format: `Player (Rock) : CPU (Paper)`
# Check both player's moves: 
# If there is a winner, print the winner, and the program ends. 
# If it's a tie (the computer and player pick the same move), restart the game from step 3

import random

def play():
    print("Get Ready To Play RockPaperScissor")
    user = input("What's your choice? R for rock, P for paper. S for scissors\n")
    user = user.lower()

    if (user == "r") or (user == "s") or (user == "p"):
        print('Great choice!')
        # Computer's selection
        computer = random.choice(['r', 'p', 's'])

        # Figuring out who wins
        if user == computer:
            return "Player ({}) : CPU ({}) \n It's a tie!".format(user, computer)

        if user_wins(user, computer):
            return "Player ({}) : CPU ({}) \n You won!".format(user, computer)

        return "Player ({}) : CPU ({}) \n You lost :(".format(user, computer)
    else:
        print("Your input is invalid. Try again!!\n")

def user_wins(player, opponent):
    # rules: R > S, S > P, P > R
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'): 
        return True
    return False

print(play())

check = input("Would you like to play again?? Y/N \n")
check = check.lower()

if check == "y":
    print(play())
else:
    print("Goodbye!! :)")

