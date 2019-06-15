from grandpy.classes import Parsing
from grandpy import classes

# def test_ma_fonction_f_est_ok(monkeypatch):
#     def mock_g():
#         return "tout fonctionne"
#     monkeypatch.setattr('grandpy.demo.g',mock_g)
#     result = f()
#     assert result == "tout fonctionne"

# def test_ma_fonction_g_se_comporte_correctement():
#     result = g()
#     assert result == "tout fonctionne"
class Testparsing():

    def test_returnkeyword(self):
        result = Parsing("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
        assert result.returnkeyword() == "openclassrooms"

    def test_secondkeyword(self):
        result2 = Parsing("quelle est l'adresse de Versailles chantier ??%")
        assert result2.returnkeyword() == "Versailles chantier"
