# src/data_loader.py
import numpy as np

def load_xor_data():
    # Input data (XOR combinations)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    # Output data (XOR results)
    y = np.array([[0], [1], [1], [0]])
    return X, y