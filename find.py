import webbrowser
import os
import re

def find(data):
    possible = {"find me a":store,
            "find file containing":find_file_containing,
                "find file":find_file,    
            }
    
    for x in possible:
        if x in data:
            possible[x](data)
            break


def find_file(data):
    d = re.findall("\"(.*)\"", data)
    if data:
        data = d[0]
    else:
        print "I don't understand"
        return
    for dir,_,file in os.walk("/"):
        for file in file:
            if file == data:
                print dir+"/"+file

def find_file_containing(data):
    d = re.findall("\"(.*)\"", data)
    if d:
        data = d[0]
    else:
        print "I don't understand"
        return

    for dir,_,file in os.walk("/"):
        for file in file:
            try:
                with open(dir+"/"+file, 'rb') as file_:
                    if file_.read().find(data) != -1:
                        print dir+"/"+file
            except IOError:
                pass

def store(data):
    data = ''.join(data.split("find me a ")[1])
    split_words = [" near ", " in ", " by "]
    for word in split_words:
        if word in data:
            data = data.split(word)
            break
    if type(data) != list:
        webbrowser.open("http://www.yelp.com/search?find_desc={0}".format(data[0]))
    else:
        webbrowser.open("http://www.yelp.com/search?find_desc={0}#find_loc={1}".format(data[0], data[1]))
