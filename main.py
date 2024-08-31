from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the models
model_kmeans = joblib.load('kmens_model.joblib')
scaler_kmeans = joblib.load('kmens_scaler.joblib')

# Define the input data model
class InputFeatures(BaseModel):
    Provider: str
    Level: str
    Type: str
    Duration_Weeks: str

# Preprocessing function
def preprocessing(input_features: InputFeatures):
    dict_f = {
        'Provider': input_features.Provider,
        'Level': input_features.Level,
        'Type': input_features.Type,
        'Duration / Weeks': input_features.Duration_Weeks,
    }
    
    # Convert dictionary values to a list in the correct order
    features_list = [dict_f[key] for key in dict_f]
    
    # Scale the input features
    scaled_features = scaler_kmeans.transform([features_list])
    
    return scaled_features

# Prediction endpoint
@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    y_pred = model_kmeans.predict(data)
    return {"pred": y_pred.tolist()[0]}

# Example endpoint to test the server
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/")
def root():
    return " Prediction"
