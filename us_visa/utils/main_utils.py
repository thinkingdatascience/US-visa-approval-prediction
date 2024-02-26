import os
import sys
import numpy as np
from pandas import DataFrame
import dill
import yaml

from us_visa.exception import USvisaException
from us_visa.logger import logging

"""
try:
    pass
except Exception as e:
    raise USvisaException(e,sys) from e
"""


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file=file_path, mode="rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise USvisaException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file=file_path, mode="w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise USvisaException(e, sys) from e


def load_object(file_path: str) -> object:
    logging.info("Entered the load object method of utils")
    try:
        with open(file=file_path, mode="rb") as file_obj:
            obj = dill.load(file_obj)
        logging.info("Exited the load _object method of utils")

        return obj

    except Exception as e:
        raise USvisaException(e, sys) from e


def save_numpy_array_data(file_path: str, array: np.array):
    """Save the numpy array data to a file.

    Args:
        file_path (str): location of a file to save
        array (np.array):data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file=file_path, mode="wb") as file_obj:
            np.save(file=file_obj, arr=array)

    except Exception as e:
        raise USvisaException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return:np.array data loaded
    """
    try:
        with open(file=file_path, mode="rb") as fileobj:
            return np.load(fileobj)
    except Exception as e:
        raise USvisaException(e, sys) from e


def save_object(file_path: str, obj: object) -> None:
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file=file_path, mode="wb") as file_obj:
            dill.dump(obj=obj, file=file_obj)

        logging.info("Exited the save_obj of utils")

    except Exception as e:
        raise USvisaException(e, sys) from e


def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    """drops the columns from a pandas Dataframe

    Args:
        df (DataFrame): pandas Dataframe
        cols (list): List of columns to be dropped

    Returns:
        DataFrame: Returns a dataframe after the columns are dropeed
    """
    logging.info("Entered drop columns mentioned in utils")

    try:
        df.drop(columns=cols, axis=1)

        logging.info("Exited the drop column method of utils")

        return df

    except Exception as e:
        raise USvisaException(e, sys) from e
