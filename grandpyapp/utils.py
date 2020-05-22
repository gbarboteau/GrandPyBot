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
        self.clean_sentence = self.return_no_punctuation(sentence.lower())
        self.clean_sentence = self.return_remove_spaces(self.clean_sentence)
        self.sentenceWords = self.clean_sentence.split()
        self.newWords = [word for word in self.sentenceWords if word not in self.stopwords]
        self.newSentence = " ".join(self.newWords)
        # self.newSentence = self.return_no_punctuation(self.newSentence)
        # self.newSentence = self.return_remove_spaces(self.newSentence)
        return self.newSentence

    def return_no_punctuation(self, sentence):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        self.sentence_without_punctuation = ""
        for char in sentence:
            if char not in punctuations:
                self.sentence_without_punctuation = self.sentence_without_punctuation + char
            else: 
                self.sentence_without_punctuation = self.sentence_without_punctuation + " "
        self.sentence_without_punctuation = self.return_remove_spaces(self.sentence_without_punctuation)
        return self.sentence_without_punctuation

    def return_remove_spaces(self, sentence):
        # self.new_words = sentence.split(" ")
        self.new_words = [words.strip() for words in sentence.split(" ")]
        # self.new_sentence = " ".join(self.new_words)
        self.new_sentence = ""
        for i in range(0, len(self.new_words)):
            if self.new_words[i] != '':
                self.new_sentence = self.new_sentence + self.new_words[i] + " "
        self.new_sentence = self.new_sentence[0:-1]
        return self.new_sentence


class GoogleMaps():
    def get_address(self, search):
        myRequest = requests.get(GOOGLE_MAP_ADRESS + "?key=" + GOOGLE_MAP_KEY + "&inputtype=textquery&input=" + search)
        myInfos = myRequest.json()
        myPlaceID = myInfos['candidates'][0]['place_id']
        myAddressRequest = requests.get(GOOGLE_MAP_GEOCACHE + "?key=" + GOOGLE_MAP_KEY + "&place_id=" + myPlaceID)
        myAddress = myAddressRequest.json()
        myAdressFormatted = myAddress['result']['formatted_address']
        latitude = myAddress["result"]["geometry"]["location"]["lat"]
        longitude = myAddress["result"]["geometry"]["location"]["lng"]
        print(myAdressFormatted, latitude, longitude)
        return(myAdressFormatted, latitude, longitude)


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
