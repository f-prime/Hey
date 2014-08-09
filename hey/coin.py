import random

def coin(string):
    print "Okay, flipping a coin..."
    print "The coin landed %s." % random.choice(("heads", "tails"))
