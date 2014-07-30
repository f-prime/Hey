import webbrowser
import re

def directions(data):
    #hey get me directions from "asd,asd,asd" to "asd,asd,asd"
    data = data.split(" to ")
    starting = re.findall("\"(.*)\"", data[0])
    ending = re.findall("\"(.*)\"", data[1])
    if len(data) != 2:
        print "I don't understand"
        return
    starting = data[0].split(",")
    ending = data[1].split(',')

    webbrowser.open("https://www.google.com/maps/dir/{0}, {1}, {2}/{3}, {4}, {5}/".format(starting[0], starting[1], starting[2], ending[0], ending[1], ending[2]))

