from cnnClassifier.config.configuration import configurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger


STAGE_NAME = "Evaluation"

class EvaluaitonPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = configurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Start {STAGE_NAME} <<<<<<<<<")
        obj = EvaluaitonPipeline()
        obj.main()
        logger.info(f">>>>>>> End {STAGE_NAME} <<<<<<<<<\n\n X============X\n")
        
    except Exception as e:
        logger.exception(e)
        raise e