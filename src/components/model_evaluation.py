import pandas as pd 
import numpy as np 
import os 
from src.logger.logging import logging
from src.exception.exception import customexception
import sys 
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from dataclasses import dataclass
from pathlib import Path
import mlflow
import mlflow.sklearn
import pickle 
from src.utils.utils import load_object
from urllib.parse import urlparse

@dataclass
class ModelEvalConfig:
    model_path : str = os.path.join("artifacts","model.pkl")
class ModelEval:

    def __init__(self) -> None:
        self.model_path = ModelEvalConfig.model_path
    
    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        logging.info("Evaluation metrics captured")
        return rmse,mae,r2


    def initiate_model_evaluation(self,train_arr, test_arr):
        try:
            logging.info("Model evaluation initiated !!")
            x_test,y_test = (test_arr[:,:-1],test_arr[:,-1])
            model = load_object(self.model_path)

            # mlflow.set_registry_uri("")

            logging.info("Model has registered")

            # tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            # print(tracking_url_type_store)

            with mlflow.start_run():
                pred = model.predict(x_test)
                mlflow.log_param("Predication",pred)
                rmse,mae,r2 = self.eval_metrics(y_test,pred)
                mlflow.log_param("rmse",rmse)
                mlflow.log_param("mae",mae)
                mlflow.log_param("r2",r2)
                
                # if tracking_url_type_store != "file":
                #     mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
            # else:
                mlflow.sklearn.log_model(model,"model")

                

        except Exception as e:
            logging.info()
            raise customexception(e,sys)