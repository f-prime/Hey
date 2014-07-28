import re
import webbrowser

def go(string):
    check = re.findall("go to http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", string)
    reddit = re.findall("go to /r/[a-z]*",string)
    if check:
        check[0] = check[0].replace("go to ", '')
        webbrowser.open(check[0])
    else:
        if reddit:
            reddit[0] = reddit[0].replace("go to ", '')
            webbrowser.open("http://reddit.com" + reddit[0])
    
