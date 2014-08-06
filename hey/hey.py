#!/usr/bin/python

import coin
#Import Readline module for the console.
import readline

import calculate
import download
import sys
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



class Console:
        def __init__(self):
            pass

        def start(self):
            print "Welcome to Hey Console. Type 'quit' to exit."
            while(1):
                string = raw_input("Hey> ")
                string = string.strip()
                if string == 'quit':
                    exit()
                string = string.split()
                Hey().parse(string)


class Hey:
    #Used to differentiate between terminal input and console.
    console  = False

    def __init__(self):
        self.keywords = {
        
            "calc" : calculate.calculate,
            "calculate" : calculate.calculate,
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
    def setTerminal(self,val):
        #Will set value to the console variable
        #If console it 0 it is a terminal input else console
        console = val
        
    def parse(self, string=""):
        valid = False
        #Use input from sys.argv only if input given from terminal.
        if self.console:
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
    if len(sys.argv) == 1:
        Hey().setTerminal(True)
        Cons = Console()
        Cons.start()
    else:
        Hey().parse()

