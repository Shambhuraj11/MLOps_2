from fastapi import FastAPI, Request, Form, Depends
import os 
import sys 
from src.logger.logging import logging
from src.exception.exception import customexception
from src.pipeline.prediction_pipeline import PredictionPipeline, CustomData
from src.utils.models import Requestmodel, Responsemodel
from fastapi.templating  import Jinja2Templates


app = FastAPI(title= "Gemstone")
# templates = Jinja2Templates(directory="templates")

pred_pipeline = PredictionPipeline()
custom_data_obj = CustomData()

@app.post("/api",response_model= Responsemodel, tags= ['Get Price'])
# def get_price(request: Requestmodel = Depends(get_form_data)):
def get_price(request: Requestmodel):

    logging.info("Process Started !!!")

    request_data = request.model_dump()
    Df_data = custom_data_obj.get_data_as_dataframe(request_data) 
    logging.info("Converted Data to DataFrame")
    prediction = pred_pipeline.predict(Df_data)
    logging.info(f"Prediction is :{prediction}")
    return Responsemodel(
        price=prediction
    )

@app.get("/heathcheck")
def health():
    return {
        "success":1,
        "Status":"Ok"
    }

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app , host = "127.0.0.1",port=8000)

    


