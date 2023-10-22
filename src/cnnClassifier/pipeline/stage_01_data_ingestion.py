from cnnClassifier.config.configuration import configurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            config = configurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config= data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Start {STAGE_NAME} <<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> End {STAGE_NAME} <<<<<<<<<\n\n X============X\n")
        
    except Exception as e:
        logger.exception(e)
        raise e