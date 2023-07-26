import os
import datetime
import trie_generator as tg
'''
    x - \u274C
    right - \u2705
'''
class DictionaryApplication:
    def __init__(self, location = os.path.abspath("")) -> None:
        # the location where the database, address file and semaphore files will be saved
        # absolute path is used 
        self.location = location
        self.global_addressmap = {}
        self.log_file = open("log.txt", "a",encoding="utf-8")
        self.log_file.write("\u2705 Application launched: {}\n".format(datetime.datetime.now()))

    def close(self):
        self.log_file.write("\u2705 Application terminated safely\n\n")
        self.log_file.close()
    
    def clear_logfile(self):
        os.remove('log.txt')

    def find_word(self, word):
        if not word:
            self.log_file.write("\u274C\tError: Tried to find an empty string in add_word()\n")
        else:
            word = word.lower()
            initial = word[0]
            if initial not in "abcdefghijklmnopqrstuvwxyz":
                self.log_file.write("\u274C\tError: '{}' is not a valid word, try not using any special characters in the word\n".format(word))
                self.close()
                exit()
            address_file = "{}.adsf".format(initial)
            # check for the existence of the TRIE of the address file
            try:
                self.global_addressmap[initial]
            except:
                self.log_file.write("\u274C\tError: '{}' TRIE not found in global addressmap\n".format(initial))
                # generate the TRIE for the address_file
                TRIE = tg.TrieGenerator(address_file, self.location)
                self.global_addressmap[initial] = TRIE.send_head()

            # check for existence of the word in the TRIE
            # write the find algorithm of TRIE in trie_generator.py file write it as another class 

            






    def add_word(self):
        pass

    def update_word(self):
        pass
DA = DictionaryApplication()
DA.find_word("")
DA.find_word("_tri")
DA.close()

