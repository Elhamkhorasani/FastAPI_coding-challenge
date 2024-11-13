from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from datetime import datetime
import logging
import joblib
from typing import List, Literal
import numpy as np

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Simple API",
    description="A basic FastAPI application with health check",
    version="1.0.0",
)


#load model
try:
    lr_model = joblib.load("linear_regression_model.pkl")
    rfr_model = joblib.load("random_forest_model.pkl")
    logger.info("Models loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load models: {e}")
    lr_model, rfr_model = None, None


# Define input schema
class InferenceInput(BaseModel):
    features: List[float] = Field(..., description="List of feature values for prediction")

# Define output schema
class InferenceOutput(BaseModel):
    prediction: float


class HealthResponse(BaseModel):
    status: str
    timestamp: str
 

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify API is running
    """
    logger.info("Health check endpoint called")
    return HealthResponse(status="healthy", timestamp=datetime.utcnow().isoformat())



# Inference Endpoint
@app.post("/predict", response_model=InferenceOutput)
async def predict(input_data: InferenceInput, model: Literal["linear_regression", "random_forest"] = Query(...)):
    """
    Make predictions using the specified model (either Linear Regression or Random Forest).
    """
    if model == "linear_regression" and lr_model is None:
        raise HTTPException(status_code=503, detail="Linear Regression model is not available")
    elif model == "random_forest" and rfr_model is None:
        raise HTTPException(status_code=503, detail="Random Forest model is not available")
    
    # Prepare input features
    features_array = np.array([input_data.features])

    
    # Perform prediction
    try:
        if model == "linear_regression":
            prediction = lr_model.predict(features_array)[0]
        else:
            prediction = rfr_model.predict(features_array)[0]
        
        logger.info(f"Prediction using {model}: {prediction}")
        return InferenceOutput(prediction=prediction)
    except Exception as e:
        logger.error(f"Model inference failed: {e}")
        raise HTTPException(status_code=500, detail="Model inference failed")




if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
