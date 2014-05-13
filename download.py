import re
import urllib
import uuid

def download(string):
    find = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", string)
    as_ = re.findall(r"(as|to|named|name\sit|with\sthe\sname|naming\sit) (.*\s)", string)
    for num, x in enumerate(as_):
        as_[num] = x[1]

    
    for num, x in enumerate(as_):
        if num < len(find):
            on = find[num]
            open(x, 'wb').write(urllib.urlopen(on).read())
            find.remove(find[num])
        else:
            break
    
    for x in find:
        with open(uuid.uuid4().hex, 'wb') as file:
            file.write(urllib.urlopen(x).read())

    
        
