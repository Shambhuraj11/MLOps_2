from __future__ import annotations
import json 
from textwrap import dedent
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.pipeline.training_pipeline import TrainingPipeline
import numpy as np
training_pipeline = TrainingPipeline()

# Direct Acyclic Graph

with DAG(
    "Model_Training_Pipeline",
    default_args= {"retries":2},
    description= "Gemstone Price Prediction Model Training",
    schedule="@weekly",
    start_date=pendulum.datetime(2024,8,17,tz="UTC"),
    catchup= False,
    tags=['Machine Learning','classification','gemstone']
) as dag:
    dag.doc_md = __doc__


    # xcom : cross communication between components
    def data_ingestion(**kwargs):
        ti = kwargs["ti"]
        # Dag by default pass dict in which there is a key 'ti' stands for task instance
        train_data_path, test_data_path = training_pipeline.start_data_ingestion()
        ti.xcom_push("data_ingestion_artifact",{"train_data_path":train_data_path,"test_data_path":test_data_path})   # Push output to next component

    
    def data_transformation(**kwargs):
        ti = kwargs['ti']
        data_ingestion_artifact = ti.xcom_pull(task_id = 'data_ingestion', key = 'data_ingestion_artifact')  # Pull outputs of previous components to this  as a input
        train_arr,test_arr = training_pipeline.start_data_transformation(data_ingestion_artifact['train_data_path'],data_ingestion_artifact['test_data_path'])
        train_arr = train_arr.to_list()
        test_arr = test_arr.to_list()
        ti.xcom_push("data_transformation_artifact",{'train_arr':train_arr,'test_arr':test_arr})
    
    def model_trainer(**kwargs):
        ti = kwargs['ti']
        data_transformation_artifact = ti.xcom_pull(task_id ='data_transformation',key = "data_transformation_artifact")
        train_arr = np.array(data_transformation_artifact['train_arr'])        
        test_arr = np.array(data_transformation_artifact['test_arr'])        
        training_pipeline.start_model_training(train_arr,test_arr)



    data_ingestion_task = PythonOperator(
        task_id = "data_ingestion",
        python_callable = data_ingestion
    )
    data_ingestion_task.doc_md = dedent(
        """\
    #### Ingestion task
    this task creates a train and test file.
    """
    )

    data_transformation_task = PythonOperator(
        task_id = "data_transformation",
        python_callable = data_transformation
    )
    data_transformation_task.doc_md = dedent(
        """
    #### Transformation task
    this task performs the transformation"""
        
    )

    model_trainer_task = PythonOperator(
        task_id = "model_trainer",
        python_callable = model_trainer
    )

    model_trainer_task.doc_md = dedent(
        """\
    #### model trainer task
    this task perform training
    """
    )



data_ingestion_task>>data_transformation_task>>model_trainer_task


