import os
from src.logger.logging import logging
from src.exception.exception import customexception
import sys 
from src.utils.utils import save_object,evaluate_model
import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEval


class TrainingPipeline:
    def start_data_ingestion(self):
        try:
            ingestion_obj = DataIngestion()
            train_data_path, test_data_path = ingestion_obj.initiate_data_ingestion()
            return train_data_path,test_data_path
        except Exception as e:
            raise customexception(e,sys)
    
    def start_data_transformation(self,train_data_path:str, test_data_path:str):
        try:
            data_transformation = DataTransformation()
            train_arr,test_arr = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
            return train_arr,test_arr
        except Exception as e:
            raise customexception(e,sys)
    
    def start_model_training(self,train_arr,test_arr):
        try:
            model_trainer_obj = ModelTrainer()
            model_trainer_obj.initiate_model_training(train_arr,test_arr)
        except Exception as e:
            raise customexception(e,sys)
    
    def training_pipe(self):
        try:
            train_data_path,test_data_path = self.start_data_ingestion()
            train_arr,test_arr = self.start_data_transformation(train_data_path,test_data_path)
            self.start_model_training(train_arr,test_arr)
        except Exception as e:
            raise customexception(e,sys)