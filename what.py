import urllib

def what(string):
    possible = {

        "what is my ip":ip,
        "what version":version,
    }


    for x in possible:
        if x in string:
            possible[x]()


def ip():
    ip = urllib.urlopen("http://www.telize.com/ip").read()
    print "Your IP is: {0}".format(ip)

def version():
    version = "0.1.0"
    print "You currently have version {0} of Hey".format(version)
