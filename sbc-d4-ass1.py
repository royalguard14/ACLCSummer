'''
Developer: Ghaizar A. Bautista
Title: Ma-iba-Panalo (Remodify and Documented)
Note: Kung gagamit ka ng code ko
        wag mong alisin to. :)
'''
from random import randint as com # Import randint from random module and alias it as com
import os
os.system('cls')
def selected(x,y,z):
    selection = ["Unfold","Fold"] # List of possible selections
    return selection[x],selection[y],selection[z] # Return selections based on indices
def procces(p1,c1,c2):
    if all(p1 != x for x in [c1, c2]) : return "Player 1 wins" # Check if player 1's choice is unique
    elif all(c1 != x for x in [p1, c2]) : return "Computer 1 wins" # Check if computer 1's choice is unique
    elif all(c2 != x for x in [p1, c1]) : return "Computer 2 wins" # Check if computer 2's choice is unique
    else:return "DRAW!!!"  # If no unique choices, it's a draw
try:
    p1 = int(input('''
        0 - for Unfold
        1 - for Fold
        Select your number: ''')) # Prompt player for their selection and convert it to an integer
    if p1 not in [0, 1]: # Validate if input is within the allowed range
        print("Invalid Selection") # Print error message if input is invalid
    else:
        c1, c2= com(0,1), com(0,1) # Generate random choices for computer 1 and computer 2
        player, com1, com2 = selected(p1,c1,c2) # Get the selections based on choices
        print(f"P1 = {player}\nC1 = {com1}\nC2 = {com2}\n") # Print the selections of player, computer 1, and computer 2
        print(procces(p1,c1,c2)) # Determine and print the result of the game
except ValueError: # Handle invalid input that cannot be converted to an integer
    print("Invalid type input!") # Print error message for invalid input type
    
#Documentation of Functions:
"""
for Def Selection(x,y,z)
    Return the selection for player and computers based on their choices.
Args:
    x (int): Choice of player 1 (0 for Unfold, 1 for Fold).
    y (int): Choice of computer 1 (0 for Unfold, 1 for Fold).
    z (int): Choice of computer 2 (0 for Unfold, 1 for Fold).
Returns:
    tuple: A tuple containing the selections of player, computer 1, and computer 2.
"""
"""
for Def procces(p1,c1,c2):
    Determine the winner based on the choices of player and computers.
Args:
    p1 (int): Choice of player 1.
    c1 (int): Choice of computer 1.
    c2 (int): Choice of computer 2.
Returns:
    str: Result indicating which player/computer wins or if it's a draw.
"""