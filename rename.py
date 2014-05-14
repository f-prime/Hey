import re
import os

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
    else:
        os.rename(string[0], string[1]) 

