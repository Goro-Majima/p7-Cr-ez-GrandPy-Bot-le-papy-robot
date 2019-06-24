import re
import googlemaps
import googlemaps.client
import requests

from grandpy.stopwords import *
from config import *


class Parsing:
    """Parse user sentence into a keyword for an accurate research"""
    def __init__(self,question):
        self.question = question
        self.splittedquestion = []

    def returnkeyword(self):
        self.question = self.question.lower()
        self.question = self.question.replace("'",' ')
        self.question = re.sub(r'[?!%:]',"",self.question)
        self.question = re.sub(r'[-,]'," ",self.question)
        self.question = self.question.split()
        for word in self.question:
            if word not in STOPWORDS:
                self.splittedquestion.append(word)
        self.splittedquestion = ' '.join(self.splittedquestion)
        return self.splittedquestion

class Googlemap():
    """ Will return the coordiantes and the address asked by the user"""
    def __init__(self, splittedquestion):
        self.splittedquestion = splittedquestion
        self.address = str
        self.latitude = float
        self.longitude = float       

    def http_results(self):
        """ Return lattitude, longitude and address from given input"""
        gmaps = googlemaps.Client(key=SECRET_KEY)
        #Geocoding an address
        geocode_result = gmaps.geocode(self.splittedquestion)
        self.address = geocode_result[0]['formatted_address']  
        self.latitude = geocode_result[0]["geometry"]["location"]["lat"]
        self.longitude = geocode_result[0]["geometry"]["location"]["lng"]     
        return self.address, self.latitude, self.longitude

class Mediawiki:
    """ keyword will be used to find a short history of a place"""
    def __init__(self, splittedquestion):
        self.splittedquestion = splittedquestion
    
    def historytell(self):
        S = requests.Session()
        URL = "https://fr.wikipedia.org/w/api.php"

        TITLE = self.splittedquestion
        """choose de right parameters to get the first description of the place
        check https://www.mediawiki.org/wiki/Extension:TextExtracts#Caveats
        """
        PARAMS = {
            'action':"query",
            'prop':"extracts",
            'exsentences':1,
            'exlimit':1,
            'explaintext':True,
            'exsectionformat':'plain',
            'titles': TITLE,
            'format':"json"
            # "prop": "info",
            # 'inprop': 'url'
        }
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        PAGES = DATA['query']['pages']
        for k, v in PAGES.items():
            return v['extract']

