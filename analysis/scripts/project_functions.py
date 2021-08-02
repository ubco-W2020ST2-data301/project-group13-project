# first, import the pertinent libraries/packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

from pandas_profiling import ProfileReport

"""
our csv contains aggregate/disaggregate columns. Since we'll be doing our own processing, we'll
drop these and focus on our own aggregates/processing
"""

def load_process_data(path_to_file):
    
    # Load Data into df1
    df1 = (
        pd.read_csv(path_to_file) #load data
        .dropna(axis=1,how='all') #drop columns with all NaN values
        .dropna(subset=['Substance','Source', 'Type_Event','Specific_Measure','Region','Unit','Value']) #drop rows with missing pertinent values
        .rename(columns={"Specific_Measure":"Specific Measure","Type_Event":"Type of Event"}) #rename some columns
        .reset_index(drop=True)
    )
    
    drop_list = ["PRUID","Year_Quarter","Time_Period","Value","Aggregator","Unit","Specific Measure","Disaggregator"]
    event_reassign = {
        "Total apparent opioid toxicity deaths":1,
        "Accidental apparent opioid toxicity deaths":2,
        "Suicide apparent opioid toxicity deaths":3,
        "Total opioid-related poisoning hospitalizations":4,
        "Accidental opioid-related poisoning hospitalizations":5,
        "Intentional opioid-related poisoning hospitalizations":6,
        "EMS responses to suspected opioid-related overdoses":7,
        "Total apparent stimulant toxicity deaths":8,
        "Accidental apparent stimulant toxicity deaths":9,
        "Accidental stimulant-related poisoning hospitalizations":10,
        "Total stimulant-related poisoning hospitalizations":11,
        "Intentional stimulant-related poisoning hospitalizations":12
    }
    substance_key = {"Opioids":1,"Stimulants":2}
    
    # drop columns, reassign
    df2 = ( df1 
            .drop(drop_list,1)
    )
    
    df2['Event Category'] = df2['Type of Event'].apply(lambda x: event_reassign[x])
    df2['Substance'] = df2['Substance'].apply(lambda x: substance_key[x])
    return df2

# initial thoughts: Type of Event is highly correlated with Source and Substance

df2 = load_process_data('../../data/raw/SubstanceHarmsData.csv')
# checking unique events
#list_ = pd.unique(df2['Type of Event'])
#print(list_)

#checking df2 information
#print(df2.tail(15))
#df2_profile = ProfileReport(df2).to_notebook_iframe()


