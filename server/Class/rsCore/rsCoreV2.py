from dataclasses import dataclass

import numpy as np
from . import names
from . import cleaningHelper 
from ..sqlConnection import dbHandler
from ..embedding import embeddingHandler

import pandas as pd
from traceback import print_exc



pureData = None
def initiate():
    """get a hole data and build the recoSys v2 from point zero with new db"""
    try:
        global pureData
        print('get data from db')
        
        pureData = pd.read_sql(names.getServiceModel(), con=dbHandler.engine, columns=[names.getJobId(), names.getJobDescription()])
        print('data is here, now we will clean it :)')
        
        data_frame = cleaningHelper.cleanEmbeddingData(pureData)
        print('data cleanned, building word2vec model...')

        embeddingHandler.initializeModel(data_frame)
        embeddingHandler.makeVectors(data_frame)
        embeddingHandler.buildCosinSim(data_frame)

    except:
        print_exc()



def update():
    """update the reco system v2 """

    try:
        global pureData
        print('get data from db')
        
        pureData = pd.read_sql(names.getServiceModel(), con=dbHandler.engine, columns=[names.getJobId(), names.getJobDescription()])
        print('data is here, now we will clean it :)')
        
        data_frame = cleaningHelper.cleanEmbeddingData(pureData)
        print('data cleanned, building word2vec model...')

        embeddingHandler.updateModel(data_frame)
        embeddingHandler.makeVectors(data_frame)
        embeddingHandler.buildCosinSim(data_frame)

    except:
        print_exc()


# {
#     "id": [
#         34
#     ]
# }

def getRecommend(userData : dict):
    """get a recommendation"""
    global indicies
    services = {'id' : []}
    for id in userData.get('id'):
        try:
            ids = pureData.index[pureData[names.getJobId()] == id].tolist()[0]
            result = embeddingHandler.getSimilar(ids)
            
            lis:np.ndarray = result.argsort(axis = 0)[-11:][::-1]
            lis = lis[1:]
            #TODO remember to Check this
            for i in lis:
                services.get('id').append(int(pureData.iloc[i, 0]))
        
        except Exception:
            print_exc()
    return services
    

