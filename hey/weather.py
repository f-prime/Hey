"""Uses Yahoo's weather API to determine a forecast and output it."""
from xml.dom.minidom import parseString
import re
import urllib

WEATHER_URL = "http://weather.yahooapis.com/forecastrss?w=%s&u=c"
CONDITIONS = "%s, it is %s with a temperature of about %s degrees C."
FORECAST = "%s -- %s, lows of %s degrees C, highs of %s degrees C."

# We define this lambda function because calling node.getAttribute is
# long and ugly. ga(node, name) is much shorter and nicer.
ga = lambda node, name: node.getAttribute(name)

def print_conditions(dom):
    print "== CONDITIONS =="

    for node in dom.getElementsByTagName("yweather:condition"):
        print CONDITIONS % (ga(node, "date"), ga(node, "text"),
                            ga(node, "temp"))

def print_forecast(dom):
    print "== FORECAST =="

    for node in dom.getElementsByTagName("yweather:forecast"):
        print FORECAST % (ga(node, "day"), ga(node, "text"),
                            ga(node, "low"), ga(node, "high"))

def weather(string):
    find_results = re.findall("(\d{7})", string)

    # If we couldn't find a 7 digit area code...  
    if not find_results:
        print "Please supply a valid 7 digit area code."
        return

    area_code = find_results[0]

    try:
        dom = parseString(urllib.urlopen(WEATHER_URL % area_code).read())
    except:
        print "An internal error occurred."
        return
    
    print_conditions(dom)
    print "\n", # To make space for forecast.  
    print_forecast(dom)
