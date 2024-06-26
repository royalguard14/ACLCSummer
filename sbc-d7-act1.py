'''
Developer: Ghaizar A. Bautista
Title: MY BANK (Functions)
'''
import os
from random import randint
os.system("cls")
##############################################################
def help():
    print("""\
Command:
     create                   Create 1 user
     delete     [userID]       
     check      [userID]
     deposite   [userID]
     withdraw   [userID]
     data  
     clear                    Clear terminal
     exit                     Exit code
""")
    

##############################################################
data={}


def create():
    rid = randint(-1,10000)
    while rid not in data.keys():
        data[rid] = 1000

def check(x):
    xf = int(x.strip())
    if xf in data.keys(): 
        print(f'''
            ===BANK INFORMATION===
                User ID: {xf}
                Balance: {data[xf]}
    ''')
    else: print("User ID not Exist")

def delete(x):
    xf = x.strip()
    if xf in data.keys():
        data.pop(int(xf))

def display():
    for x,y in data.items():
        print(x,":",y)

def deposite(x):
    xf = int(x.strip())
    if xf in data.keys(): 
        dep = int(input("Amount: "))
        if dep < 0:
            print("Negative Value")
        else:
            data[xf] = data.get(xf) + dep
            print("Deposite Success!")
    else: print("User ID not Exist")

def withdraw(x):
    xf = int(x.strip())
    if xf in data.keys(): 
        dep = int(input("Amount: "))
        if dep < 0:
            print("Negative Value")
        else:
            if dep > data.get(xf):
                print("Insufficient funds")
            else:
                data[xf] = data.get(xf) - dep
                print("Withdraw Success!")

    else: print("User ID not Exist")

##############################################################

while True: 
    command = input("Command: ").lower().replace(" ","")
    if "help" in command: help() 
    elif "create" in command: create()
    elif "delete" in command: delete(command.replace("delete",""))
    elif "check" in command: check(command.replace("check",""))
    elif "deposite" in command: deposite(command.replace("deposite",""))
    elif "withdraw" in command: withdraw(command.replace("withdraw",""))
    elif "data" in command: display() 
    elif "clear" in command: os.system('cls') 
    elif "exit" in command: break   
    else: print("Command Invalid | use 'help command' ") 