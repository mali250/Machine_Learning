from dataclasses import dataclass
import os
import pandas as pd
import sys
from src.myproject.logger import logging 
from src.myproject.exception import CoustomException
from src.myproject.utils import read_sql_data
from sklearn.model_selection import train_test_split



@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestation:
    def __init__(self):
        self.ingestation_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            #os.makedirs(os.path.dirname(self.ingestation_config.raw_data_path),exist_ok=True)
            #(self.ingestation_config.raw_data_path,index=False,Header=True)
            df=pd.read_csv("src/raw.csv")
            
            
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestation_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestation_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion is completed")

            return(
                self.ingestation_config.train_data_path,
                self.ingestation_config.test_data_path )
           
            
        except Exception as e:
            raise CoustomException(e,sys)
