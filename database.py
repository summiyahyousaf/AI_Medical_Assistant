import sqlite3
import os

print(os.path.abspath("user.db"))
# Connect to database (creates user.db if it doesn't exist)
conn = sqlite3.connect("user.db")

cursor = conn.cursor()

# -------------------------------
# Users Table
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# -------------------------------
# Reports Table
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS reports (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_name TEXT,

    age INTEGER,

    gender TEXT,

    disease TEXT,

    confidence REAL,

    other_symptoms TEXT,

    report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

print(cursor.fetchall())


conn.close()

print("Database and tables created successfully!")