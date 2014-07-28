import urllib
from time import gmtime, strftime

def what(string):
    possible = {

        "my ip":ip,
        "version":version,
        "time":time_,
        "date":date_
    }


    for x in possible:
        if x in string:
            possible[x]()


def date_():
    print "The date is: {0}".format(strftime("%d-%m-%Y", gmtime()))

def time_():
    print "The time is: {0}".format(strftime("%H:%M:%S", gmtime()))

def ip():
    ip = urllib.urlopen("http://www.telize.com/ip").read()
    print "Your IP is: {0}".format(ip)

def version():
    version = "0.1.0"
    print "You currently have version {0} of Hey".format(version)
