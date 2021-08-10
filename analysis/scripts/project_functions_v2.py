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
    return df2

					  
        
# for rhys' analysis
def load_process_rdata(path_to_file):
    
    # Load Data into df3
    df3 = (
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
    source_reassign = {
        "Deaths" : 1,
        "Hospitalizations": 2,
        "Emergency Medical Services (EMS)":3
    }
    
    # drop columns, reassign
    df4 = ( df3 
            .drop(drop_list,1)
    )
    
    df4['Event Category'] = df4['Type of Event'].apply(lambda x: event_reassign[x])
    df4['Substance'] = df4['Substance'].apply(lambda x: substance_key[x])
    df4['Source_number'] = df4['Source'].apply(lambda x: source_reassign[x])
    
    return df2
# Make sure to return the latest dataframe
    
    

 
	