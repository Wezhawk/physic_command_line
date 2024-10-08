#This program is a basic command line interface that can read and write files

import socket
import getpass
import platform
import os
from urllib.request import urlretrieve
from urllib.request import urlopen

print("Welcome to the Physic Command Line command line\n\n")
print("Compiled for Windows using Pyinstaller\n")
print("Copyright 2024 Wezhawk\n\n\n\n")
username = input("Please enter your username or leave blank to use your current sign in: ")
if len(username) == 0:
    username = os. getlogin()
    if len(username) == 0:
        username == os.path.expanduser()
        if len(username) == 0:
            username == os.environ.get()
            if len(username) == 0:
                username == getpass.getuser()
                if len(username) == 0:
                    print("Error in fetching username! Using default\n")
                    username == "user"
computer = input("Please enter your computer's name or leave blank to use your current computer name: ")
if len(computer) == 0:
    computer = platform.node()
    if len(computer) == 0: 
        os.environ['COMPUTERNAME']
        if len(computer) == 0:
            socket.gethostname()
            if len(computer) == 0:
                print("Error in fetching computer name! Using default\n")
                computer = "computer"

print("\nThank you, starting now\n\n\n\n")
def command_handler(prompt):
    if prompt == "":
        return
    # Create Command
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
        if prompt[7:] == " " or prompt[7:] == "":
            print("Please specify filename!")
            return
        filename = prompt[7:] + ".txt"
        if os.path.exists(filename):
            print("File already exists!")
            return
        f = open(filename, "x")
        f.close()
        print("Successfully created " + filename)
        return
    # Delete Command
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
        if prompt[7:] == " " or prompt[7:] == "":
            print("Please specify filename!")
            return
        filename = prompt[7:] + ".txt"
        if os.path.exists(filename):
            os.remove(filename)
            print(filename + " was deleted")
            return
        else:
            print("File does not exist!")
            return
    # Edit Command
    if "edit" in prompt:
        #If --help or -h argument is given
        if prompt[5:] == "-h" or prompt[5:] == "--help":
            print("\nEdit Command Help:\n\nEnter the edit command followed by a mode and filename argument to edit files\nMode arguments include:\n\n-a or --append or --add to add/append a line to a file\n\nExamples:\n  'edit -a myfile'\n\nNote: A .txt file extension will automatically be added to the filename\nNote: File will be created if it does not exist\n\n")
            return
        if prompt[5:] == "" or prompt[5] == " ":
            print("Please specify argument!\nUse command 'edit -h' for more info")
            return
        # If --append argument given        
        if "--append" in prompt[5:]:
            if prompt[13:] == "":
                print("Please specify filename!")
                return
            if prompt[14:] == "":
                print("Please specify filename!")
                return
            filename = prompt[14:] + ".txt"
            lineToAppend = input("Please enter the line you would to add/append: ")
            if len(lineToAppend) == 0:
                lineToAppend = input("Add/Append must contain at least 1 characters. Please try again: ")
                if len(lineToAppend) == 0:
                    lineToAppend = input("Add/Append must contain at least 1 characters. Please try again: ")
                    if len(lineToAppend) == 0:
                        lineToAppend = input("Add/Append must contain at least 1 characters. Please try again: ")
                        if len(lineToAppend) == 0:
                            print("Exiting Command!\n")
                            return
            if not os.path.isfile(filename):
                print("File does not exist!")
                return
            else:
                f = open(filename, "a")
                f.write(lineToAppend + "\n")
                f.close()
                print(lineToAppend + " was added/appended to " + filename)
                return
        # If --add argument given
        elif "--add" in prompt[5:]:
            if prompt[10:] == "":
                print("Please specify filename!")
                return
            if prompt[11:] == "":
                print("Please specify filename!")
                return
            filename = prompt[11:] + ".txt"
            lineToAppend = input("Please enter the line you would to add/append: ")
            if len(lineToAppend) == 0:
                lineToAppend = input("Add/Append must contain at least 1 characters. Please try again: ")
                if len(lineToAppend) == 0:
                    lineToAppend = input("Add/Append must contain at least 1 characters. Please try again: ")
                    if len(lineToAppend) == 0:
                        lineToAppend = input("Add/Append must contain at least 1 characters. Please try again: ")
                        if len(lineToAppend) == 0:
                            print("Exiting Command!\n")
                            return
            if not os.path.isfile(filename):
                print("File does not exist!")
                return
            else:
                f = open(filename, "a")
                f.write(lineToAppend + "\n")
                f.close()
                print(lineToAppend + " was added/appended to " + filename)
                return
        # If -a argument given
        elif "-a" in prompt[5:]:
            if prompt[7:] == "":
                print("Please specify filename!")
                return
            if prompt[8:] == "":
                print("Please specify filename!")
                return
            filename = prompt[8:] + ".txt"
            lineToAppend = input("Please enter the line you would to add/append: ")
            if len(lineToAppend) == 0:
                lineToAppend = input("Add/Append must contain at least 1 characters. Please try again: ")
                if len(lineToAppend) == 0:
                    lineToAppend = input("Add/Append must contain at least 1 characters. Please try again: ")
                    if len(lineToAppend) == 0:
                        lineToAppend = input("Add/Append must contain at least 1 characters. Please try again: ")
                        if len(lineToAppend) == 0:
                            print("Exiting Command!\n")
                            return
            if not os.path.isfile(filename):
                print("File does not exist!")
                return
            else:
                f = open(filename, "a")
                f.write(lineToAppend + "\n")
                f.close()
                print(lineToAppend + " was added/appended to " + filename)
                return
        else:
            if prompt[5] != "":
                print("Please specify argument!\nUse command 'edit -h' for more info")
                return
        if prompt[4] != " ":
            print("Command not recognized!")
            return
    # Install Command
    if prompt[:7] == "install":
        if prompt[8:] == "-h" or prompt[8:] == "--help":
            print("\nInstall Command Help:\n\nEnter the install command followed by a package name argument to install additional modules\n\nNote: You must have an active internet connection to use the install command")
            return
        else:
            packageToInstall = prompt[8:]
            if packageToInstall == "" or packageToInstall == " ":
                print("Please enter a package name!")
                return
            packageToInstall = packageToInstall + ".py"
            url = "https://wezhawk.github.io/physic_command_line_packages/" + packageToInstall
            print("Searching for " + packageToInstall + " in primary package repo at " + url)
            downloadFilename = "packages/" + packageToInstall
            try: 
                urlopen(url)
            except:
                print("Package does not exist!")
            else:
                print("Package found")
                install = input("Are you sure you want to install? (y/n): ")
                if install == "y":
                    try:
                        if not os.path.exists("packages"):
                            os.makedirs("packages")
                        if not os.path.exists("packages/packages_list"):
                            f = open("packages/packages_list", "x")
                            f.close()
                            print("Successfully created package list file")
                        if os.path.exists(downloadFilename):
                            print("Package already installed!")
                            return
                        print("\nProceeding with installation\n")
                        print("Downloading file...\n")
                        urlretrieve(url, downloadFilename)
                        f = open("packages/packages_list", "a")
                        f.write(packageToInstall)
                        f.close()
                    except Exception as e: 
                        print("Error!: ")
                        print(e)
                    else:
                        print("Successfully installed and downloaded!")
                    return
                else:
                    print("Aborting install!")
        return
    # Exit Command
    if prompt == "exit":
        print("Script Terminating!!!\n")
        exit()
    else:
        print("Command not recognized!")
        return
while True:
    prompt = input(username + "@" + computer + "> ")
    command_handler(prompt)
