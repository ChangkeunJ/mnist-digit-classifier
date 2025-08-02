# src/evaluate.py
from data_loader import load_xor_data
from tensorflow.keras.models import load_model
import numpy as np

def evaluate_model():
    X, y = load_xor_data()
    model = load_model('xor_model.h5')

    predictions = model.predict(X)
    predictions_binary = (predictions > 0.5).astype(int)

    for inp, label, pred in zip(X, y, predictions_binary):
        print(f"Input: {inp} | Ground Truth: {label[0]} | Predicted: {pred[0]}")

if __name__ == "__main__":
    evaluate_model()
