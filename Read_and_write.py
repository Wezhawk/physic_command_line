#This program is a basic command line interface that can read and write files

import os

print("Welcome to the listing command line\n\n")
print("Compiled for Windows using Pyinstaller, and installation program was created with Actual Installer\n")
print("Copyright 2024 Everett Carrington\n\n\n\n")
username = input("Please enter your username: ")
if len(username) == 0:
    username = input("Please try again: ")
    if len(username) == 0:
        username = input("Please try again: ")
        if len(username) == 0:
            username = input("Please try again: ")
            if len(username) == 0:
                print("Script Terminating!!!\n")
                exit()
computer = input("Please enter your computer's name: ")
if len(computer) == 0:
    computer = input("Please try again: ")
    if len(computer) == 0:
        computer = input("Please try again: ")
        if len(computer) == 0:
            computer = input("Please try again: ")
            if len(computer) == 0:
                print("Script Terminating!!!\n")
                exit()
print("\nThank you, starting now\n\n\n\n")
def command_handler(prompt):
    if prompt == "":
        print("\n")
        return
    if "create" in prompt:
        if prompt[7:] == "-h" or prompt[7:] == "--help":
            print("\nCreate Command Help:\n\nEnter the create command followed by a filename argument to make a new writable file\n\nExample: 'create myfile'\n\nNote: A .txt file extension will automatically be added to the filename\n\n")
            return        
        if prompt[6:] == "":
            print("Please specify filename!")
            return
        if prompt[6] != " ":
            print("Command not recognized!")
            return
        filename = prompt[7:] + ".txt"
        if os.path.exists(filename):
            print("File already exists!")
            return
        f = open(filename, "x")
        print("Successfully created " + filename)
        return
    if "delete" in prompt:
        if prompt[7:] == "-h" or prompt[7:] == "--help":
            print("\nDelete Command Help:\n\nEnter the delete command followed by a filename argument to delete a file\n\nExample: 'delete myfile'\n\nNote: A .txt file extension will automatically be added to the filename\n\n")
            return
        if prompt[6:] == "":
            print("Please specify filename!")
            return
        if prompt[6] != " ":
            print("Command not recognized!")
            return
        filename = prompt[7:] + ".txt"
        if os.path.exists(filename):
            os.remove(filename)
            print(filename + " was deleted")
            return
        else:
            print("File does not exist!")
            return
    if prompt == "exit":
        print("Script Terminating!!!\n")
        exit()
    else:
        print("Command not recognized!")
        return
while True:
    prompt = input(username + "@" + computer + "> ")
    command_handler(prompt)
