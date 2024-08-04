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
    model_file_path : str = os.path.join("artifacts","model.pkl")


class ModelTrainer:

    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_training(self,train_array, test_array):
        logging.info("Initiated Model training!!")
        try:
            x_train,x_test,y_train,y_test = (
                train_array[:,:-1],
                test_array[:,:-1],
                train_array[:,-1],
                test_array[:,-1],

            )
            models = {
                    "LR":LinearRegression(),
                    "Lasso":Lasso(),
                    "Ridge":Ridge(),
                    "ElasticNet":ElasticNet(),
                    "RF":RandomForestRegressor(),
                    "xgb":XGB()
                }
            
            model_report:dict = evaluate_model(x_train,y_train,x_test,y_test,models)

            logging.info(f"Model Report: {model_report}")

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            logging.info(f"Best Model found, Model Name: {best_model_name}, R2 Score: {best_model_score}")

            save_object(
                self.model_trainer_config.model_file_path,
                best_model
            )

        except Exception as e:
            logging.info()
            raise customexception(e,sys)