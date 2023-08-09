import os
import api 
'''
commands:
1. FIND : to find a particular word in the dictionary database
    e.g. FIND apple
2. LOC: to provide the absolute path of the database, if left empty considers the curret directory
    e.g. LOC "D:/codes/projects/oxford"
3. ADD: add the word to the database
    e.g. ADD apple
        -> description
        -> image_address
        -> source
4. UPDATE: update the word
    e.g. UPDATE apple
        -> new description
        -> NONE
        -> NONE
5. QUIT: close the CLI
    e.g. QUIT
6. CREATE: create a new database
    e.g. CREATE hindi_dictionary
        -> set location
'''
def find(word):
    wrd, des, img, src = api.find(word)
    if wrd != None:
        print()
        print("Word: {}".format(word.upper()))
        print("Description: {}".format(des))
        print("Image:{}".format(img))
        print("Source:{}".format(src))
    else:
        print("The word '{}' does not exist in the database, try adding".format(word.upper()))

def add(word):
    des = input("Enter the description:\n")
    img = input("[optional] image address:\n")
    src = input("[optional] source/credit of the image:\n")
    if api.add(word, des, img, src):
        print("The word '{}' added successfuly to the database".format(word.upper()))
    else:
        print("The word '{}' already exist in the database, try updating".format(word.upper()))

def update(word):
    des = input("Enter the description:\n")
    if des.lower() == "none":
        des = None
    img = input("[optional] image address:\n")
    if img.lower() == "none":
        img = None
    src = input("[optional] source/credit of the image:\n")
    if src.lower() == "none":
        src = None
    if api.update(word, des, img, src):
        print("The word '{}' updated successfuly to the database".format(word.upper()))
    else:
        print("The word '{}' does not exist in the database, try adding".format(word.upper()))

running = True
location = os.path.abspath("")
api.setLocation(location)

print("WELCOME TO THE COMMAND-LINE-INTERFACE OF DICTIONARY BUILDER APPLICATION")
print("ADVICE: try to set the location before starting with CLI")
while running:
    commands = input(">_ ").rstrip(" ").lstrip(" ")
    commands = commands.split(" ")
    if len(commands) > 2 or len(commands) == 0:
        print("no such commands exist")
        continue
    
    if commands[0].upper() == "FIND":
        try:
            find(commands[1])
        except:
            print("incomplete command")
            print("type HELP to get the help dialogue open")
    
    elif commands[0].upper() == "LOC":
        try:
            location = os.path.abspath(commands[1])
            api.setLocation(location)
        except:
            print("incomplete command")
            print("type HELP to get the help dialogue open")
    
    elif commands[0].upper() == "ADD":
        try:
            wrd = commands[1].lower()
            add(wrd)
        except:
            print("incomplete command")
            print("type HELP to get the help dialogue open")

    elif commands[0].upper() == "UPDATE":
        try:
            wrd = commands[1].lower()
            update(wrd)
        except:
            print("incomplete command")
            print("type HELP to get the help dialogue open")
    
    elif commands[0].upper() == "QUIT":
        running = False
        print("CLI application closed")
    
    elif commands[0].upper() == "CREATE":
        print("under construction, check for the update in the github")
    else:
        print("no such commands exist")
        # get the help function
    pass