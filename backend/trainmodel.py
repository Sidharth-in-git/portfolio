import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

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
