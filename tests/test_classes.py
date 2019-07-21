""" Test driven development file used to test classes file"""
from grandpy.classes import Parsing,Googlemap,Mediawiki
from grandpy import classes

# import googlemaps
# import googlemaps.client
import urllib.request

class Testparsing:
    """ Check if the parser return a filtered keyword for a geo search """
    def test_return_lowered_case(self):
        """Check if string is lowered"""
        result = Parsing("265 Avenue du Midi")
        assert result.returnkeyword() == "265 avenue midi"

    def test_no_punctuation_sentence(self):
        """check if the punctuation is removed """
        result2 = Parsing("ou est l'adresse: de 5 rue de Versailles chantier ??%")
        assert result2.returnkeyword() == "5 rue versailles chantier"

    def test_request_to_grandpybot(self):
        """check if parsing is fully ok"""
        result3 = Parsing("Salut GrandPy ! Connais-tu l'adresse d'openclassrooms ? Merci !")   
        assert result3.returnkeyword() == "openclassrooms"

class Testgooglemaps:
    """ Check what the function return from the google api """
    def test_return_adress_and_coordinates(self, monkeypatch):
        """Check the output"""
        tested_keyword = Googlemap("tour eiffel")
        results = 48.85837009999999, 2.2944813, 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France'  
        def mockreturn(request, params):
            return results
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert tested_keyword.http_results() == results

class Testmediawiki:
    """ Check that the function return a short description \
        of a keyword or address from the mediawiki api """
    def test_text_returned_from_keyword(self,monkeypatch):
        tested_keyword = Mediawiki(48.8748465, 2.3504873)
        results = "L'Hôtel Bourrienne (appelé aussi Hôtel de Bourrienne et Petit Hôtel Bourrienne) est un hôtel particulier du XVIIIe siècle situé au 58 rue d'Hauteville dans le 10e arrondissement de Paris. Propriété privée, il est classé au titre des monuments historiques depuis le 20 juin 1927.", 'https://fr.wikipedia.org/wiki/H%C3%B4tel_Bourrienne' 
        def mockreturn(request, params):
            return results
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert tested_keyword.historytell() == results
    