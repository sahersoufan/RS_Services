import pandas as pd
from . import names

def cleanData(data_frame:pd.DataFrame) :
    """clean data for JobsRecoSystem (remove additional column, remove empty rows, bla bla bla ...)"""
    try:
        # data_frame = data_frame.iloc[:][[names.getJobTitle(),names.getJobTitle()]]
        # data_frame.set_index(names.getJobTitle(), inplace=True)
        # #TODO do it with ID please

# there is nothing to do here right now


        return data_frame
    except:
        raise Exception