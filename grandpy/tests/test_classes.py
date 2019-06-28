""" Test driven development file used to test classes file"""
from grandpy.classes import Parsing,Googlemap,Mediawiki
from grandpy import classes

import googlemaps
import googlemaps.client
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
    def test_adress_and_coordinates(self):
        """Check the output"""
        tested_keyword = Googlemap("tour eiffel")
        mock = 48.85837009999999, 2.2944813, 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France'  
        assert tested_keyword.http_results() == mock

class Testmediawiki:
    """ Check that the function return a short description \
        of a keyword or address from the mediawiki api """
    def test_text_returned_from_keyword(self):
        tested_keyword = Mediawiki("Montparnasse")
        mock2 = "Montparnasse est un toponyme parisien."
        assert tested_keyword.historytell() == mock2
    
    # def test_nothing_to_tell(self):
    #     tested_keyword2 = Mediawiki('tour eiffel')
    #     mock3 = "désolé mon petit mais je n'ai pas réussi à trouver ce lieu"
    #     assert tested_keyword2.historytell() == mock3