'''
act2 = while loop
row = 5
col = 5

****
   *
   *
   *
****
'''
#act3
'''
*****
****
***
**
*   *
**
***
****
*****
'''


'''
Developer: Ghaizar A. Bautista
Title: for and while Activity
'''
import os
os.system("cls")
##############################################################
def help():
    print("""\
Command:
        
     -clear                    Clear terminal
     -exit                     Exit code
""")
##############################################################
def activity1(x):
    xf = x.strip()
    revxf = ""
    for i in xf:
        revxf = i+revxf
    if xf == revxf: 
        print("This word is Palindrome")
    else:
        print("This word is Not Palindrome")


def activity2(x):
    xf = x.split(",")
    row = int(xf[0])
    col = int(xf[1]) -1

    print("*" * col) # Top row
    
    row_count = 2 
    while row_count <= row - 1:
        print(' ' * (col-1) + '*') # Middle rows
        row_count += 1
    print("*" * col) # Bottom row

def activity3(rows):
    rows = int(rows)
    
    # Print descending pyramid
    for i in range(rows, 0, -1):
        print("*" * i)
    
    # Print ascending pyramid
    for i in range(2, rows + 1):
        print("*" * i + )

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