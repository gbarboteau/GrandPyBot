import pytest
from .utils import Parser, GoogleMaps, Wikimedia, remove_html_tags
import config
import urllib.request

class TestParser:

    def test_parser_no_spaces(self):
        my_parser = Parser()
        sentence = my_parser.return_remove_spaces(" bonjour  tout  le monde  ")
        assert sentence == "bonjour tout le monde"

    def test_parser_punctuation(self):
        my_parser = Parser()
        sentence = my_parser.return_no_punctuation("openclassrooms !!!")
        assert sentence == "openclassrooms"

    def test_parser_stopwords(self):
        my_parser = Parser()
        sentence = my_parser.return_parsed("Bonjour Papy, dis-moi où est Openclassrooms ?")
        assert sentence == "openclassrooms"

    def test_googlemaps_get_adress(self, monkeypatch):
        my_googlemaps = GoogleMaps()
        my_adress_and_coordinates = my_googlemaps.get_address("openclassrooms")
        data = {
                "business_status": "OPERATIONAL",
                "formatted_address": "7 Cité Paradis, 75010 Paris, France",
                "formatted_phone_number": "01 80 88 80 30",
                "geometry": {
                    "location": {
                        "lat": 48.8748465,
                        "lng": 2.3504873
                    }
                },
                "id": "dd80dc7de1802674cba35cce4e303e6862a4f3ed",
                "reference": "ChIJIZX8lhRu5kcRGwYk8Ce3Vc8"
            }
        def mockreturn():
            return data
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert my_adress_and_coordinates == (data["formatted_address"], data["geometry"]["location"]["lat"], data["geometry"]["location"]["lng"])

    def test_wikimedia_get_story(self, monkeypatch):
        my_wikimedia = Wikimedia()
        my_summary = my_wikimedia.get_story("openclassrooms")
        data = {
                "pageid": 4338589,
                "ns": 0,
                "title": "OpenClassrooms",
                "extract": "<p class=\"mw-empty-elt\">\n</p>\n<p><b>OpenClassrooms</b> est un site web de formation en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur des métiers en croissance. Ses contenus sont réalisés en interne, par des écoles, des universités, des entreprises partenaires comme Microsoft ou IBM, ou historiquement par des bénévoles. Jusqu'en 2018, n'importe quel membre du site pouvait être auteur, via un outil nommé « interface de rédaction » puis « Course Lab ». De nombreux cours sont issus de la communauté, mais ne sont plus mis en avant. Initialement orientée autour de la programmation informatique, la plate-forme couvre depuis 2013 des thématiques plus larges tels que le marketing, l'entrepreneuriat et les sciences.\n</p><p>Créé en 1999 sous le nom de <b>Site du Zéro</b>, il se forme essentiellement sur la base de contributions de bénévoles proposant des tutoriels vulgarisés avec un ton léger portant sur des sujets informatiques divers. À la suite du succès et de la fin des études des gérants, l'entreprise Simple IT, renommée ensuite OpenClassrooms, est fondée dans le but de pérenniser le site. Celle-ci base son modèle économique sur la délivrance de certifications payantes et propose un abonnement pour être suivi par un mentor<sup class=\"reference cite_virgule\">,</sup>. Suite à ces changements, des utilisateurs créent un site web aux buts similaires, dont les auteurs et l'association le gérant sont uniquement bénévoles et ne propose pas de certifications (Zeste de Savoir).\n</p>"
            }
        def mockreturn():
            return data
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert my_summary == remove_html_tags(data["extract"])
