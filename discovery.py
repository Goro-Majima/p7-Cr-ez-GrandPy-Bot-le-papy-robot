import googlemaps
import googlemaps.client
import json
import requests
from datetime import datetime
from config import *
from grandpy.Main.main import process_question
# splitted = 'openclassrooms'

# gmaps = googlemaps.Client(key="AIzaSyAOXqgCFDowOEhWXY_IIUjuupg8nmHkSek")

# #Geocoding an address
# geocode_result = gmaps.geocode(splitted)

# # Look up an address with reverse geocoding
# # reverse_geocode_result = gmaps.reverse_geocode((48.8747265, 2.3505517))

# # # Request directions via public transit
# # now = datetime.now()
# # directions_result = gmaps.directions("Sydney Town Hall",
# #                                      "Parramatta, NSW",
# #                                      mode="transit",
# #                                      departure_time=now)

# # lat = geocode_result[0]["geometry"]["location"]["lat"]
# # lon = geocode_result[0]["geometry"]["location"]["lng"]
# # address = geocode_result[0]['formatted_address']
# #test - print results
# print (geocode_result) 

# """autre manière de recuperer coordonées api gmaps"""
# S = requests.Session()
# key="AIzaSyAOXqgCFDowOEhWXY_IIUjuupg8nmHkSek"
# URL= "https://maps.googleapis.com/maps/api/geocode/json"

# splitted = 'openclassrooms'

# PARAMS = {
#     'address': splitted,
#     'key': key,
#     'region':'fr'
# }
# R = S.get(url= URL, params=PARAMS)
# DATA = R.json()
# lat = DATA['results'][0]['geometry']['location']['lat']
# lng = DATA['results'][0]['geometry']['location']['lng']
# address = DATA['results'][0]['formatted_address']
# print(lat, lng, address)


# # """mediawiki ok"""
# import requests

# S = requests.Session()

# URL = "https://fr.wikipedia.org/w/api.php"

# TITLE = 'les invalides'
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


#OK FUNCTION
# from grandpy.classes import *

# query = input("entre ton lieu: ")
# parsedquery = Parsing(query)
# keyword = parsedquery.returnkeyword()
# datagmap = Googlemap(keyword)
# #try to get address and coordinates"""
# try:
#     location = datagmap.http_results()
#     diction = {'papyintro': "Bien sûr mon poussin! La voici: ", 'address':location[2],\
#         'latitude': location[0], 'longitude': location[1]}
#     addressinfo = diction['papyintro'] + diction['address']
    
#     #try to get a story an,d link (tuple) from mediawiki with the keyword
#     try:
#         mediawikistory = Mediawiki(diction['latitude'], diction['longitude']).historytell()
#         print(mediawikistory[1])
#         diction = {'papyintro': 'Voici le lieu que tu cherches:', 'address':location[2],\
#         'latitude': location[0], 'longitude': location[1], 'story': mediawikistory}
#         infowithstory = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? " + diction['story'][0]# diction['story'] is a tuple
#         link = "Si tu veux en savoir plus clique sur ce lien: " + diction['story'][1]
#         print(addressinfo)
#         print(infowithstory)
#         print("")
#         print(link)
#     #return negative answer if no story to tell
#     except IndexError:
#         print("Désolé mon petit mais j'ai tout oublié à propos de ce lieu...")
# #return negative answer if index out of list or no data""" 
# except IndexError:
#     print("Désolé mon petit mais je n'ai pas trouvé ce que tu me demandes =(")

##mediawiki extract with geolocation
# import requests

# S = requests.Session()

# URL = "https://fr.wikipedia.org/w/api.php"

# COORDS = '48.8748465|2.3504873'#https://www.coordonnees-gps.fr/

# PARAMS = {
#     'action':"query",
#     'list':"geosearch",
#     'gscoord': COORDS,
#     'gsradius':10000,
#     'gslimit':3,
#     'format':"json"
# }

# R = S.get(url=URL, params=PARAMS)
# DATA = R.json()
# PLACES = DATA['query']['geosearch']
# TITLE = PLACES[0]['title']
# for i in PLACES:
#     print(i['title'])
# PARAMS = {
#     'action':"query",
#     'exsentences':3,
#     'exlimit':3,
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

# try:
#     for k, v in PAGES.items():
#         print('story: ', v['extract'],' lien: ', v['fullurl'])
# except KeyError:
#     print("Désolé ")

output = process_question('openclassrooms')