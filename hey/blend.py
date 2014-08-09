import re
import webbrowser

DISPLAY_URL = "http://www.colorpicker.com/%s"

def blend(string):
    colors = re.findall("([0-9a-f]{6})+", string, flags=re.I)

    if colors:
        c = [0, 0, 0]
        for i in colors:
            c[0] += int(i[:2], 16)
            c[1] += int(i[2:4], 16)
            c[2] += int(i[4:], 16)
            print c
        c = [i // len(colors) for i in c]
        blended = "%.2x%.2x%.2x" % (c[0], c[1], c[2])
        print "Blended: #%s" % blended

        inp = raw_input("Should I open it in a browser for you to see? <Y/n>")
        if inp or inp.lower().startswith("y"):
            webbrowser.open(DISPLAY_URL % blended)

    else:
        print "You have to supply me with some colors in hexadecimal notation!"
