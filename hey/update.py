import os
import platform

def update(string):
    possibilities = {"ubuntu":"apt-get update",
                     "centos":"yum update",
                     "debian":"aptitude update",
                     "arch":"pacman -Syu",
                    }

    try:
        os.system(possibilities[platform.linux_distribution()[0]])
    except KeyError:
        print "That OS or distribution is not supported"
