import pandas as pd 
import numpy as np 
import os 
from src.logger.logging import logging
from src.exception.exception import customexception
import sys 
from sklearn.linear_model import Lasso, Ridge, LinearRegression, ElasticNet
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor as XGB
from dataclasses import dataclass
from pathlib import Path
from src.utils.utils import save_object,evaluate_model

@dataclass
class ModelTrainerConfig:
    pass

class ModelTrainer:

    def __init__(self) -> None:
        pass


    def initiate_model_training(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)