import os
import re

def rename(string, copy=False):
    if copy:
        word = "copy "
    else:
        word = "rename "
    string = string.split(word)[1:][0]
    check = re.findall("\sto\s|\sas\s", string)
    if check:
        for x in check:
            string = string.replace(x, ' ')
    
    string = string.split()
    if copy: # So I don't repeat myself
        with open(string[0], 'rb') as read:
            with open(string[1], 'wb') as write:
                write.write(read.read())

        print "The file {0} has been copied to {1}".format(string[0], string[1])

    else:
        os.rename(string[0], string[1]) 
        print "The file {0} has been renamed to {1}".format(string[0], string[1])
