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
    return render_template('index.html', hello_phrase=hello_phrase)


@app.route('/search', methods=['GET'])
def search():
    userText = request.args.get('text')
    myParser = Parser()
    myMap = GoogleMaps()
    myWiki = Wikimedia()
    search = myParser.return_parsed(userText)
    place_phrase = random.choice(config.PLACE_PHRASES)
    wiki_phrase = random.choice(config.WIKI_PHRASES)
    try:
        info_id = myMap.get_address(search)
        print(info_id)
        try:
            MyDesc = myWiki.get_story(search)
        except:
            MyDesc = "Je ne trouve pas d'histoire lié ! Gomendozei !!! é_è"
        print(MyDesc)
    except:
        info_id = "Oups ! Je n'ai pas compris, peux-tu réeesayer ?"
        MyDesc = ""
    return json.dumps({"MyDesc":MyDesc, "info_id":info_id, "place_phrase":place_phrase, "wiki_phrase":wiki_phrase})


if __name__ == "__main__":
    app.run()