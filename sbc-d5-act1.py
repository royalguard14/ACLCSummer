'''
Developer: Ghaizar A. Bautista
Title: Basic Stack and Queue
Note: Kung gagamit ka ng code ko wag mong alisin to. :)
'''
import os
office = [] # initialize list
while True: # endless loop until exit command execute
    command = input("Command: ").lower().replace(" ","") # get the user command and filter the word 
    if "add" in command: # if the word add is in the inserted command
        fil1 = command.replace("add","") # string manipulation, removing the word add
        office.append(fil1) # add the number to list , from command add.
    elif "display" in command:print(office) # print the list
    elif "naa" in command: office.pop(0) #Queue Remove 
    elif "wala" in command: office.pop() #Stack Remove
    elif "clear" in command: os.system('cls') # clear terminal
    elif "exit" in command: break   #end the loop
    else: print("Command Invalid")  #other command






