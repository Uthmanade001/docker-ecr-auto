from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.getenv("POSTGRES_DB", "mydb"),
        user=os.getenv("POSTGRES_USER", "myuser"),
        password=os.getenv("POSTGRES_PASSWORD", "mypassword")
    )
    return conn

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"✅ Connected to PostgreSQL!<br>Version: {version[0]}"
    except Exception as e:
        return f"❌ Failed to connect to PostgreSQL<br>Error: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
# This code is a Flask application that connects to a PostgreSQL database.