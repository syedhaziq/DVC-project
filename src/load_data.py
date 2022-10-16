## Load and save the data
## Load the functions from previous file

import os
from get_data import read_param, get_data
import argparse
import pandas as pd

def load_and_save(config_path):
    configs = read_param(config_path)
    df = get_data(config_path)
    print(df.head())
    raw_data_path = configs["load_data"]["raw_dataset_csv"]
    
 
    old_col_names= df.columns
    new_col_name = []
    for name in old_col_names:
        new_name = name.replace(' ', '_')
        new_col_name.append(new_name)
   
    
    df.rename(columns=dict(zip(df.columns,new_col_name)), inplace= True)
    df.to_csv(raw_data_path, sep=',', index=False) 

    
 
    

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default = "params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path= parsed_args.config)
