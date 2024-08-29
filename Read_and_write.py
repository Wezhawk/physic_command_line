print("Welcome to the listing command line\n\n")
print("Compiled for Windows using Pyinstaller, and installation program created with actual installer\n\n\n")
print("Copyright 2024 Everett Carrington\n\n\n\n")
username = input("Please enter your username: ")
if len(username) == 0:
    username = input("Please try again: ")
    if len(username) == 0:
        username = input("Please try again: ")
        if len(username) == 0:
            username = input("Please try again: ")
            if len(username) == 0:
                print("Script Terminating!!!")
                exit
computer = input("Please enter your computer's name: ")
if len(computer) == 0:
    computer = input("Please try again: ")
    if len(computer) == 0:
        computer = input("Please try again: ")
        if len(computer) == 0:
            computer = input("Please try again: ")
            if len(computer) == 0:
                print("Script Terminating!!!")
                exit
print("Thank you, starting now\n\n\n\n")
def command_handler(prompt):
    if prompt == "":
        print("\n")
    if print(prompt[:5]) == "create":
        if prompt[6:] == "":
            print("Please specify filename!")
            return
        filename = prompt[7:] + ".txt"
while True:
    prompt = input(username + "@" + computer + "> ")
    command_handler(prompt)
