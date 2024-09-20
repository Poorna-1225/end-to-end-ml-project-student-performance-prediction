import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass



@dataclass #helps us to create class varibales directly without creating __init__ method
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion method started")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("data set reading as data frame done")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header = True)
            logging.info("train test split started")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42) 


            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header = True)

            logging.info("ingestion of data is completed")
            print(os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True))
            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)
        except Exception as e:
            raise CustomException(e,sys)
"""
checking if class is working properly 

if __name__ == "__main__":
    d = DataIngestion()
    print(d.ingestion_config)
    print(d.initiate_data_ingestion())

the output will be a folder called artifacts created with 3 csv files in it 
    """