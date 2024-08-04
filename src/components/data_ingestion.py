import pandas as pd 
import numpy as np 
import os 
from src.logger.logging import logging
from src.exception.exception import customexception
import sys 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts','raw.csv')
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')

class DataIngestion:

    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        logging.info("Started Data Ingestion")
        try:
            logging.info("reading data from artifacts")
            data = pd.read_csv(self.ingestion_config.raw_data_path)

            train,test = train_test_split(data,test_size=0.30,random_state=42)

            train.to_csv(self.ingestion_config.train_data_path,index = False)
            test.to_csv(self.ingestion_config.test_data_path,index = False)
            logging.info("Data Ingestion is Done")
        
            return (
            self.ingestion_config.train_data_path,
            self.ingestion_config.test_data_path
            )


        except Exception as e:
            logging.info()
            raise customexception(e,sys)
        