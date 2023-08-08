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
            self.log_file.write("\u274C\tError: Tried to find an empty string in find_word()\n")
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
                    db_file = open(self.location + "/core_file/ database_files/{}".format(database_file.lstrip(" ")), 'r')
                    db = db_file.readlines()
                    word, description, image_address, source = db[int(line_no)].split('|')
                    self.log_file.write("\u2705\t'{}' found successfully in the '{}' TRIE\n".format(word, initial))
                    db_file.close()
                    return word, description, image_address, source
                else:
                    self.log_file.write("\u274C\tError: '{}' not found in the '{}' TRIE, if it's a valid word add the word\n".format(word, initial))
                    return None, None, None, None

    def add_word(self, word, description, image_address = "", source = ""):
        word = word.lower()
        wrd, _, _, _ = self.find_word(word)
        initial = word[0]
        if wrd == None:
            # word is not previously stored, proceed for adding the word
            # add the word to the database file get the line number
            database_file = "{}.dbf".format(initial)
            db_file = open(self.location + "/core_file/ database_files/{}".format(database_file), 'a')
            db_file.write("{}|{}|{}|{}\n".format(word, description, image_address, source))
            db_file.close()
            
            # to read the line number 
            db_file = open(self.location + "/core_file/ database_files/{}".format(database_file), 'r')
            line_no = len(db_file.readlines()) - 1
            db_file.close()
            
            # add the word and the linenumber to the address file
            address_file = "{}.adsf".format(initial)
            ads_file = open(self.location + "/core_file/ address_files/{}".format(address_file), 'a')
            ads_file.write("{},{},{}\n".format(word, database_file, line_no))
            ads_file.close()

            # add the word to the TRIE in global hashmap if it exist
            try:
                # if the TRIE is already present in the global_addressmap
                trie_head = self.global_addressmap[initial]
                # add the word to the TRIE
                tg.AddInTrie(head = trie_head, word = word, database = db_file, line_no = line_no)
            except:
                # if the TRIE is not already generated, then nothing needs to be done
                # since the data is already in the address_file, TRIE will be generated 
                # whenever it is required
                pass  
        else:
            # Word already exist 
            # suggest updating
            self.log_file.write("\u26A0\tWarning: '{}' already exist, try updating the word\n".format(word))
            return None

            

    def update_word(self):
        pass
DA = DictionaryApplication()
word, description, image_address, source = DA.find_word("tri")
word, description, image_address, source = DA.find_word("asd")
DA.add_word("apple", "a popular fruit, a big MNC is named after")
DA.add_word("trie", "a data structure which is used to make this application")
DA.close()

