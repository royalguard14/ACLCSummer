'''
Developer: Ghaizar A. Bautista
Title: for and while Activities
'''
import os
os.system("cls")
##############################################################
def help():
    print("""\
Command:
     act1 word|Sentence       Check if input is Palindrome or not.
     act2 row,col             Create a box with * based on row and col. 
     act3 row                 Create a ????????  
     clear                    Clear terminal
     exit                     Exit code
""")
##############################################################
def activity1(x):
    xf = x.strip().replace("word=","")
    revxf = ""
    for i in xf:
        revxf = i+revxf
    if xf == revxf: 
        print("This word is Palindrome")
    else:
        print("This word is Not Palindrome")


def activity2(x):
    xf = x.split(",")
    row,col = int(xf[0]),int(xf[1])
    print("*" * col) # Top row
    row_count = 2 
    while row_count <= row - 1:
        print( "*" +' ' * (col-2) + '*') # Middle rows
        row_count += 1
    print("*" * col) # Bottom row

def activity3(rows):
    rows = int(rows)
    for i in range(rows, 1, -1): #top side
        print("*" * i)

    print("*" + (" ") * (rows-2 ) + "*") #middle

    for i in range(2, rows + 1): #bot side
        print("*" * i)

##############################################################
while True: 
    command = input("Command: ").lower().replace(" ","") 
    if "act1" in command: activity1(command.replace("act1",""))
    elif "act2" in command: activity2(command.replace("act2",""))
    elif "act3" in command: activity3(command.replace("act3","")) 
    elif "help" in command: help()
    elif "clear" in command: os.system('cls') 
    elif "exit" in command: break   
    else: print("Command Invalid | use 'help command' ")  