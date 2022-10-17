# Load the training and testing data
# build the model
#save the params and metrics


import os
                                                                     
import warnings
import sys
import pandas as pd
import numpy as пр
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
from get_data import read_param
import argparse
import joblib
import json


def eval_metrics(actual, pred):
   # rmse=np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return  mae, r2



def train_and_evaluate(config_path):
    config = read_param(config_path)
    train_data_path=config["split_data"]["train_path"]
    test_data_path=config["split_data"]["test_path"]
    random_state =  config["base"]["random_state"]
    
    learning_rate = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]
    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    #print(alpha)
    target_col = [ config["base"]["target_col"] ]
   
    
    model_save_path = config["model_dir"]
    
    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")

        

    train_y = train[target_col]
    test_y = test[target_col]
    
    #print(train_y.head())
    
    train_x = train.drop(target_col, axis=1)
    test_x = test.drop(target_col, axis=1)
    
    lr = ElasticNet(
        alpha= alpha,
        l1_ratio= learning_rate,
        random_state= random_state)
    
    lr.fit(train_x, train_y)

    predicted_qualities = lr.predict(test_x)
    
    (mae, r2) = eval_metrics(test_y, predicted_qualities)

    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, learning_rate))
    #print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

#####################################################
    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]   
    
    with open(scores_file,'w') as f:
        scores = {
            
            "mae": mae,
            "r2": r2
        }
        json.dump(scores, f, indent=4)
    
    
    with open(params_file, "w") as f:
        params = {
            "alpha": alpha,
            "l1_ratio": learning_rate,
        }
        json.dump(params, f, indent=4)
        
        
#####################################################


    os.makedirs(model_save_path, exist_ok=True)
    model_path = os.path.join(model_save_path, "model.joblib")
    print("the path of save model is : \n{}".format(model_path))


    joblib.dump(lr, model_path)



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)    
    
    
    
