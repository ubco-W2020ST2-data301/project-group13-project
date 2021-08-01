
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
    
    # drop columns + add new ones
    df2 = ( df1 
            .drop(drop_list,1)
    )
    
    return df2

# initial thoughts: Type of Event is highly correlated with Source and Substance

df2 = load_process_data('../../data/raw/SubstanceHarmsData.csv')
#print(df2.head(15))
#df2_profile = ProfileReport(df2).to_notebook_iframe()