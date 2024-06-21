'''
Developer: Ghaizar A. Bautista
Title: Ma-iba-Panalo
Note: Kung gagamit ka ng code ko
        wag mong alisin to. :)
'''
from random import randint as com
import os
os.system('cls')

def selected(x,y,z):
    selection = ["Unfold","Fold"]
    return selection[x],selection[y],selection[z]

def procces(p1,c1,c2):
    if p1 != c1 and p1 != c2:
        return "Player 1 win"
    elif c1 != p1 and c1 != c2:
        return "Computer 1 win"
    elif c2 != p1 and c2 != c1:
        return "Computer 2 win"
    else:
        return "DRAW!!!"

try:
    p1 = int(input('''
        0 - for Unfold
        1 - for Fold
        Select your number: '''))

    c1, c2= com(0,1), com(0,1)

    if (p1 > 1) or (p1< 0):
        print("Invalid Selection")
    else:
        player, com1, com2 = selected(p1,c1,c2)
        print(f"P1 = {player}\nC1 = {com1}\nC2 = {com2}\n")
        print(procces(p1,c1,c2))
    
except ValueError as e:
    print("Invalid type input!")