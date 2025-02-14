import sys
import os

# Ensure the parent directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.db_connection import fetch_data


# Fetch project data from PostgreSQL
query = "SELECT project_id, built_up_area, floors, bhk, service_package, estimated_cost FROM projects;"
df = fetch_data(query)

# Display initial data
print("📌 Raw Data:")
print(df.head())

# Check for missing values
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# Fill missing values
df.fillna(0, inplace=True)

from sklearn.preprocessing import LabelEncoder

# Convert categorical column (service_package) to numbers
encoder = LabelEncoder()
df["service_package"] = encoder.fit_transform(df["service_package"])

print("\n📌 Encoded Data:")
print(df.head())


from sklearn.preprocessing import MinMaxScaler

# Select numerical columns for normalization
num_cols = ["built_up_area", "floors", "bhk", "estimated_cost"]

# Apply MinMaxScaler
scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("\n📌 Normalized Data:")
print(df.head())

# Save preprocessed data as CSV
df.to_csv("processed_data.csv", index=False)

print("\n✅ Data Preprocessing Complete! Saved as 'processed_data.csv'")
