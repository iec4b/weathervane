# weathervane.py
# This is the configuration file for the weathervane tool.

# Set the URLs for extracting information from the national weather service, and rename the variables as you see fit. Just be sure to update the weathervane.py file accordingly. 
#You may have to do some digging/tweaking to make sure that weathervane will find the right text content if you change the sources from what you see below. Adjustments could be necessary, for example, to the soup.find() function.
# This version is tailored to the New York City area.

# Weather Discussions

# New York Weather Discussions

nyweather_discussions="https://forecast.weather.gov/product.php?site=NWS&issuedby=OKX&product=AFD&format=txt&version=1&glossary=1&highlight=off"

# National Weather Discussions

natlweather_discussions = "https://forecast.weather.gov/product.php?site=NWS&issuedby=SPD&product=PMD&format=CI&version=1&glossary=1&highlight=off"

natlextended_discussions = "https://forecast.weather.gov/product.php?site=NWS&issuedby=EPD&product=PMD&format=CI&version=1&glossary=1&highlight=off"

# Other products

# NYC Weather Roundup

nyc_weather_roundup = "https://forecast.weather.gov/product.php?site=NWS&issuedby=OKX&product=OSO&format=txt&version=1&glossary=1&highlight=off"

# NY Zone Forecast

ny_zone_forecast = "https://forecast.weather.gov/product.php?site=NWS&issuedby=OKX&product=ZFP&format=txt&version=1&glossary=1&highlight=off"
