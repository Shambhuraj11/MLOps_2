import pandas as pd 
import numpy as np 
import os 
from src.logger.logging import logging
from src.exception.exception import customexception
import sys 
from dataclasses import dataclass
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from src.utils.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path : str = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:

    def __init__(self) -> None:
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation(self):
        try:
            logging.info("Started Get data transformation")
            pipeline = Pipeline(
                        steps=[
                            ("Imputer",SimpleImputer(strategy="most_frequent")),
                            ("Scaler",StandardScaler())
                        ]
                        )
            
            columns = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y',
       'z']
            preprocessor_obj = ColumnTransformer(
                [
                    ("Pipeline",pipeline,columns)
                ]
                )
            return preprocessor_obj

        except Exception as e:
            raise customexception(e,sys)


    def initiate_data_transformation(self,train_path: str, test_path: str):
        try:
            logging.info("Started Data Transformation")
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)
            logging.info("Train and Test data reading is completed...")

            logging.info("Started data transformation for Categorical features")

            # cat_cols = train_data.columns[train_data.dtypes == 'object']
            # num_cols = train_data.columns[train_data.dtypes != 'object']

            cut_categories = {"Fair":1,"Good":2,"Very Good":3,"Premium":4,"Ideal":5}
            color_categories = {"J":1,"I":2,"H":3,"G":4,"F":5,"E":6,"D":7}
            clarity_categories={"I1":1,"SI2":2,"SI1":3,"VS2":4,"VS1":5,"VVS2":6,"VVS1":7,"IF":8}

            train_data['cut'] = train_data['cut'].replace(cut_categories)
            train_data['color'] = train_data['color'].replace(color_categories)
            train_data['clarity'] = train_data['clarity'].replace(clarity_categories)

            test_data['cut'] = test_data['cut'].replace(cut_categories)
            test_data['clarity'] = test_data['clarity'].replace(clarity_categories)
            test_data['color'] = test_data['color'].replace(color_categories)

            preprocessor_obj = self.get_data_transformation()
            target_column = "price"

            x_train = train_data.drop(columns=["id","price"],axis=1)
            y_train = train_data[target_column]

            x_test = test_data.drop(columns=["id","price"],axis=1)
            y_test = test_data[target_column]

            xtrain = preprocessor_obj.fit_transform(x_train)
            xtest = preprocessor_obj.transform(x_test)

            logging.info("Applying preprocessing on train and test datasets")

            train_arr = np.c_[xtrain,np.array(y_train)]
            test_arr = np.c_[xtest,np.array(y_test)]

            save_object(self.data_transformation_config.preprocessor_obj_file_path,preprocessor_obj)
            logging.info("Preprocessing pickle file is saved")

            return (
                train_arr,
                test_arr
            )


        except Exception as e:
            logging.info("Error occurred in data transformation")
            raise customexception(e,sys)