from cnnClassifier.config.configuration import configurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallbacks
from cnnClassifier.components.training import Training
from cnnClassifier import logger


STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = configurationManager()
        prepare_callback_config = config.get_prepare_callback_config()
        prepare_callback = PrepareCallbacks(config= prepare_callback_config)
        callback_list = prepare_callback.get_tb_ckpt_callbacks()
            
        training_config = config.get_training_config()
        training = Training(config= training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list= callback_list
        )
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Start {STAGE_NAME} <<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> End {STAGE_NAME} <<<<<<<<<\n\n X============X\n")
        
    except Exception as e:
        logger.exception(e)
        raise e