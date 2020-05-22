from flask import Flask, render_template, url_for, request, jsonify
from .utils import Parser, GoogleMaps, Wikimedia
from random import randint
import config, json, random

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
@app.route("/index/")
def index():
    hello_phrase = random.choice(config.GREETINGS_PHRASES)
    return render_template('index.html', hello_phrase=hello_phrase, GOOGLE_MAP_KEY=config.GOOGLE_MAP_KEY)


@app.route('/search', methods=['GET'])
def search():
    userText = request.args.get('text')
    myParser = Parser()
    myMap = GoogleMaps()
    myWiki = Wikimedia()
    search = myParser.return_parsed(userText)
    place_phrase = random.choice(config.PLACE_PHRASES)
    wiki_phrase = random.choice(config.WIKI_PHRASES)
    print(search)
    try:
        info_id, latitude, longitude = myMap.get_address(search)
        try:
            MyDesc = myWiki.get_story(search)
        except:
            MyDesc = ""
            wiki_phrase = "Je ne trouve pas d'histoire lié ! Gomendozei !!! é_è"
        print(MyDesc)
    except:
        info_id = ""
        latitude = ""
        longitude =""
        place_phrase = "Je ne comprends pas ce que tu me dis caneton !"
        MyDesc = ""
        wiki_phrase = ""
    print(info_id, latitude, longitude)
    return json.dumps({"MyDesc":MyDesc, "info_id":info_id, "latitude":latitude, "longitude":longitude, "place_phrase":place_phrase, "wiki_phrase":wiki_phrase, "GOOGLE_MAP_KEY":config.GOOGLE_MAP_KEY})


if __name__ == "__main__":
    app.run()