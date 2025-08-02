# src/train.py
from data_loader import load_xor_data
from model import build_xor_model

import tensorflow as tf

def train_model():
    X, y = load_xor_data()
    model = build_xor_model()

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X, y, epochs=500, verbose=0)

    model.save('xor_model.h5')
    print("Model trained and saved as xor_model.h5")

if __name__ == "__main__":
    train_model()