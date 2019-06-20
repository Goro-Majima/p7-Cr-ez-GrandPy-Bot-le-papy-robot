# import googlemaps
# import googlemaps.client
# import json
# import requests
# from datetime import datetime

# splitted = 'openclassrooms'

# gmaps = googlemaps.Client(key="AIzaSyAOXqgCFDowOEhWXY_IIUjuupg8nmHkSek")

# #Geocoding an address
# geocode_result = gmaps.geocode('tour eiffel')

# # Look up an address with reverse geocoding
# # reverse_geocode_result = gmaps.reverse_geocode((48.8747265, 2.3505517))

# # # Request directions via public transit
# # now = datetime.now()
# # directions_result = gmaps.directions("Sydney Town Hall",
# #                                      "Parramatta, NSW",
# #                                      mode="transit",
# #                                      departure_time=now)

# lat = geocode_result[0]["geometry"]["location"]["lat"]
# lon = geocode_result[0]["geometry"]["location"]["lng"]
# address = geocode_result[0]['formatted_address']
# #test - print results
# print (lat, lon, address) 

# """api wikipedia"""
# import wikipediaapi

# wiki_wiki = wikipediaapi.Wikipedia('en')

# page_py = wiki_wiki.page('tour eiffel')
# print("Page - Exists: %s" % page_py.exists())
# # Page - Exists: True

# page_missing = wiki_wiki.page('NonExistingPageWithStrangeName')
# print("Page - Exists: %s" %     page_missing.exists())
# # Page - Exists: False

# import simplemediawiki 
# """api mediawiki"""
# wiki = simplemediawiki.MediaWiki('http://www.mediawiki.org/w/api.php')

# # sample query suggested by Wikidata API sandbox
# print wiki.call({'action': 'wbsearchentities', 'search': 'abc',
#                  'language': 'en', 'limit': 10, 'continue': 10})

# from pywikiapi import wikipedia
# # Connect to English Wikipedia
# site = wikipedia('en')

# Iterate over all query results as they are returned
# from the server, handling continuations automatically.
# (pages whose title begins with "New York-New Jersey")

# """get article from title"""
# for r in site.query(list='allpages', apprefix='Zidane'):
#   for page in r.allpages:
#     print(page.title)

# # Iterate over two pages, getting the page info and the list of links for each of the two pages. Each page will be yielded as a separate result.
# for page in site.query_pages(titles=['Neymar', 'API'], prop=['links', 'info'], pllimit=10):
#     print(page.title)
#     print(', '.join([l.title for l in page.links]))
#     print()

import requests

S = requests.Session()

URL = "https://fr.wikipedia.org/w/api.php"

TITLE = 'place Pigalle'
"""choose de right parameters to get the first description of the place
check https://www.mediawiki.org/wiki/Extension:TextExtracts#Caveats
"""
PARAMS = {
    'action':"query",
    'prop':"extracts",
    'exsentences':3,
    'exlimit':1,
    'explaintext':True,
    'exsectionformat':'plain',
    'titles': TITLE,
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']['extract']

# for k, v in PAGES.items():
#     print("Latitute: " + str(v['coordinates'][0]['lat']))
#     print("Longitude: " + str(v['coordinates'][0]['lon']))
try:
    print(PAGES)
except KeyError:
    pass