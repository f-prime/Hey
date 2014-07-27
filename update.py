import os

def update(string):
    possibilities = {"ubuntu":"apt-get update",
                     "centos":"yum update",
                     "debian":"aptitude update",
                    }
    for x in possibilities:
        if x in string:
            os.system(possibilities[x])
            return

    print "That OS or distribution is not supported"
