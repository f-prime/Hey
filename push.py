import os
import re

def push(string):
    string = string.replace("push ", '')
    string = string.split("to")
    files = string[0]
    message = string[1]
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

