'''
Developer: Ghaizar A. Bautista
Title: Basic String Manipulation
Note: Kung gagamit ka ng code ko wag mong alisin to. :)
'''
import os
office = []
while True:
    command = input("Command: ").lower().replace(" ","")
    if "add" in command:
        fil1 = command.replace("add","")
        office.append(fil1)
    elif "display" in command:print(office)
    elif "naa" in command: office.pop(0)
    elif "wala" in command: office.pop()
    elif "clear" in command: os.system('cls')
    elif "exit" in command: break
    else:
        print("Command Invalid")
        








