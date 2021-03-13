import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    

    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .dropna()
        .drop(['VotingAgeCitizen','Office','Drive','Carpool','Transit','Walk','Service','Construction'], axis ="columns")
    )

    df2 = (
        df1
        .loc[(df1['State'] == 'Florida') | (df1['State'] == 'Texas')|(df1['State'] == 'California')|(df1['State'] == 'New York')]
        .reset_index()
        .drop(['index'], axis=1)
    )

    return df1




#method chaining begins 

load_and_process("acs2017_county_data.csv")
