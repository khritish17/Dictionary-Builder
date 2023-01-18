
class Dictionary_builder:
    def __init__(self) -> None:
        self.cached_file = {}
        pass

    def add_word(self, word, description, image_link = "--", source = "--"):
        word = word.lower()
        initials = word[:2]
        try:
            file = open('dictionary\{}.txt'.format(initials), 'a')
            file.write("{}|{}|{}|{}\n".format(word, description, image_link, source))
            file.close()
        except:
            file = open('dictionary\{}.txt'.format(initials), 'w')
            file.write("{}|{}|{}|{}\n".format(word, description, image_link, source))
            file.close()

    def update_word(self):
        pass

    def view_word(self, word):
        word.lower()
        initials = word[:2]
        try:
            file = open('dictionary\{}.txt'.format(initials), 'r')
            for line in file:
                line = line.rstrip('\n').split('|')
                self.cache_file(data_frame = line)
            file.close()
        except:
            print("No such word exist")
        print(self.cached_file)


    def cache_file(self, data_frame):
        wrd = data_frame[0]
        des = data_frame[1]
        img = data_frame[2]
        src = data_frame[3]
        self.cached_file[wrd] = dict({'description':des, 'image':img, 'source':src})

    def history(self):
        pass

DB = Dictionary_builder()
# DB.add_word(word = 'Computer', description = "A machine")
# DB.add_word(word = 'Compur', description = "A machine")
DB.view_word(word = 'Computer')