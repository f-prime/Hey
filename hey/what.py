import urllib
from time import gmtime, strftime
import os
import platform
import datetime

def what(string):
    possible = {

        "my ip":ip,
        "version":version,
        "time":time_,
        "date":date_,
        "day":day,
        "month":month,
        "year":year,
        "directory":directory,
        "operating system":my_os,
        "os":my_os,
        "my name":name,
        }


    for x in possible:
        if x in string:
            possible[x]()


def name():
    print "Your name is: {}".format(platform.uname()[1])

def my_os():
    print "You are currently running: {}".format(platform.linux_distribution()[0])

def directory():
    print "You are currently in: {}".format(os.getcwd())

def month():
    print datetime.datetime.now().strftime("%B")

def year():
    print "{0}".format(strftime("%Y", gmtime()))

def day():
    print "Today is {}".format(datetime.datetime.now().strftime("%A"))

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
