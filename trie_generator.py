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
        for line in address_file.readlines():
            # line = address_file.readline().rstrip("\n")
            if line:
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

class SearchInTrie:
    def __init__(self, head, word) -> None:
        self.head = head
        self.word = word
    
    def search(self):
        temp = self.head
        for letter in self.word:
            try:
                temp = temp.characters[letter]
            except:
                return False, None, None
        return temp.status, temp.database, temp.line_no


class AddInTrie:
    def __init__(self, head, word, database, line_no) -> None:
        self.head = head
        self.word = word
        self.database = database
        self.line_no = line_no
    
    def add(self):
        temp = self.head
        for letter in self.word:
            try:
                temp = temp.characters[letter]
            except:
                temp.characters[letter] = TrieNode()
                temp = temp.characters[letter]
        temp.status = True
        temp.database = self.database
        temp.line_no = self.line_no


# T = TrieGenerator( "a.adsf",os.path.abspath(""))
# head = T.send_head()
# S = SearchInTrie(head, "asd")
# print(S.search())
