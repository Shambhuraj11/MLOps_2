import os 
import sys
import numpy as np 
import pandas as pd 
import pickle
from src.exception.exception import customexception
from src.logger.logging import logging
from sklearn.metrics import r2_score, median_absolute_error, mean_squared_error


def save_object(filepath:str,obj):
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)
        with open(filepath, "wb") as f:
            pickle.dump(obj,f)

    except Exception as e:
        logging.info("Exception occurred in saving object function")

        raise customexception(e,sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise customexception(e,sys)

def load_object(filepath:str):
    try:
        with open(filepath, "rb") as f:
            return pickle.load(f)

    except Exception as e:
        logging.info("Exception occurred in loading object function")
        raise customexception(e,sys)