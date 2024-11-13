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


# FastAPI Prediction API

This repository contains a FastAPI-based web application that serves a **prediction API** using machine learning models (Linear Regression and Random Forest). The application performs predictions based on a set of features provided by the user. The API also includes a health check endpoint to monitor the service's status.

## Features

- **Health Check Endpoint**: To verify if the API is running properly.
- **Prediction Endpoint**: To get predictions from two machine learning models — Linear Regression and Random Forest.
  - You can specify which model to use for predictions through the `model` query parameter.
  - The prediction is made using a set of input features provided in the request body.
- **Logging**: Logs are created to monitor the status of the models and predictions.

## How It Works

The FastAPI app loads two pre-trained models:
1. **Linear Regression Model** (`linear_regression_model.pkl`)
2. **Random Forest Model** (`random_forest_model.pkl`)

These models are loaded at the app startup, and the API provides two main endpoints:

### 1. Health Check

- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: This endpoint checks if the API is running properly.
  
  **Response Example**:
  ```json
  {
    "status": "healthy",
    "timestamp": "2024-11-13T12:00:00"
  }

#### 2. Make Predictions

- **Endpoint**: `/predict`
- **Method**: `POST`
- **Description**: This endpoint allows users to make predictions using either the Linear Regression or Random Forest model.
  
  You can specify which model to use by passing the `model` query parameter with one of the following values:
  - `"linear_regression"`
  - `"random_forest"`

- **Request Body**: The request body should contain a JSON object with a `features` array, which contains the feature values required for making the prediction. The number of features must match the number expected by the model (6 features for this example).

**Request Example**:

```bash
POST http://127.0.0.1:8000/predict?model=linear_regression

Request Body (JSON):

{
  "features": [0.5, 1.2, -0.3, 4.5, 8, 2.5]
}
  

