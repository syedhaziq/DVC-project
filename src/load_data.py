## Load and save the data
## Load the functions from previous file

import os
from get_data import read_param, get_data
import argparse

def load_and_save(config_path):
    config = read_param(config_path)
    df = get_data(config_path)
    
    new_cols= [col for col in df.columns]
    print(new_cols)
    

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default = "params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path= parsed_args.config)
