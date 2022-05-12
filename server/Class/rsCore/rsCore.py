from json import load
from logging import exception
import numpy as np
import pandas as pd
import pickle
import os
from . import cleaningHelper
from ..sqlConnection import dbHandler
from ..tfIdf import tfIdfHandler
from . import names

#variables#
cosSim:np.ndarray = None
indicies:pd.DataFrame = None



def initiate():
    """get a hole data and build the recoSys from point zero with new db"""
    try:
        print('get data from db')
        
        data = pd.read_sql('jobs', con=dbHandler.engine, columns=[names.getJobId(), names.getJobDescription()])
        data_frame = pd.DataFrame(data)
        print('data is here, now we will clean it :)')
        
        data_frame = cleaningHelper.cleanData(data_frame)
        print('data cleanned, building tfidf matrix')
        
        tfidfM, voc = tfIdfHandler.makeTfIdfMatrix(data_frame=data_frame)
        print('tfidf matrix is here, now we build cosin similarity and indicies')
        
        global cosSim, indicies
        cosSim = tfIdfHandler.makeCosSim(tfidfM)
        indicies = tfIdfHandler.makeJobsIndices(data_frame)
        print('cosin similarity and indicies are done, saving the vocabulary')
        
        if(os.path.exists(os.path.join(os.getcwd(), names.getVoc()))):
            os.remove(os.path.join(os.getcwd(), names.getVoc()))
        pickle.dump(voc, open(os.path.join(os.getcwd(), names.getVoc()), "wb"))
        print('saving is done')
    except:
        print('error in initiate func')
        raise exception

def update():
    """update the reco system """
    try:
        print('get data from db')
        data = pd.read_sql('jobs', con=dbHandler.engine, columns=[names.getJobId(), names.getJobDescription()])
        data_frame = pd.DataFrame(data)
        print('data is here, now we will clean it :)')
        
        data_frame = cleaningHelper.cleanData(data_frame)
        print('data cleanned, building tfidf matrix')
        
        savedVocabulary = pickle.load(open(os.path.join(os.getcwd(), names.getVoc()), "rb"))
        tfidfM,voc = tfIdfHandler.updateTfIdfMatrix(data_frame=data_frame, vocabulary=savedVocabulary)
        print('tfidf matrix is here, now we build cosin similarity and indicies')

        global cosSim, indicies
        cosSim = tfIdfHandler.makeCosSim(tfidfM)
        indicies = tfIdfHandler.makeJobsIndices(data_frame)
        print('cosin similarity and indicies are done, saving the vocabulary')

        if(os.path.exists(os.path.join(os.getcwd(), names.getVoc()))):
            os.remove(os.path.join(os.getcwd(), names.getVoc()))
        pickle.dump(voc, open(os.path.join(os.getcwd(), names.getVoc()), "wb"))
        print('saving is done')
        return True
    except:
        print('error in update func')
        raise exception



def getRecommend(userData : dict):
    """get a recommendation"""
    services = {'id' : []}
    for id in userData.get('id'):
        ids = indicies.iloc[indicies.index == id].values[0][0]
        simScores = enumerate(cosSim[ids])
        simScores = sorted(simScores, key=lambda x: x[1], reverse=True)
        simScores = simScores[1:10]

        simIndex = [i[0] for i in simScores]
        services.get('id').append(simIndex)
    return services


