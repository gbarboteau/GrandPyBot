# To generate a new secret key:
import os

SECRET_KEY = os.environ['SECRET_KEY']

basedir = os.path.abspath(os.path.dirname(__file__))

STOP_WORDS = os.path.join(basedir, 'grandpyapp', 'scripts', 'fr-improved.json')

GREETINGS_PHRASES = ["Bonjour mon petit fardadet des étoiles ! Où veux-tu que je t'emmènes ?" ,"Salutations ma petite douceur de Pologne ! Quel endroit souhaites-tu explorer ?", "Dis-moi petit canard des îles... Que veux-tu savoir ?"]
PLACE_PHRASES = ["Je connais cet endroit, ô divin tiramisu !", "Ca me dit quelque chose, loukoum de Normandie !", "J'y suis allé samedi dernier, petit éclair au matcha !"]
WIKI_PHRASES = ["Connais-tu l'histoire de ce lieu, petite côté de boeuf ?", "Je vais te raconter une histoire sur cette endroit, sacré couscous à la merguez !", "Le savais-tu, petit artichaut fourré au beurre salé ?"]


GOOGLE_MAP_KEY = os.environ['GOOGLE_MAP_KEY']
GOOGLE_MAP_ADRESS = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
GOOGLE_MAP_GEOCACHE = "https://maps.googleapis.com/maps/api/place/details/json"
WIKIPEDIA_ADDRESS = "https://fr.wikipedia.org/w/api.php?action=query&format=json&list=search&srlimit=1&srsearch="
WIKIPEDIA_PAGE = "http://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&format=json&titles="