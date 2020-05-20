# coding: utf-8
import sys
import re
from config import STOP_WORDS, GOOGLE_MAP_ADRESS, GOOGLE_MAP_GEOCACHE, GOOGLE_MAP_KEY, WIKIPEDIA_ADDRESS, WIKIPEDIA_PAGE
import json
import requests 


class Parser():
    def __init__(self):
        self.sentenceWords = ""
        with open(STOP_WORDS, encoding='utf-8') as f:
            self.stopwords = json.load(f)
        self.newWords = ""
        self.newSentence = ""

    def return_parsed(self, sentence):
        self.sentenceWords = sentence.split()
        self.newWords = [word for word in self.sentenceWords if word not in self.stopwords]
        self.newSentence = " ".join(self.newWords)
        return self.newSentence

class GoogleMaps():
    def get_address(self, search):
        myRequest = requests.get(GOOGLE_MAP_ADRESS + "?key=" + GOOGLE_MAP_KEY + "&inputtype=textquery&input=" + search)
        myInfos = myRequest.json()
        myPlaceID = myInfos['candidates'][0]['place_id']
        myAddressRequest = requests.get(GOOGLE_MAP_GEOCACHE + "?key=" + GOOGLE_MAP_KEY + "&place_id=" + myPlaceID)
        myAddress = myAddressRequest.json()
        myAdressFormatted = myAddress['result']['formatted_address']
        print(myAdressFormatted)
        return(myAdressFormatted)

class Wikimedia():
    def get_story(self, myTitle):
        myRequest = requests.get(WIKIPEDIA_ADDRESS + myTitle)
        myInfos = myRequest.json()
        myPage = myInfos['query']['search'][0]['title']
        myOtherRequest = requests.get(WIKIPEDIA_PAGE + myPage)
        myNewInfos = myOtherRequest.json()
        myPageID = list(myNewInfos['query']['pages'])[0]
        myExtract = myNewInfos['query']['pages'][str(myPageID)]['extract']
        myExtract = remove_html_tags(myExtract)
        return(myExtract)


def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
