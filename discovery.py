import googlemaps
import googlemaps.client
import json
import requests
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyAOXqgCFDowOEhWXY_IIUjuupg8nmHkSek")

#Geocoding an address
geocode_result = gmaps.geocode('tour eiffel')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((48.8747265, 2.3505517))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
print(geocode_result[0])
