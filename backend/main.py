import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
from fastapi.middleware.cors import CORSMiddleware


# Example training data
data = {
    "area": [1000, 1500, 1200, 1800, 2000],
    "bedrooms": [2, 3, 2, 4, 4],
    "bathrooms": [1, 2, 2, 3, 3],
    "price": [120000, 180000, 150000, 240000, 270000]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms", "bathrooms"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved as model.pkl")
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# load ML model
model = pickle.load(open("model.pkl", "rb"))

app = FastAPI()

# allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# request format
class House(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int

@app.get("/")
def home():
    return {"message": "House Price Prediction API is running 🚀"}

@app.post("/predict")
def predict_price(data: House):
    features = np.array([[data.area, data.bedrooms, data.bathrooms]])
    predicted_price = model.predict(features)[0]
    
    return {"predicted_price": round(float(predicted_price), 2)}
