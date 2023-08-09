import dictionary_application as da
import os
location = os.path.abspath("")

def setLocation(loc):
    global location
    location = loc

DA = da.DictionaryApplication(location)

def find(word):
    '''
    return value:
    if the word is in the dictionary database
    -> word, description, image_address, source
    if the word is not in the dictionary database 
    -> None, None, None, None
    '''
    return DA.find_word(word)

def add(word, description, image_address = "", source = ""):
    '''
    return value:
    if the word is not in the dictionary database
    -> True
    if the word is in the dictionary database 
    -> False
    '''
    return DA.add_word(word, description, image_address, source)

def update(word, description = None, image_address = None, source = None):
    '''
    Does not update the particulars where None parameter is passed
    return value:
    if the word is in the dictionary database
    -> True
    if the word is not in the dictionary database 
    -> False
    '''
    return DA.update_word(word, description, image_address, source)

# print(find("asd"))
# print(find("aPple"))
# print(add("fake", "dubicious", "image_address", "source"))
# print(find("fake"))
# update("app","a big tech MNC", "www.apple.com/redapples")
# update("apple", "new phone", "jfj", None)