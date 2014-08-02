import os
import re

def push(string):
    string = string.replace("push ", '')
    string = string.split("to")
    files = string[0]
    try:
        message = string[1]
    except IndexError:
        print "To where should I push it?"
        return
    message = re.findall("\"(.*)\"", message)
    if not message:
        message = "This was commited with \"Hey\""
    else:
        message = message[0]

    if files.find("everything") != -1:
        os.system("git add -A")
    else:
        os.system("git add "+' '.join(files.split(",")))

    os.system("git commit -m \""+message+"\"")
    os.system("git push -u origin master")



def pull(string):
    os.system("git pull -u origin master")


def clone(string):
    check = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", string)
    os.system("git clone {0}".format(check[0]))

