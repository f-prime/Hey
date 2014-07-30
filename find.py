import webbrowser

def find(data):
    possible = {"find me a":store}
    
    for x in possible:
        if x in data:
            possible[x](data)
            break


def store(data):
    data = ''.join(data.split("find me a ")[1])
    split_words = [" near ", " in ", " by "]
    for word in split_words:
        if word in data:
            data = data.split(word)
            break
    if type(data) != list:
        webbrowser.open("http://www.yelp.com/search?find_desc={0}".format(data[0]))
    else:
        webbrowser.open("http://www.yelp.com/search?find_desc={0}#find_loc={1}".format(data[0], data[1]))
