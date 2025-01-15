import sqlite3
import cgi
import os
import json

print("Content-Type: application/json\n") 

# Get form data
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

# Initialize response
response = {"status": "failure", "message": "Unknown error"}

db_path = os.getcwd() + "/db/users.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Check if the username already exists
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
existing_user = cursor.fetchone()

if existing_user:
    response["message"] = "User already exists. Please choose a different username."
else:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    response["status"] = "success"
    response["message"] = "Registration successful! Please login to continue."

conn.close()

print(json.dumps(response))
