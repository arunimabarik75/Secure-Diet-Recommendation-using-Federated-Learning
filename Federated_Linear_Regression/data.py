from typing import Tuple, Union, List
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

Dataset = pd.core.frame.DataFrame

def get_required_columns(data: Dataset) -> Dataset:
    """Returns the required columns of the dataset."""

    col_list = [
        "age",
        "weight(kg)",
        "height(m)",
        "gender",
        "BMI",
        "BMR",
        "activity_level",
        "calories_to_maintain_weight",
    ]

    return data[col_list]


def encode_labels(data: Dataset) -> Dataset:
    """Encode gender column of the dataset."""

    le = LabelEncoder()
    gender_encoded = le.fit_transform(data["gender"])
    data["gender"] = gender_encoded
    return data


def scale_input(data: Dataset) -> Dataset:
    """Scale columns of the dataset."""

    scaler = StandardScaler()
    data.iloc[:, :] = scaler.fit_transform(data.iloc[:, :])
    return data


def load_data(type: str) -> Dataset:
    """Loads the dataset using pandas."""

    file_name = "calories_" + type + ".csv" 
    data = pd.read_csv(file_name)
    data = get_required_columns(data)
    data = encode_labels(data)
    data = scale_input(data)

    return data
