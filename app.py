from flask import Flask
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = Flask(__name__)

@app.route("/")
def home():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    cur.execute("SELECT * FROM Asamy LIMIT 1;")
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return f"ID: {row[0]}, Name: {row[1]}"
    else:
        return "No rows found."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
