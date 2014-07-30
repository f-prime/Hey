import re
import webbrowser

def google(data):
    data = re.findall("\"(.*)\"", data)
    webbrowser.open("https://www.google.com/search?q={}".format(data[0]))
    print "There I opened a new browser window"
