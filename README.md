# 🏠 California Housing Price Prediction API

An end-to-end Machine Learning project that predicts **median house prices in California** using a **Random Forest Regressor**, exposed via a **FastAPI REST API** with input validation, JSON serialization, and geolocation-based location mapping.

---

## 🚀 Project Overview

This project demonstrates how a trained ML regression model can be deployed as a real-world API.  
The API predicts house prices and also provides **geographical context** of the house location using latitude and longitude.

### 🔑 Key Highlights
- Continuous value prediction (Regression)
- Multiple numerical features
- Feature scaling (for linear models)
- Strong non-linear model using Random Forest
- REST API using FastAPI
- Input validation using Pydantic annotations
- JSON serialization of responses
- Geolocation mapping using latitude & longitude
- GitHub-ready, production-style structure

---

## 📊 Dataset

**California Housing Dataset**

- Source: `sklearn.datasets.fetch_california_housing`
- Target Variable: `MedHouseVal` (median house value in $100,000s)

### Features:
| Feature | Description |
|------|-----------|
| MedInc | Median income |
| HouseAge | Average house age |
| AveRooms | Average number of rooms |
| AveBedrms | Average number of bedrooms |
| Population | Block population |
| AveOccup | Average occupancy |
| Latitude | Latitude |
| Longitude | Longitude |

---

## 🧠 Model Performance

### Model Comparison

| Model | MAE | RMSE | R² |
|-----|-----|------|----|
| Linear Regression | ~0.53 | ~0.74 | ~0.58 |
| **Random Forest (Final)** | **0.33** | **0.50** | **0.81** |

✅ Random Forest was selected as the final model due to its superior performance and ability to capture non-linear and spatial patterns.

---

## 🗺️ Geolocation Mapping Feature

- Uses **latitude and longitude** to:
  - Identify approximate house location in California
  - Provide user-friendly geographic context
- Serialized output includes location-related information for better interpretability

---

## 🧪 API Features

- **FastAPI-based REST API**
- Input validation using Pydantic annotations (`gt`, `ge`, `le`)
- JSON request & response format
- Swagger UI for testing
- Model loaded once for efficiency

---

