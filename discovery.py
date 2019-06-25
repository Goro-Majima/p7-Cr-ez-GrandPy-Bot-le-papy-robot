# import googlemaps
# import googlemaps.client
# import json
# import requests
# from datetime import datetime
# from config import *

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

"""mediawiki ok"""
# import requests

# S = requests.Session()

# URL = "https://fr.wikipedia.org/w/api.php"

# LIST = 'tour eiffel'
# TITLE = 'marseille'
# """choose de right parameters to get the first description of the place
# check https://www.mediawiki.org/wiki/Extension:TextExtracts#Caveats
# """
# PARAMS = {
#     'action':"query",
#     'exsentences':1,
#     'exlimit':1,
#     'explaintext':True,
#     'exsectionformat':'plain',
#     'titles': TITLE,
#     'format':"json",
#     "prop":"extracts|info",
#     'inprop': 'url'
# }

# R = S.get(url=URL, params=PARAMS)
# DATA = R.json()
# PAGES = DATA['query']['pages']

# print(PAGES)
# try:
#     for k, v in PAGES.items():
#         print('story: ', v['extract'],' lien: ', v['fullurl'])
# except KeyError:
#     print("Désolé ")

# from grandpy.classes import *

# query = input("entre ton lieu: ")
# parsedquery = Parsing(query)
# keyword = parsedquery.returnkeyword()
# datagmap = Googlemap(keyword)
# #try to get address and coordinates"""
# try:
#     location = datagmap.http_results()
#     diction = {'papyintro': 'Voici le lieu que tu cherches: ', 'address':location[0],\
#         'latitude': location[1], 'longitude': location[2]}
#     infowithoutstory = diction['papyintro'] + diction['address'] + ", ses coordonnées gps: ", \
#     diction['latitude'], diction['longitude']
#     print(infowithoutstory)
#     #try to get a story an,d link (tuple) from mediawiki with the keyword
#     try:
#         mediawikistory = Mediawiki(keyword).historytell()
#         diction = {'papyintro': 'Voici le lieu que tu cherches:', 'address':location[0],\
#         'latitude': location[1], 'longitude': location[2], 'story': mediawikistory}
#         infowithstory = "J'ai une belle histoire à raconter sur ce lieu: " + diction['story'][0]# diction['story'] is a tuple
#         print(infowithstory)
#         print("Si tu veux en savoir plus clique sur ce lien: " + diction['story'][1])
#     #return negative answer if no story to tell
#     except KeyError:
#         print("Désolé mon petit mais je ne me souviens plus de l'histoire de ce lieu")
# #return negative answer if index out of list or no data""" 
# except IndexError:
#     print("Désolé mon petit mais je n'ai pas trouvé ce que tu me demandes =(")

import requests

S = requests.Session()

URL = "https://fr.wikipedia.org/w/api.php"

COORDS = '48.8604234|2.7604437'

PARAMS = {
    'action':"query",
    'list':"geosearch",
    'gscoord': COORDS,
    'gsradius':10000,
    'gslimit':1,
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PLACES = DATA['query']['geosearch']

for place in PLACES:
    print(place['title'])

TITLE = place['title']

PARAMS = {
    'action':"query",
    'exsentences':1,
    'exlimit':1,
    'explaintext':True,
    'exsectionformat':'plain',
    'titles': TITLE,
    'format':"json",
    "prop":"extracts|info",
    'inprop': 'url'
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']

try:
    for k, v in PAGES.items():
        print('story: ', v['extract'],' lien: ', v['fullurl'])
except KeyError:
    print("Désolé ")
