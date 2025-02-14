import os
import joblib
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# Load model using absolute path
model_path = os.path.join(os.getcwd(), "models/construction_cost_model.pkl")

try:
    model = joblib.load(model_path)
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Error loading model:", e)

@app.get("/")
def home():
    return {"message": "Welcome to the House Construction Cost Estimator API"}
