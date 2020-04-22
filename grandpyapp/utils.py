# coding: utf-8
import sys
from config import STOP_WORDS
import json

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
