import sqlite3
import cgi
import os
import subprocess

print("Content-Type: text/html\n")

# Collect form data
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

# Define the database path
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/database.db'))

# Check if the database file exists
if not os.path.exists(db_path):
    # Initialize the database by executing init_db.py
    init_script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/init_db.py'))
    try:
        subprocess.run(["python", init_script_path], check=True)
        print("<p>Database initialized successfully.</p>")
    except subprocess.CalledProcessError as e:
        print(f"<p>Error initializing database: {e}</p>")
        exit()

# Connect to the database
try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Insert user data into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    print("<html><body>Registration successful! <a href='/templates/login.html'>Login</a></body></html>")
except sqlite3.Error as e:
    print(f"<p>Database error: {e}</p>")
