from src.myproject.logger import logging
import sys
from src.myproject.exception import CoustomException
from src.myproject.components.data_ingestation import DataIngestation
#from src.myproject.components.data_ingestation import initiate_data_ingestion
from src.myproject.components.data_ingestation import DataIngestionConfig

if __name__=="__main__":
    logging.info("The Execution has Started")


    try:
       data_ingestation=DataIngestation()
       data_ingestation.initiate_data_ingestion()
    except Exception as e:
        logging.info("Coustom Exception")
        raise CoustomException(e,sys)