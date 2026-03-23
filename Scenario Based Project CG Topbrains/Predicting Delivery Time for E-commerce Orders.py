# Scenario: Predicting Delivery Time for E-commerce Orders

# An e-commerce company wants to predict how long an order will take to deliver based on:

# Distance to customer (km)

# Number of items in the order

# Traffic level (1 = Low, 2 = Medium, 3 = High)

# Warehouse processing time (hours)

# Since multiple factors affect delivery time, they use Multiple Linear Regression.
# DeliveryTime=b0​+b1​(Distance)+b2​(Items)+b3​(Traffic)+b4​(ProcessingTime)

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("Delievery_dataset_1.csv")

print("Dataset:")
print(df.head())

x = df[["Distance_km","Items","Traffic_Level","Processing_Time_hr"]]
y = df["Delivery_Time_hr"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size= 0.2, random_state= 42
)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("\nActual vs Predicted:")
for actual, pred in zip(y_test.values, y_pred):
    print(f"Actual: {actual:.2f}, Predicted: {pred:.2f}")

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Absolute Error:", mae)
print("R2 Score:", r2)


# Predict new time
new_time = pd.DataFrame({
    "Distance_km": [5],
    "Items": [2],
    "Traffic_Level": [1],
    "Processing_Time_hr": [1]
})

predicted_time = model.predict(new_time)

print(f"\nPredicted the delivery: {predicted_time[0]:.2f} time")
