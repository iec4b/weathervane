# weathervane.py

# import modules. "Weathervaneconfig" is a customizable set of variable definitions stored in the file weathervaneconfig.py.
import requests
from weathervaneconfig import *
from bs4 import BeautifulSoup
import sys

# Set up for system options and arguments. Currently the program is only set up to take options.
# I copied this basic parser code and the if/elif statements structure from https://realpython.com/python-command-line-arguments/#a-few-methods-for-parsing-python-command-line-arguments
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

# Define a function to be called by each of weathervane's options.
# The source will be determined by the variables defined in weathervaneconfig.py.
def feed(source):
  
  # this uses the requests module to load a web page, and the page address is defined by the external config file weathervaneconfig.py.
  page = requests.get(source)
  
  # Use BeatifulSoup to parse the html drawn from the request.
  soup = BeautifulSoup(page.content, "html.parser")
  
  # The desired texts are located under the element with the id attribute "proddiff".
  results = soup.find(id="proddiff")

  # the function returns the desired text, defined above.
  return(results.text)

# Local weather discussion
if "-dl" in opts:
  print(feed(nyweather_discussions))

# National weather discussion
elif "-dn" in opts:
  print(feed(natlweather_discussions))

# Extended national weather discussion
elif "-dne" in opts:
	print(feed(natlextended_discussions))

# Local forecast
elif "-fl" in opts:
  print(feed(ny_zone_forecast))

# Local observations
elif "-ol" in opts:
	print(feed(nyc_weather_roundup))

# Help text
elif "-h" in opts:
  raise SystemExit(f"Usage: weathervane [-opt] \n\t-dl \t<display New York weather discussions>\n\t-dn \t<display national weather discussions>\n\t-dne \t<display national extended forecast discussions>\n\t-fl \t<display NY zone forecast>\n\t-ol \t<display NYC weather roundup>\n\t-h \t<display this instructional message>")

# Display help text if invalid options and arguments are entered.
else:
  raise SystemExit(f"Usage: weathervane [-opt] \n\t-dl \t<display New York weather discussions>\n\t-dn \t<display national weather discussions>\n\t-dne \t<display national extended forecast discussions>\n\t-fl \t<display NY zone forecast>\n\t-ol \t<display NYC weather roundup>\n\t-h \t<display this instructional message>")

