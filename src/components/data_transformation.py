import pandas as pd 
import numpy as np 
import os 
from src.logger.logging import logging
from src.exception.exception import customexception
import sys 
from dataclasses import dataclass
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from src.utils.utils import save_object


@dataclass
class DataTransformationConfig:
    pass

class DataTransformation:

    def __init__(self) -> None:
        pass


    def initiate_data_transformation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)