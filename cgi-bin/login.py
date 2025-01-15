import sqlite3
import cgi
import os
import json

print("Content-Type: application/json\n")

form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

# Initialize response
response = {"status": "failure", "message": "Unknown error"}

db_path = os.getcwd() + "/db/users.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))

user = cursor.fetchone()

if user:
    response["status"] = "success"
else:
    response["message"] = "Invalid credentials. Please try again."
conn.close()

print(json.dumps(response))
