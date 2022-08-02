from cmath import inf
from logging import exception
from traceback import print_exc
from tracemalloc import stop
from typing import NewType
from unicodedata import name
from langcodes import tag_match_score
import pandas as pd
from pyparsing import Word
from sqlalchemy import true
from . import names
import re
import string
def cleanData(data_frame:pd.DataFrame) :
    """clean data for JobsRecoSystem (remove additional column, remove empty rows, bla bla bla ...)"""
    try:



        return data_frame
    except:
        print_exc()



def cleanEmbeddingData(data_frame:pd.DataFrame()):
    try:
        resultFrame:pd.DataFrame() = data_frame.copy()
        for i in resultFrame.index:
            row = resultFrame.loc[i, names.getJobDescription()]
            tempRow = toLower(row)
            tempRow = removePunctuation(tempRow)
            resultFrame.loc[i, names.getJobDescription()] = removeStopWords(tempRow)

        return resultFrame
    except:
       print_exc()




def toLower(text:str):
    '''converte text to lowercase'''
    return text.lower()

################################################################

import inflect
p = inflect.engine()

reg = r'([0-9]+)'

def isFloat(v):
    try:
        float(v)
        return true
    except:
        return False

def converteNumbers(text):
    '''coverte text numbers to words'''
    tempText = text.split()
    NewText = []
    try:

        for word in tempText:
            tempNumList = re.split(reg, word)
            for miniword in tempNumList:
                if miniword.isdigit() or isFloat(miniword):
                    temp = p.number_to_words(miniword)
                    NewText.append(temp)
                else:
                    NewText.append(miniword)

        tempText = ' '.join(NewText)
    except:
        print_exc()

    return tempText


########################################################################



translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
def removePunctuation(text:str):
    ''' remove punctuation from text'''

    global translator
    return text.translate(translator)

########################################################################

def removeWhiteSpace(text:str):
    return " ".join(text.split())


########################################################################

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def removeStopWords(text:str):
    sw = set(stopwords.words("english"))
    wt = word_tokenize(text)
    filteredText = [word for word in wt if not word in sw]
    return ' '.join(filteredText)

########################################################################

from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
def stemWords(text:str):
    global stemmer
    wt = word_tokenize(text)
    stems = []
    for word in wt:
        temp = stemmer.stem(word)
        stems.append(temp)
    return ' '.join(stems)

########################################################################

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk import pos_tag, defaultdict

lmtzr = WordNetLemmatizer()

tag_map = defaultdict(lambda: wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

def lemmtizeWords(text:str):
    tokens = word_tokenize(text)
    lemmas = [lmtzr.lemmatize(token, tag_map[tag[0]]) for token, tag in pos_tag(tokens) ]
    return ' '.join(lemmas)


