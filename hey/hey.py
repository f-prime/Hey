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
import remove
import rename
import sys
import tell
import update
import what

class Hey:
    def __init__(self):
        self.keywords = {
        
            "clone":push.clone,
            "coin":coin.coin,
            "compress":compression.compress,
            "copy":copy.copy,
            "decompress":compression.decompress,
            "dice":dice.dice,
            "directions":directions.directions,
            "download":download.download,
            "find":find.find,
            "go":go.go,
            "google":google.google,
            "googling":google.google, # Just a different possible word
            "pull":push.pull,
            "push":push.push,
            "remove":remove.remove,
            "rename":rename.rename,
            "tell":tell.tell,
            "update":update.update,
            "what":what.what,
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
