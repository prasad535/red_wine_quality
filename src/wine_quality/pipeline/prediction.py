import joblib
from pathlib import Path
import pandas as pandas
import os



class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_training/model.joblib'))

    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction