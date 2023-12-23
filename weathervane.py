# weathervane.py

import requests
from weathervaneconfig import *
from bs4 import BeautifulSoup
import sys

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

def feed(source):
        
  page = requests.get(source)

  soup = BeautifulSoup(page.content, "html.parser")

  results = soup.find(id="proddiff")

  return(results.text)

if "-dl" in opts:
  print(feed(nyweather_discussions))
elif "-dn" in opts:
  print(feed(natlweather_discussions))
elif "-dne" in opts:
	print(feed(natlextended_discussions))
elif "-fl" in opts:
  print(feed(ny_zone_forecast))
elif "-ol" in opts:
	print(feed(nyc_weather_roundup))
elif "-h" in opts:
  raise SystemExit(f"Usage: weathervane [-opt] \n\t-dl \t<display New York weather discussions>\n\t-dn \t<display national weather discussions>\n\t-dne \t<display national extended forecast discussions>\n\t-fl \t<display NY zone forecast>\n\t-ol \t<display NYC weather roundup>\n\t-h \t<display this instructional message>")
else:
  raise SystemExit(f"Usage: weathervane [-opt] \n\t-dl \t<display New York weather discussions>\n\t-dn \t<display national weather discussions>\n\t-dne \t<display national extended forecast discussions>\n\t-fl \t<display NY zone forecast>\n\t-ol \t<display NYC weather roundup>\n\t-h \t<display this instructional message>")

