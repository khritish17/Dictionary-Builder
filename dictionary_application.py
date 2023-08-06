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
            return None, None, None, None
        else:
            word = word.lower()
            initial = word[0]
            if initial not in "abcdefghijklmnopqrstuvwxyz":
                self.log_file.write("\u274C\tError: '{}' is not a valid word, try not using any special characters in the word\n".format(word))
                return None, None, None, None
            else:
                address_file = "{}.adsf".format(initial)
                # check for the existence of the TRIE of the address file
                address_file_TRIE = None
                try:
                    address_file_TRIE = self.global_addressmap[initial]
                except:
                    self.log_file.write("\u274C\tError: '{}' TRIE not found in global addressmap\n".format(initial))
                    # generate the TRIE for the address_file
                    TRIE = tg.TrieGenerator(address_file, self.location)
                    self.global_addressmap[initial] = TRIE.send_head()
                    address_file_TRIE = self.global_addressmap[initial]
                    self.log_file.write("\u2705\t'{}' TRIE generated and added to global addressmap\n".format(initial))
                
                # check for existence of the word in the TRIE
                # write the find algorithm of TRIE in trie_generator.py file write it as another class 
                SRCH = tg.SearchInTrie(address_file_TRIE, word)
                status, database_file, line_no = SRCH.search()
                if status:
                    # the word is in the database file at line number line_no
                    db_file = open(self.location + "/core_file/ database_files/{}".format(database_file), 'r')
                    db = db_file.readlines()
                    word, description, image_address, source = db[int(line_no)].split('|')
                    return word, description, image_address, source
                else:
                    return None, None, None, None

                

            






    def add_word(self):
        pass

    def update_word(self):
        pass
DA = DictionaryApplication()
word, description, image_address, source = DA.find_word("")
# DA.find_word("_tri")
word, description, image_address, source = DA.find_word("asd")
DA.close()

