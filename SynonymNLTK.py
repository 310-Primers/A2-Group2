from urllib.request import ProxyHandler
from nltk.corpus import wordnet as wn
from Chatbot import *

synonyms = []
antonyms = []



def detectsyn(word):
    for syn in wn.synsets(word):
        for w in syn.lemmas():
            synonyms.append(w.name())
        if w.antonyms():
            antonyms.append(w.antonyms()[0].name())

    print(set(synonyms))


detectsyn("phrase")

