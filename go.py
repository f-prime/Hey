import re
import webbrowser

def go(string):
    check = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", string)
    reddit = re.findall("/r/[a-zA-Z0-9_]*",string)
    if check:
        webbrowser.open(check[0])
    elif reddit:      
        webbrowser.open("http://reddit.com" + reddit[0])
    
