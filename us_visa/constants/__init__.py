import os
from datetime import date

# Constant for MongoDB
MONGODB_URL_KEY = "MONGODB_URL"
DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"


# Other Constant
PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME = "model.pkl"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"


TARGET_COLUMN = "case_status"  # Dependent Variable
CURRENT_YEAR = date.today().year

FILE_NAME: str = "usvisa.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

"""
Data Ingestion related constant starts with "DATA_INGESTION" and Variable Name
"""

DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
