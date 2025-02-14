import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# Load preprocessed data
df = pd.read_csv("processed_data.csv")

# Features (X) and target (y)
X = df.drop(columns=["estimated_cost"])  # All columns except the target
y = df["estimated_cost"]  # Target variable

# Split into train (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print dataset shapes
print(f"📌 Training Data: {X_train.shape}, Test Data: {X_test.shape}")

# Train a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"\n✅ Model Trained Successfully!")
print(f"📊 Mean Absolute Error (MAE): {mae:.2f}")
print(f"📊 Mean Squared Error (MSE): {mse:.2f}")
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print(f"📊 R² Score: {r2:.2f}")


# Save the trained model
joblib.dump(model, "models/construction_cost_model.pkl")
print("\n💾 Model saved as 'models/construction_cost_model.pkl'")

