import re
import tarfile
import zipfile
import os
try:
    import zlib
    mode = zipfile.ZIP_DEFLATED
except:
    mode = zipfile.ZIP_STORED

def compress(string):
    """hey compress a.db as a.zip"""

    new_str = ' '.join(string.split("compress")[1:])
    check = re.findall("\S\w*\.\w*", new_str)
    on = 0
    new = []
    temp = []
    for x in check:
        if on < 1:
            temp.append(x)
            on += 1
        else:
            temp.append(x)
            new.append(temp)
            on = 0
    for x in new:
        file_, as_ = x[0], x[1]
        if as_.endswith(".zip"):
            zip_ = zipfile.ZipFile(as_, 'w', mode)
            zip_.write(file_)
            zip_.close()
        elif as_.endswith(".tar"):
            tar = tarfile.open(as_, "w")
            tar.add(file_)
            tar.close()
        else:
            print "It doesn't look like the file type for {0} is supported yet".format(x)
def decompress(string):
    new_str = ' '.join(string.split("decompress")[1:])
    new = []
    data = re.findall("(\S.*\.zip|\S.*.tar)", new_str)
    for x in data:
        if x not in new:
            new.append(x)
    
    for x in new:
        if os.path.exists(x) and x.endswith(".zip"):
            with zipfile.ZipFile(x, 'r') as z:
                z.extractall(os.getcwd())
                print "{0} was decompressed for you.".format(x)
        
        elif os.path.exists(x) and x.endswith(".tar"):
            with tarfile.TarFile(x, 'r') as t:
                t.extractall(os.getcwd())
                print "{0} was decompressed for you.".format(x)
        
        else:
            print "Hmm, it doesn't seem like {0} exists.".format(x)

