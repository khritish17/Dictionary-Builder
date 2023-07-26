import os
class TrieNode:
    def __init__(self) -> None:
        self.characters = {}
        self.database = None
        self.line_no = None
        self.status = None
    
class TrieGenerator:
    def __init__(self, address_file, location) -> None:
        self.address_file = address_file
        self.location = location
        self.head = TrieNode()
        self.read_address_file()
        
    def read_address_file(self):
        address_file = open(self.location + "/core_file/ address_files/{}".format(self.address_file), "r")
        for line in address_file:
            # line = address_file.readline().rstrip("\n")
            line = line.rstrip("\n").split(",")
            self.add(line)

    def add(self, data):
        word, database, line_no = data[0], data[1], data[2] 
        temp = self.head
        # print("temp:{}".format( temp))
        for letter in word:
            try:
                temp = temp.characters[letter]
            except:
                temp.characters[letter] = TrieNode()
                temp = temp.characters[letter]
            # print("letter:{}, temp:{}".format(letter, temp))
        temp.database = database
        temp.line_no = line_no
        temp.status = True
    def send_head(self):
        return self.head
# T = TrieGenerator( "a.adsf",os.path.abspath(""))