# coding: utf-8
import sys
from config import STOP_WORDS as stopwords
import json

def parse(sentence):
	sentenceWords = sentence.split()
	with open('fr.json', encoding='utf-8') as f:
		stopwords = json.load(f)
	print(stopwords)
	newWords = [word for word in sentenceWords if word not in stopwords]
	newSentence = " ".join(newWords)
	print(newSentence)
	return newSentence

parse(sys.argv[-1])