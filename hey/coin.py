import random

def coin(string):
    print "Okay, flipping a coin..."
    print "The coin landed {}.".format(random.choice(("heads", "tails")))
