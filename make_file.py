import os

def make_file(location):
    # here the location needs to be the absolute path
    # first create the directories
    log_file = open("log.txt", "a",encoding="utf-8")
    log_file.write("\u2705 core files creation initiated\n")
    path = location + "/core_file/ address_files"
    try:
        os.makedirs(path)
        log_file.write("\u2705 \taddress_files directory created\n")
    except:
        log_file.write("\u2705 \taddress_files directory already exist\n")
    path = location + "/core_file/ database_files"
    try:
        os.makedirs(path)
        log_file.write("\u2705 \tdatabase_files directory created\n")
    except:
        log_file.write("\u2705 \taddress_files directory already exist\n")
    
    # generate the address_files
    letters = "abcdefghijklmnopqrstuvwxyz"
    for initial in letters:
        path = location + "/core_file/ address_files/{}.adsf".format(initial)
        f = open(path,"w")
        f.close()
        log_file.write("\u2705 \t{}.adsf created\n".format(initial))
    log_file.write("\n")
    # generate the database_files
    for initial in letters:
        path = location + "/core_file/ database_files/{}.dbf".format(initial)
        f = open(path,"w")
        f.close()
        log_file.write("\u2705 \t{}.dbf created\n".format(initial))
    log_file.write("\u2705 Core files creation completed\n\n")

# path = os.path.abspath("")
# make_file(path)
