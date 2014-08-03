import os
import re
import shutil

def rename(string, copy=False):
    if copy:
        string = string.split("copy ")[1:][0]
    else:
        string = string.split("rename ")[1:][0]

    check = re.findall("\sto\s|\sas\s", string)
    if check:
        for x in check:
            string = string.replace(x, ' ')
    
    string = string.split()
    if copy: # So I don't repeat myself
        shutil.copyfile(string[0], string[1])
        print "The file {0} has been copied to {1}".format(string[0], string[1])

    else:
        os.rename(string[0], string[1]) 
        print "The file {0} has been renamed to {1}".format(string[0], string[1])
