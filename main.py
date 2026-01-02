from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np

app = FastAPI()

# This class ensures the data sent from Streamlit is valid
class HousingData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.post("/predict_and_search")
async def predict_and_search(data: HousingData):
    # --- MODEL PREDICTION LOGIC ---
    # Replace this with: model.predict([[data.MedInc, ...]])
    # Here, we use a dummy calculation for demonstration
    mock_prediction = data.MedInc * 0.5 + (data.HouseAge * 0.01)

    # --- SIMILAR LOCATIONS LOGIC ---
    # We generate 5 coordinates slightly offset from the user's input
    suggestions = []
    for i in range(5):
        suggestions.append({
            "Latitude": data.Latitude + np.random.uniform(-0.1, 0.1),
            "Longitude": data.Longitude + np.random.uniform(-0.1, 0.1)
        })

    return {
        "predicted_price": round(float(mock_prediction), 4),
        "suggested_locations": suggestions
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)