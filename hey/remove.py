import os
import re

def remove(string):
    filename = re.findall("remove\s(?:the\s)?(?:file\s)?(\w+)", string)[0]

    try:
        print "Okay, removing the file '{}'.".format(filename)
        os.remove(filename)
    except OSError:
        print "Hold on; that file doesn't even exist."
