# import apiclient
# API_KEY = "AIzaSyAOXqgCFDowOEhWXY_IIUjuupg8nmHkSek" 	
# SERVICE = discovery.build(API, VERSION, developerKey=API_KEY)

import googlemaps
import googlemaps.client
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyAOXqgCFDowOEhWXY_IIUjuupg8nmHkSek")

#Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
print(geocode_result)
