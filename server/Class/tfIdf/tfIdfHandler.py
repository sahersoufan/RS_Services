from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
from ..rsCore import names







def makeTfIdfMatrix(data_frame:pd.DataFrame):
    """
    here we build the tf-idf matrix with TfidfVectorizer from sklear and return the matrix
    """
    try:
        tfidf = TfidfVectorizer(stop_words='english', lowercase=True)
        if data_frame[names.getJobDescription()].isnull().values.any():
            data_frame[names.getJobDescription()] = data_frame[names.getJobDescription()].fillna("")
        tfIdfMatrix = tfidf.fit_transform(data_frame[names.getJobDescription()])
        return tfIdfMatrix, tfidf.vocabulary_
    except:
        print("error in makeTfIdfMatrix() from tfIdfHandler module")
        raise Exception


def updateTfIdfMatrix(data_frame:pd.DataFrame, vocabulary):
    """
    here we update the tf-idf matrix with TfidfVectorizer from sklear and return the matrix
    """
    try:
        tfidf = TfidfVectorizer(stop_words='english', lowercase=True, vocabulary=vocabulary)
        if data_frame[names.getJobDescription()].isnull().values.any():
            data_frame[names.getJobDescription()] = data_frame[names.getJobDescription()].fillna("")
        tfIdfMatrix = tfidf.fit_transform(data_frame[names.getJobDescription()])
        return tfIdfMatrix, tfidf.vocabulary_
    except:
        print("error in updateTfIdfMatrix() from tfIdfHandler module")
        raise Exception



def makeCosSim(tfidfMatrix):
    """ build a table of cosine similarity from the tf idf matrix"""
    cosine_sim = linear_kernel(tfidfMatrix, tfidfMatrix)
    return cosine_sim

def makeJobsIndices(data : pd.DataFrame):
    """make indices from ids"""
    indicies = pd.DataFrame(data=data['id'])
    indicies.rename(columns={'id':'jobsId'}, inplace=True)
    indicies['simId'] = indicies.index.values
    indicies.set_index('jobsId', inplace=True)
    return indicies

