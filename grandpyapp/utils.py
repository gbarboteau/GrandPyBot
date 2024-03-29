# coding: utf-8
import sys, re, json, requests
from config import STOP_WORDS, GOOGLE_MAP_ADRESS, GOOGLE_MAP_GEOCACHE, GOOGLE_MAP_KEY, WIKIPEDIA_ADDRESS, WIKIPEDIA_PAGE


class Parser():
    """A parser removing words from a given
    sentence.
    """
    def __init__(self):
        """Init the parser"""
        self.sentenceWords = ""
        with open(STOP_WORDS, encoding='utf-8') as f:
            self.stopwords = json.load(f)
        self.newWords = ""
        self.newSentence = ""

    def return_parsed(self, sentence):
        """Return a sentence without the stop words"""
        self.clean_sentence = self.return_no_punctuation(sentence.lower())
        self.clean_sentence = self.return_remove_spaces(self.clean_sentence)
        self.sentenceWords = self.clean_sentence.split()
        self.newWords = [word for word in self.sentenceWords if word not in self.stopwords] #Remove any words among the stop word lists
        self.newSentence = " ".join(self.newWords)
        return self.newSentence

    def return_no_punctuation(self, sentence):
        """Return a sentence without any punctuation"""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' #the list of unwanted characters
        self.sentence_without_punctuation = ""
        for char in sentence:   #Add a character to a string if it's not an unwanted character
            if char not in punctuations:
                self.sentence_without_punctuation = self.sentence_without_punctuation + char
            else: 
                self.sentence_without_punctuation = self.sentence_without_punctuation + " "
        self.sentence_without_punctuation = self.return_remove_spaces(self.sentence_without_punctuation)
        return self.sentence_without_punctuation

    def return_remove_spaces(self, sentence):
        """Remove useless whitespaces"""
        self.new_words = [words.strip() for words in sentence.split(" ")]
        self.new_sentence = ""
        for i in range(0, len(self.new_words)):  #Recompose a sentence so there is no useless whitespace
            if self.new_words[i] != '':
                self.new_sentence = self.new_sentence + self.new_words[i] + " "
        self.new_sentence = self.new_sentence[0:-1]
        return self.new_sentence


class GoogleMaps():
    """An instance of an object using the
    Google Map API.
    """
    def get_address(self, search):
        """Get an adress and its coordinates from a name"""
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
    """An instance of an object using the
    Wikimedia API.
    """
    def get_story(self, myTitle):
        """Return the extract of a Wikipedia article"""
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
