from grandpy.classes import Parsing
from grandpy import classes

class Testparsing():

    def test_return_lowered_case(self):
        result = Parsing("265 Avenue du Midi")
        assert result.returnkeyword() == "265 avenue midi"

    def test_no_punctuation_sentence(self):
        result2 = Parsing("ou est l'adresse: de 5 rue de Versailles chantier ??%")
        assert result2.returnkeyword() == "5 rue versailles chantier"

    def test_request_to_grandpybot(self):
        result3 = Parsing("Salut GrandPy ! Connais-tu l'adresse d'openclassrooms ? Merci !")   
        assert result3.returnkeyword() == "openclassrooms"

    def test_request_to_grandpybot2(self):
        result4 = Parsing("ou se trouve notre dame ?")   
        assert result4.returnkeyword() == "notre dame"

class Testgooglemaps():
    
    def 