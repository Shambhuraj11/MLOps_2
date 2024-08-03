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

def load_object(filepath:str):
    try:
        with open(filepath, "wb") as f:
            return pickle.load(f)

    except Exception as e:
        logging.info("Exception occurred in loading object function")
        raise customexception(e,sys)