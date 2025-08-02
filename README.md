# mnist-digit-classifier
MNIST Digit Classifier with Multi-Layer Perceptron (MLP) Architecture

# XOR Deep Neural Network - Hello World Project

A simple yet structured Deep Learning project that solves the XOR problem using TensorFlow and Keras. This is designed as a clean project template to understand how data flows through layers and how to structure a basic DNN project.

---

## 🗂️ Project Structure
```
XOR-DNN-Project/
├── src/
│   ├── data_loader.py      # Dataset loading and preprocessing
│   ├── model.py            # MLP model definition
│   ├── train.py            # Training loop
│   └── evaluate.py         # Model evaluation
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and documentation
```

---

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/ChangkeunJ/XOR-DNN-Project.git
cd XOR-DNN-Project

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### 1. Train the Model
```bash
python src/train.py
```

### 2. Evaluate the Model
```bash
python src/evaluate.py
```

---

## 📊 Sample Output
```
Model trained and saved as xor_model.h5
Input: [0 0] | Ground Truth: 0 | Predicted: 0
Input: [0 1] | Ground Truth: 1 | Predicted: 1
Input: [1 0] | Ground Truth: 1 | Predicted: 1
Input: [1 1] | Ground Truth: 0 | Predicted: 0
```

---

## ✨ What You Learn
- How to structure a basic Deep Learning project (modular codebase)
- Flow of data through layers (Input → Hidden → Output)
- Training & Evaluating a neural network with TensorFlow

---

## 📄 License
MIT License

---

## 🙋‍♂️ Author
David Jang  | [GitHub](https://github.com/ChangkeunJ)
