import pandas as pd 
import numpy as np 
import os 
from src.logger.logging import logging
from src.exception.exception import customexception
import sys 
from sklearn.metrics import r2_score, median_absolute_error, mean_squared_error
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ModelEvalConfig:
    pass

class ModelEval:

    def __init__(self) -> None:
        pass


    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)