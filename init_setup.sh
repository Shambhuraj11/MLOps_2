echo [$(date)]: "START"

echo [$(date)]:"Creating env with python 3.8 version"


conda create --name MLenv python==3.8 -y

echo [$(date)]: "activating the environment"

source activate MLenv

echo [$(date)] : "installing the dev requirements"

pip install -r requirements_dev.txt

echo [$(date)] : "END"