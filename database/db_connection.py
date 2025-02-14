import psycopg2
import pandas as pd

# Database connection settings
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "1234",  # Change to your actual password
    "host": "localhost",
    "port": "5432",
}

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    print("✅ Database connection successful!")
except Exception as e:
    print("❌ Error connecting to database:", e)


def fetch_data(query):
    """Fetches data from PostgreSQL and returns a Pandas DataFrame."""
    try:
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]  # Get column names
        data = cursor.fetchall()
        return pd.DataFrame(data, columns=columns)
    except Exception as e:
        print("❌ Error fetching data:", e)
        return None


if __name__ == "__main__":
    # Example query to fetch materials data
    query = "SELECT * FROM materials;"
    df_materials = fetch_data(query)

    if df_materials is not None:
        print("📌 Materials Data:")
        print(df_materials.head())  # Show first 5 rows
