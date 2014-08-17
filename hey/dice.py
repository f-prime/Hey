import random
import re

def dice(string):
    # We assume that the first number (if any) is the number of sides.  
    sided = re.findall("(\d+)", string)
    sides = int(sided[0]) if sided else 6

    print "Sure, rolling a %d sided dice for you..." % sides
    print "The dice rolled %d." % random.randint(1, sides)
