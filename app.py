from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "testdb"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres")
    )
    return conn

@app.route('/')
def home():
    try:
        conn = get_db_connection()
        conn.close()
        return "task 4 completed !"
    except Exception as e:
        return f"Connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
