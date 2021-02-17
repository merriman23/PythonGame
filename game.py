# This is gonna be some pseudo code
# User Selection - get info from the user
# computer selection - rng either rock paper or scissors
# evaluate results
# declare a winner

import random


userSelection = input("What is your selection? (Rock, Paper, or Scissors)  : ")
# TODO validate user selection
print ("You chose", userSelection)
possibleChoices = ['Rock','Paper','Scissors']

# computer selection
computerSelection = random.choices(possibleChoices)
print('Computer chose', str(computerSelection))

# Evalutate results - conditional statement

if (userSelection == computerSelection):
    print ("You tied")
elif (userSelection == "Rock"):
    if computerSelection == "Paper":
        print("You lost")
    else:
        print("You won")
elif (userSelection == "Paper"):
    if computerSelection == "Scissors":
        print("You lost")
    else:
        print("You won")
elif (userSelection == "Scissors"):
    if computerSelection == "Rock":
        print("You lost")
    else:
        print("You won")


