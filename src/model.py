# src/model.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def build_xor_model():
    model = Sequential()
    model.add(Dense(4, input_dim=2, activation='relu'))  # Hidden layer (4 neurons)
    model.add(Dense(1, activation='sigmoid'))            # Output layer (1 neuron)
    return model