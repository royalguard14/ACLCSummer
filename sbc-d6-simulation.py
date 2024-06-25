'''
Developer: Ghaizar A. Bautista
Title: Loops
'''
import os
os.system("cls")
##############################################################
def help():
    print("""\
Command:
     -loop1                    Display list loop
     -loop2                    Display sting loop
     -loop3                    Display String array loop
     -loop4 x                  Display range(Start)
     -loop4 x,y                Display range(Start,End)
     -loop4 x,y,z              Display range(Start,End,Skip)
     -loop5 row                Display (*)(row)
     -while1                   Display while with arithmetic condition
     -while2 batman,akosiden   Display while with boolean         
     -clear                    Clear terminal
     -exit                     Exit code
""")
##############################################################
def forloop1():
    li = [0,1,2,3,4]
    for n in li:
        print(n)

def forloop2():
    string = "Hello world"
    for char in string:
        print(char)

def forloop3():
    li_ = ["z","a","r"] # put _ to identify as LIST,
    for obj in li_:
        print(obj)

def forloop4(x):
    xf = x.split(",")
    if len(xf) == 1: 
        for i in range(int(xf[0])): # range(start)
            print(i)
    elif len(xf) == 2:
        for i in range(int(xf[0]),int(xf[1])): # range(start,last)
            print(i)
    elif len(xf) == 3:
        for i in range(int(xf[0]),int(xf[1]),int(xf[2])): # range(start,last,skip)
            print(i)

def forloop5(row):
    for x in range(int(row) +1):
        print("*" * x)

##############################################################
def whileloop1():
    n = 0
    while n < 5:
        print(n)
        n += 1

def whileloop2(x):
    log = True
    while log:
        xf = x.split(",")
        username = xf[0]
        password = xf[1]
        print
        if username == "batman" and password == "akosiden":
            print("Successfully Login")
            log = False #stop while
            #break  #break statement 
        else:
            print("login Failed, Try again!\n")
            
##############################################################
while True: 
    command = input("Command: ").lower().replace(" ","") 
    if "while1" in command: whileloop1() 
    elif "while2" in command: whileloop2(command.replace("while2","")) 
    elif "loop1" in command: forloop1()
    elif "loop2" in command: forloop2()
    elif "loop3" in command: forloop3()
    elif "loop4" in command: forloop4(command.replace("loop4",""))
    elif "loop5" in command: forloop5(command.replace("loop5",""))
    elif "help" in command: help()
    elif "clear" in command: os.system('cls') 
    elif "exit" in command: break   
    else: print("Command Invalid | use 'help command' ")  