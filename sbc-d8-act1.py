import os
from pathlib import Path
os.system("cls")

file_path = Path("data.txt")
islog = False
current_user = None
##############################################################
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def help():
    print("""\
Commands:
     login                    Log into your account
     register                 Register a new account
     change password          Change your account password
     logout                   Log out of your account
     clear                    Clear terminal screen
     exit                     Exit the application
     help                     Show available commands
""")
##############################################################
def file_check():
    if not file_path.exists():
        with open(file_path, 'w') as file:
            file.write("")

def open_file_dict():
    data_dict = {}
    with open(file_path, "r") as file:
        for line in file:
            parts = line.rstrip('\n').split(':')
            if len(parts) == 2:
                username, password = parts
                password = password.rstrip(',')
                data_dict[username] = password
    return data_dict

def username_exists(username):
    with open(file_path, "r") as file:
        for line in file:
            parts = line.rstrip('\n').split(':')
            if parts:
                existing_username = parts[0]
                if existing_username == username:
                    return True
    return False
##############################################################
def register(username, password):
    if username_exists(username):
        print(f"Username '{username}' already exists. Choose a different username.")
        return
    
    with open(file_path, "a") as file:
        file.write(f"{username}:{password},\n")
        print(f"User '{username}' registered successfully.")

def login():
    global islog, current_user
    if islog:
        print("You are already logged in.")
        return
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    data_dict = open_file_dict()

    if username in data_dict and data_dict[username] == password:
        islog = True
        current_user = username
        print(f"Welcome, {username}! You are now logged in.")
    else:
        print("Invalid username or password. Please try again.")

def change_password():
    global islog, current_user
    if not islog:
        print("You need to be logged in to change your password.")
        return
    
    if current_user:
        new_password = input("Enter your new password: ")
        with open(file_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for index, line in enumerate(lines):
                if line.startswith(f"{current_user}:"):
                    lines[index] = f"{current_user}:{new_password},\n"
            file.writelines(lines)
        print("Password updated successfully.")
    else:
        print("Invalid username or password. Password change failed.")
##############################################################
def logout():
    global islog, current_user
    if not islog:
        print("You are not logged in.")
        return
    islog = False
    current_user = None
    print("You have been logged out successfully.")
##############################################################
    
file_check()
while True:
    print("\nWelcome to Simple Login with File Handling\n")
    print(f"{'Change Password | Logout' if islog else 'Register | Login'}")

    action = input(">>>>> ").strip().lower()
    if action == "login":login()
    elif action == "register":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        register(username, password)
    elif action == "change password":change_password()
    elif action == "logout":logout()
    elif action == "clear":clear_screen()
    elif action == "exit":break
    elif action == "help":help()
    elif action == "display":print(open_file_dict())
    else:print("Invalid command. Please enter 'help' for a list of commands.")