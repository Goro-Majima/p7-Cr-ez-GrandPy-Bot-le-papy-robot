import re
import googlemaps
import googlemaps.client
from grandpy.stopwords import *


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
    def __init__(self):
        self.address = address
        self.latitude = latitude
        self.longitude = longitude       

    def http_results(self, splittedquestion):
        """ Return lattitude, longitude and address from given input"""
        gmaps = googlemaps.Client(key="AIzaSyAOXqgCFDowOEhWXY_IIUjuupg8nmHkSek")
        #Geocoding an address
        geocode_result = gmaps.geocode(splittedquestion)
        self.address = geocode_result[0]['formatted_address']
        self.latitude = geocode_result[0]["geometry"]["location"]["lat"]
        self.longitude = geocode_result[0]["geometry"]["location"]["lng"]       
        return self.address, self.latitude, self.longitude