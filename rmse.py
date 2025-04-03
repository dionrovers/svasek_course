# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 11:42:42 2025

@author: AKR
"""

import numpy as np


def rmse(predictions, observations):
    """
    

    Args:
        predictions (numpy array): predicted values.
        observations (numpy array): observed values.

    Returns:
        numpy array: root mean square error.

    """
    return np.sqrt(((observations - predictions) ** 2).mean())