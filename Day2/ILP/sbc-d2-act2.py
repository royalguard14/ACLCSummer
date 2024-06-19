from random import randint as com
import os
os.system('cls')

p1 = int( input("1 - for Fold  \n2 - for Unfold \n Select your number: "))
c1, c2= com(0,1),com(0,1)

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


if (p1 > 1) or (p1< 0):
    print("Invalid Selection")
else:
    player, com1, com2 = selected(p1,c1,c2)
    print(f"P1 = {player}\nC1 = {com1}\nC2 = {com2}\n")
    print(procces(p1,c1,c2))

