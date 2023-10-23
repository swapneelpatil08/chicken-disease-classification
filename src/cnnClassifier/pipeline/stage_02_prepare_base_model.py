from cnnClassifier.config.configuration import configurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger


STAGE_NAME = "Prepare Base Model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            config = configurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config= prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e
        
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Start {STAGE_NAME} <<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> End {STAGE_NAME} <<<<<<<<<\n\n X============X\n")
        
    except Exception as e:
        logger.exception(e)
        raise e