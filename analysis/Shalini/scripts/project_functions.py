# import all required module
import pandas as pd
import seaborn as sns
import numpy as np
import os
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport
	
def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)
    # Clean Data: remove selected rows with NULL values
    df = pd.read_csv(url_or_path_to_csv_file)
    df1 = pd.DataFrame(df.dropna(subset=['Substance', 'Source', 'Region', 'Time_Period','Unit','Value'])             
                      )
    
    # Method Chain 2 (Create new columns, drop others, and do processing)
    # Clean Data: check for errors in the data and remove unused data
    # 1. remove un-used columns (Type_Event, Aggregator, Disaggregator, Unit, Value)
    # 2. remove all rows that contain "Canada" in column['Region']
    # 3. remove all rows that contain "By year" in column['Time_Period']
    df2 = pd.DataFrame(df1.drop(['PRUID', 'Specific_Measure', 'Aggregator', 'Disaggregator'], axis=1)
                          .reset_index()
                          .drop('index', axis=1)                       
                          .drop(index=df.loc[lambda x: (x['Region'].str.contains('Canada')) | (x['Time_Period'].str.contains('By quarter')) 
                          | (~x['Unit'].str.contains('Number' )) | (x['Value'].str.contains('Suppressed')) | (x['Value'].str.contains('Not available'))
                          | (~x['Type_Event'].str.contains('Total apparent opioid toxicity deaths')) ].index)              
                      )

    # Make sure to return the latest dataframe

    return df2 
	

	
def test(url_or_path_to_csv_file):
# Load Data: Read data from file 'filename.csv' 
	df = pd.read_csv(url_or_path_to_csv_file)

# Clean Data: check for errors in the data and remove unused data
# 1. remove rows with NULL values
# 2. remove un-used columns (Type_Event, Aggregator, Disaggregator, Unit, Value)
# 3. remove all rows that contain "Canada" in column['Region']
# 4. remove all rows that contain "By year" in column['Time_Period']

#Search_for_These_values = ['Total apparent opioid toxicity deaths','Total apparent stimulant toxicity deaths'] 
#pattern = '|'.join(Search_for_These_values)


# Create the DataFrame and run the process to clean the data
	df2 = pd.DataFrame(df.drop(['PRUID', 'Specific_Measure', 'Aggregator', 'Disaggregator'], axis=1)
                         .dropna(subset=['Substance', 'Source', 'Region', 'Time_Period','Unit','Value'])
                         .reset_index()
                         .drop('index', axis=1)
                         .drop(index=df.loc[lambda x: (x['Region'].str.contains('Canada')) | (x['Time_Period'].str.contains('By quarter')) 
                         #| (x['Value'].str.contains('Suppressed')) | (x['Value'].str.contains('Not available'))
                         | (~x['Unit'].str.contains('Number' )) | (x['Value'].str.contains('Suppressed')) | (x['Value'].str.contains('Not available'))
                         | (~x['Type_Event'].str.contains('Total apparent opioid toxicity deaths')) ].index)              
                         #| (~x['Type_Event'].str.contains('Total apparent opioid toxicity deaths' & 'Total apparent stimulant toxicity deaths')) ].index) 
                         #.drop(index=df.loc[lambda x: (x['Region'].str.contains('Canada')) ].index)
                         #.drop(index=df.loc[lambda x: (~x['Region'].str.contains('British Columbia')) | (x['Time_Period'].str.contains('By quarter')) | (~x['Year_Quarter'].str.contains('2020'))
                         #| (~x['Unit'].str.contains('Number')) | (~x['Source'].str.contains('Deaths'))].index) 
                         #.drop(index=df.loc[lambda x: (~x['Unit'].str.contains('Number')) | (~x['Source'].str.contains('Deaths'))].index) 
                
                  )

	return df2