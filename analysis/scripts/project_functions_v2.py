# import all required module
import pandas as pd
	
def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)
    # Clean Data: remove selected rows with NULL values
    df = pd.read_csv(url_or_path_to_csv_file)
    df1 = pd.DataFrame(df.dropna(subset=['Substance', 'Source', 'Region', 'Time_Period', 'Unit', 'Value',]))
	#df1 = (pd.read_csv(url_or_path_to_csv_file).dropna(axis=1, how='all'))
	
    # Method Chain 2 (Create new columns, drop others, and do processing)
    # Clean Data: check for errors in the data and remove unused data
    # 1. remove un-used columns (PRUID, Specific_Measure, Aggregator, )
    # 2. remove all rows that contain "Canada" in column['Region']
    # 3. remove all rows that contain "By year" in column['Time_Period']
    df2 = pd.DataFrame(df1.drop(['PRUID', 'Specific_Measure', 'Aggregator'], axis=1)                      
                          .drop(index=df.loc[lambda x: (x['Region'].str.contains('Canada')) | (x['Time_Period'].str.contains('By quarter')) 
                          | (~x['Unit'].str.contains('Number' )) | (x['Value'].str.contains('Suppressed')) | (x['Value'].str.contains('Not available'))
                          | (~x['Type_Event'].str.contains('Total apparent opioid toxicity deaths')) ].index)
						  .reset_index()
                          .drop('index', axis=1) 
                      )


					  
    # Make sure to return the latest dataframe

    return df2 
	