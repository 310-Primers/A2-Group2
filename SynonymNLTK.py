from urllib.request import ProxyHandler
from nltk.corpus import wordnet as wn

synonyms = []
antonyms = []


def detectsyn(word):
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())

    print(set(synonyms))


detectsyn("phrase")

