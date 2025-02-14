import os
import psycopg2

# Load database URL from Render environment variables
DB_URL = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    print("✅ Connected to Render PostgreSQL!")
except Exception as e:
    print("❌ Error connecting to database:", e)
