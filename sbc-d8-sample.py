'''
Developer: Ghaizar A. Bautista
Title: file handling
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
    


def s1():
    lines = [line.strip() for line in open("txtfile.txt")]
    file1 = open("txtfile.txt", "r").read()
    file2 = open("txtfile.txt", "r").readlines()
    print("1-",lines, len(lines))
    print("2-",file1)
    print("3-",file2)

    


def s2(x):
    xf = x.strip()
    file = open("txtfile.txt", "w")
    file.write(xf)
    file.close()


while True: 
    command = input("Command: ").lower().replace(" ","") 
    if "help" in command: help()
    if "s1" in command: s1()
    if "s2" in command: s2(command.replace("s2",""))
    elif "clear" in command: os.system('cls') 
    elif "exit" in command: break   
    else: print("Command Invalid | use 'help command' ")  