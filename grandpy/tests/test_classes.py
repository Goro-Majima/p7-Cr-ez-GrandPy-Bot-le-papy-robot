""" Test driven development file used to test classes file"""
from grandpy.classes import Parsing,Googlemap
from grandpy import classes

import googlemaps
import googlemaps.client
import urllib.request


class Testparsing:
    """ Check the parser"""
    def test_return_lowered_case(self):
        """Check if string is lowered"""
        result = Parsing("265 Avenue du Midi")
        assert result.returnkeyword() == "265 avenue midi"

    def test_no_punctuation_sentence(self):
        """check if the punctuation is removed"""
        result2 = Parsing("ou est l'adresse: de 5 rue de Versailles chantier ??%")
        assert result2.returnkeyword() == "5 rue versailles chantier"

    def test_request_to_grandpybot(self):
        """check if parsing is fully ok"""
        result3 = Parsing("Salut GrandPy ! Connais-tu l'adresse d'openclassrooms ? Merci !")   
        assert result3.returnkeyword() == "openclassrooms"

class Testgooglemaps:
