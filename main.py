from src.wine_quality import logger
from src.wine_quality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.wine_quality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.wine_quality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.wine_quality.pipeline.stage_04_model_trainer import ModelTrainerPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<< ")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<< ")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==================x")
except Exception as e:
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<< ")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==================x")
except Exception as e:
    raise e

STAGE_NAME = "Model Trainer"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<< ")
    model_trainer =  ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==================x")
except Exception as e:
    raise e