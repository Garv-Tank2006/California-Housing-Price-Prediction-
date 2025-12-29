from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load('california_housing_rf_model.pkl')

class HousingData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float  # Capital P
    AveOccup: float    # Capital A and O
    Latitude: float
    Longitude: float

@app.post("/predict")
def predict(data: HousingData):
    # This matches the names the model saw during training
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)
    return {"Predicted_Price": float(prediction[0])} # Simplified key