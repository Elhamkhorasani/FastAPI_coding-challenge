# 💻 Laptop Price Prediction API Challenge

![Python](https://img.shields.io/badge/python-v3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-green.svg)
![Docker](https://img.shields.io/badge/docker-latest-blue.svg)

## 🎯 Overview
Technical challenge focusing on ML model deployment and API development.

## 🗂 Project Structure

```
. 
├── data/ 
│ ├── label_encoders.joblib # Label encoders
│ ├── laptop_price.csv      # Training dataset
│ ├── model.joblib          # Trained model 
│ ├── scaler.joblib         # Feature scaler 
│ ├── test.csv              # Test dataset
│ └── train.csv             # Training dataset 
├── notebooks/ 
│ └── model.ipynb           # Model development 
├── app/ 
│ └── main.py #              FastAPI application 
├── pyproject.toml 
└── README.md
```

## 🎯 Challenge Tasks

### 1️⃣ Code Understanding and Execution
- Review model training notebook
- Understand feature engineering
- Run the notebook and the API, troubleshoot and fix any issues to ensure they work correctly

### 2️⃣ Model Evaluation
- Evaluate performance of models
- Compare model performances

### 3️⃣ API Development
- Create a FastAPI endpoint to perform model inference
- Add validation & logging
- Document API endpoints

### 4️⃣ Dockerization
- Create Dockerfile
- Configure environment
- Optimize container
- Document deployment

## 🚀 Getting Started

### Prerequisites
```bash
python 3.11
poetry
```

### Installation
```bash
# Install dependencies
poetry install

# Activate environment
poetry shell
```

### Running the API
```bash
# Start server
python -m app.main
```

## API Endpoints
- `GET /health` - Health check
- `POST /predict` - Price prediction

```json
{
    "Company": "Apple",
    "Cpu": "Intel Core i5 2.3GHz",
    "Gpu": "Intel Iris Plus Graphics 640",
    "OpSys": "macOS",
    "Ram": "8GB",
    "Weight": "1.37kg",
}
```
