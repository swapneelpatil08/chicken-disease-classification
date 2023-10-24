from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluaitonPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> Start {STAGE_NAME} <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> End {STAGE_NAME} <<<<<<<<<\n\n X============X\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f">>>>>>> Start {STAGE_NAME} <<<<<<<<<")
    base_model = PrepareBaseModelTrainingPipeline()
    base_model.main()
    logger.info(f">>>>>>> End {STAGE_NAME} <<<<<<<<<\n\n X============X\n")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Training"

try:
    logger.info(f">>>>>>> Start {STAGE_NAME} <<<<<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>>> End {STAGE_NAME} <<<<<<<<<\n\n X============X\n")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Evaluation"

try:
    logger.info(f">>>>>>> Start {STAGE_NAME} <<<<<<<<<")
    eval = EvaluaitonPipeline()
    eval.main()
    logger.info(f">>>>>>> End {STAGE_NAME} <<<<<<<<<\n\n X============X\n")
except Exception as e:
    logger.exception(e)
    raise e
