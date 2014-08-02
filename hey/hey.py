#!/usr/bin/python

import coin
import compression
import copy
import dice
import directions
import download
import find
import go
import google
import push
import rename
import sys
import tell
import update
import what

class Hey:
    def __init__(self):
        self.keywords = {
        
            "download":download.download,
            "dice":dice.dice,
            "coin":coin.coin,
            "compress":compression.compress,
            "decompress":compression.decompress,
            "rename":rename.rename,
            "copy":copy.copy,
            "what":what.what,
            "go":go.go,
            "tell":tell.tell,
            "push":push.push,
            "pull":push.pull,
            "clone":push.clone,
            "update":update.update,
            "google":google.google,
            "googling":google.google, # Just a different possible word
            "directions":directions.directions,
            "find":find.find,
            }

    
    def parse(self):
        valid = False
        string = sys.argv[1:]
        for x in string:
            if x in self.keywords:
                valid = True
                self.keywords[x](' '.join(string))
                
        if not valid:
            print "Sorry, I didn't understand your command."

def main():
    Hey().parse()

if __name__ == "__main__":
    main()
