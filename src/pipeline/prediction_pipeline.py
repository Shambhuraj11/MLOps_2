import os 
import pandas as pd
from pandas import DataFrame 
from src.logger.logging import logging
from src.utils.utils import load_object
import sys 
from src.exception.exception import customexception

class PredictionPipeline:
    
    def __init__(self) -> None:
        pass

    def predict(self, data : DataFrame) -> float: 
        logging.info("Prediction Initiated !!!")
        try:
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
            model_path = os.path.join("artifacts","model.pkl")

            preprocessor_obj = load_object(preprocessor_path)
            model = load_object(model_path)
            logging.info("Preprocessing and ML model loaded..")


            train_data = preprocessor_obj.transform(data)
            logging.info("Preprocessing Done")

            pred = model.predict(train_data)

            logging.info(f"Prediction done with price of {pred}")

            return pred


        except Exception as e:
            raise customexception(e,sys)


class CustomData:
    def __init__(self) -> None:
        pass

    def get_data_as_dataframe(self, features: dict):

        data = pd.DataFrame.from_dict([features])

        cut_categories = {"Fair":1,"Good":2,"Very Good":3,"Premium":4,"Ideal":5}
        color_categories = {"J":1,"I":2,"H":3,"G":4,"F":5,"E":6,"D":7}
        clarity_categories={"I1":1,"SI2":2,"SI1":3,"VS2":4,"VS1":5,"VVS2":6,"VVS1":7,"IF":8}

        data['cut'] = data['cut'].replace(cut_categories)
        data['color'] = data['color'].replace(color_categories)
        data['clarity'] = data['clarity'].replace(clarity_categories)

        return data 