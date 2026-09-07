import os #gives generic folder path
from pathlib import Path #gives specific folder path
import logging #gives logging functionality
logging.basicConfig(level=logging.INFO)
project_name="mlproject"
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "main.py"
]
for filepath in list_of_files: 
    filepath = Path(filepath) #takes the filepath and converts it into a Path object
    filedir, filename = os.path.split(filepath) #os.path.split takes out two information from the filepath, the directory and the filename``
    if filedir!="": #if the directory is not empty, then create the directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): #if the file does not exist or the file is empty, then create the file
        with open(filepath, "w") as f:
            pass #creates an empty file
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists") #skips the file creation if the file already exists
