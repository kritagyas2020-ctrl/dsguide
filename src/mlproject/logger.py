import logging
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #log file name
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)#log path
os.makedirs(log_path,exist_ok=True)#log file folder

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)#complete log file path
#login setting has a format that uses basicconfig 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]%(lineno)d %(name)s- %(levelname)s - %(message)s",
    level=logging.INFO

)