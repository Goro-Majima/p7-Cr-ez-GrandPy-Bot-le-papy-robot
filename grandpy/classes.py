"""This file contains the Parsing function and define the use of APIs"""
import re
from random import randrange
import requests

from grandpy.stopwords import *
from config import *


class Parsing:
    """Parse user sentence into a keyword for an accurate research"""
    def __init__(self, question):
        self.question = question
        self.splittedquestion = []
    def returnkeyword(self):
        """clean the question to create a keyword"""
        self.question = self.question.lower()
        self.question = self.question.replace("'", ' ')
        self.question = re.sub(r'[?!%:]', "", self.question)
        self.question = re.sub(r'[-,]', " ", self.question)
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
        session = requests.Session()
        key = SECRET_KEY
        url = "https://maps.googleapis.com/maps/api/geocode/json"

        splitted = self.splittedquestion

        params = {
            'address': splitted,
            'key': key,
            'region':'fr'
        }
        req = session.get(url=url, params=params)
        data = req.json()
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
        address = data['results'][0]['formatted_address']
        return lat, lng, address

class Mediawiki:
    """ keyword will be used to find a short history of a place"""
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def historytell(self):
        """call api from wiki url, add lat and lng from google API"""
        session = requests.Session()
        url = "https://fr.wikipedia.org/w/api.php"
        #https://www.coordonnees-gps.fr/
        params = {
            'action':"query",
            'list':"geosearch",
            'gscoord': str(self.latitude) + "|" + str(self.longitude),
            'gsradius':1000,
            'gslimit':1,
            'format':"json"
        }
        req = session.get(url=url, params=params)
        data = req.json()
        places = data['query']['geosearch']
        title = places[0]['title']
        #actually get the closest to given coordinates but what if not accurate coordinates ?
        """choose de right parameters to get the first description of the place
        check https://www.mediawiki.org/wiki/Extension:TextExtracts#Caveats"""
        params = {
            'action':"query",
            'exsentences':2,
            'exlimit':2,
            'explaintext':True,
            'exsectionformat':'plain',
            'titles': title,
            'format':"json",
            'prop':"extracts|info",
            'inprop': 'url'
        }
        req = session.get(url=url, params=params)
        data = req.json()
        pages = data['query']['pages']
        for key, args in pages.items():
            return args['extract'], args['fullurl']

class Answer:
    def addressfound():
        """return a random message if address is found"""
        addressfoundlist = ["Tiens mon enfant, je te montre l'addresse: ",\
            "Aussitot dit, aussitôt trouvé ! ", \
            "C'est bien cet endroit que tu m'as demandé de trouver ?", \
            "Je pense que tu cherches cette place: "]
        return addressfoundlist[randrange(4)]

    def nothingfound():
        """return a random message if address is not found"""
        nothinglist = ["Soit tu ne sais pas écrire ou soit ce n'est pas du français \
            mais ce n'est pas ma faute si je n'ai rien trouvé !! ",\
         "Pas de réponse!! Concentre toi pour formuler une question basique !",\
         "Je crois avoir la réponse mais ta question n'est pas claire",\
         "Plus de précision je t'en prie"]
        return nothinglist[randrange(4)]

    def nomediawiki():
        """return a random message if no story found"""
        nowikilist = ["C'est très rare que je dise cela mais j'ai tout oublié à propose de cet endroit",\
        "C'est pas que je n'ai pas d'histoire à raconter mais je n'ai tout simplement pas envie !",\
            "Rien à raconter sur cet endroit, trop dangereux je n'ai pas osé y aller."]
        return nowikilist[randrange(4)]

    def storyfound():
        """return a random message if story is found"""
        wikilist = ["Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? ", \
            "Oh je me rappelle de cet endroit, j'ai un tas de choses à raconter alors accroche toi: ",\
            "Ce lieu ravive des souvenirs les plus enfouis, laisse moi te conter ce que j'en sais", \
                "Je serai heureux de t'y emmener mais en attendant tu vas écouter ma story:"]
        return wikilist[randrange(4)]
