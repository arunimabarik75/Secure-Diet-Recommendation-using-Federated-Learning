from typing import List
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import data

Dataset = pd.core.frame.DataFrame
Params = List

def get_model_parameters(model: LinearRegression) -> Params:
    """Returns the paramters of a sklearn LinearRegression model."""
    
    if model.fit_intercept:
        params = [
            model.coef_,
            model.intercept_,
        ]
    else:
        params = [
            model.coef_,
        ]
    return params


def set_model_params(model: LinearRegression, params: Params) -> LinearRegression:
    """Sets the parameters of a sklean LinearRegression model."""
    
    model.coef_ = params[0]
    if model.fit_intercept:
        model.intercept_ = params[1]
    return model


def set_initial_params(model: LinearRegression):
    """Sets initial parameters as zeros 
    Required since model params are uninitialized until model.fit is called.
    Server asks for initial parameters from clients at launch.
    """

    n_features = 7
    model.coef_ = np.zeros((n_features,))
    model.feature_names_in_ = np.array([
        "age",
        "weight(kg)",
        "height(m)",
        "gender",
        "BMI",
        "BMR",
        "activity_level",
    ])   
    if model.fit_intercept:
        model.intercept_ = np.zeros((1,))

# def shuffle(X: np.ndarray, y: np.ndarray) -> XY:
#     """Shuffle X and y."""
#     rng = np.random.default_rng()
#     idx = rng.permutation(len(X))
#     return X[idx], y[idx]


# def partition(X: np.ndarray, y: np.ndarray, num_partitions: int) -> XYList:
#     """Split X and y into a number of partitions."""
#     return list(
#         zip(np.array_split(X, num_partitions), np.array_split(y, num_partitions))
#     )
