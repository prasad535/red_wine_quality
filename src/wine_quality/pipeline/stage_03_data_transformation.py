from wine_quality.components.data_transformation import DataTransformation
from wine_quality.config.configuration import ConfigurationManager
from wine_quality import logger

STAGE_NAME = "Data Transformation Statge"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config= data_transformation_config)
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e


if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed. \n x======================================================x")
    except Exception as e:
        raise e
