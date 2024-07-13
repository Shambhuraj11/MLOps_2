import os 
from pathlib import Path  # Take care of forward and backword /

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py"
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb"
]

for file_path  in list_of_files:
    file_path = Path(file_path)
    dir_name, file_name = os.path.split(file_path)
    if dir_name!="":
        os.makedirs(dir_name,exist_ok=True)

    if not os.path.exists("file_path"):
        with open(file_path,'w') as f:
            pass   






