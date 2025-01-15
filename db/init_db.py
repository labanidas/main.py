import sqlite3
import os

# Connect to the database (creates it if it doesn't exist)
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/database.db'))
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Create stats table
cursor.execute('''
CREATE TABLE IF NOT EXISTS stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    value INTEGER
)
''')

conn.commit()
conn.close()

print("Database and tables created successfully.")
