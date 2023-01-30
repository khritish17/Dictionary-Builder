'''
    Official API for dictionary builder
'''
import dictionary_builder as DB

def add(word, description, image_link = '--', source = '--', update_warning = True):
    dict_build = DB.Dictionary_builder()
    dict_build.add_word(word=word, description=description, image_link=image_link, source=source, update_warning=update_warning)


def update(word, description, image_link = '--', source = '--'):
    dict_build = DB.Dictionary_builder()
    dict_build.update_word(word = word, description = description, image_link = image_link, source = source)

def view(word):
    dict_build = DB.Dictionary_builder()
    word_data_frame = dict_build.view_word(word = word)
    if word_data_frame:
        print("Word:{}\nDescription:{}\nImage:{}\nSource:{}".format(word, word_data_frame['description'], word_data_frame['image'], word_data_frame['source']))
        return word_data_frame
    else:
        print("No word exist")
        return 

