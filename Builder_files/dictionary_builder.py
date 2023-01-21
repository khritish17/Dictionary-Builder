
class Dictionary_builder:
    def __init__(self) -> None:
        self.cached_file = {}
        pass

    def add_word(self, word, description, image_link = "--", source = "--", update_warning = True):
        word = word.lower()
        initials = word[:2]
        try:
            file = open('dictionary\{}.txt'.format(initials), 'a')
            file.close()
            self.cache_file(initials)
            try:
                _ = self.cached_file[word]
                # give warning
                if update_warning:
                    print("Already word exist, do you want to update ?")
                    response = input("Y/N")
                    if response == "Y" or response == 'y':
                        file = open('dictionary\{}.txt'.format(initials), 'a')
                        file.write("{}|{}|{}|{}\n".format(word, description, image_link, source))
                        file.close()
                        self.refactor(initials)
                    else:
                        pass
                else:
                    file = open('dictionary\{}.txt'.format(initials), 'a')
                    file.write("{}|{}|{}|{}\n".format(word, description, image_link, source))
                    file.close()
                    self.refactor(initials)

            except:
                file = open('dictionary\{}.txt'.format(initials), 'a')
                file.write("{}|{}|{}|{}\n".format(word, description, image_link, source))
                file.close()
        except:
            file = open('dictionary\{}.txt'.format(initials), 'w')
            file.write("{}|{}|{}|{}\n".format(word, description, image_link, source))
            file.close()
    
    def refactor(self, filename):
        self.cached_file = {}
        self.cache_file(file_name = filename)
        file = open('dictionary\{}.txt'.format(filename),'w')
        for wrd, val in self.cached_file.items():
            file.write("{}|{}|{}|{}\n".format(wrd,val['description'], val['image'], val['source']))
        file.close()

    def update_word(self,word, description, image_link = "--", source = "--"):
        self.add_word(word=word, description=description, image_link=image_link, source=source, update_warning=False)
        pass

    def view_word(self, word):
        word = word.lower()
        initials = word[:2]
        
        # check if the file exist
        try:
            file = open('dictionary\{}.txt'.format(initials), 'r')
            file.close()
            self.cache_file(initials)
        except:
            pass
        
        # return the word from cached file
        try:
            return self.cached_file[word]

        except:
            print("No such word exist")
            return 

    def cache_file(self, file_name):
        try:
            file = open('dictionary\{}.txt'.format(file_name), 'r')
            for line in file:
                line = line.rstrip('\n').split('|')
                self.cached_file[line[0]] = dict({'description':line[1], 'image':line[2], 'source':line[3]})
            file.close()
            # print(self.cached_file)
        except:
            print("No such file exist")


# DB = Dictionary_builder()
# # DB.add_word(word = 'Computer', description = "A machine")
# DB.add_word(word = 'Compur', description = "A machine",  update_warning= False)
# DB.add_word(word = 'Khritish', description = "Name",  update_warning= False)
# DB.add_word(word = 'Nma', description = "Name",  update_warning= False)
# DB.add_word(word = 'Khritish_u', description = "Name",  update_warning= False)
# # DB.refactor('co')
# print(DB.view_word(word = 'comPur'))
# DB.update_word(word = 'Khritish', description = "Name 1")
