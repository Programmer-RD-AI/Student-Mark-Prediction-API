import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor
from joblib import dump, load

# Load the data
data = pd.read_csv("./data/data.csv")

# Check for missing values and fill them
if data.isnull().values.any():
    data.fillna(data.mean(), inplace=True)

# Drop unnecessary columns
data.drop(columns=[" -"], inplace=True, errors="ignore")

# Define features and target
X = data[["First Sem"]].values  # Ensure X is 2D
y = data[" Second Sem"].values

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Initialize XGBoost Regressor with default parameters
model = XGBRegressor(objective="reg:squarederror")

# Fit the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output metrics
print(f"MAE: {mae:.2f}, MSE: {mse:.2f}, R2: {r2:.2f}")

# Save the model
dump(model, "model.joblib")

# Load the model from the file
loaded_model = load("model.joblib")

# Test the loaded model with some data
test_predictions = loaded_model.predict(X_test)
print("Test Predictions:", test_predictions)
