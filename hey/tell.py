import json
import urllib

def tell(string):
    possible = {
        
            "tell me a joke":joke,

    }

    for x in possible:
        if x in string:
            possible[x]()

def joke():
    data = json.loads(urllib.urlopen("http://api.icndb.com/jokes/random").read())
    print data['value']['joke']
