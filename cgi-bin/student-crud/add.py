import sqlite3
import cgi
import os
import json

print("Content-Type: application/json\n")

response = {"status": "failure", "message": "Unknown error", "student": None}

form = cgi.FieldStorage()
name = form.getvalue('name')
roll = form.getvalue('roll')
marks = form.getvalue('marks')



db_path = os.getcwd() + "/db/students.db"


conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll TEXT NOT NULL UNIQUE,
    marks INTEGER NOT NULL
)
''')

# Check if student with the same roll number already exists
cursor.execute("SELECT * FROM students WHERE roll = ?", (roll,))
exists = cursor.fetchone()

if exists:
    response["message"] = "Student with this roll number already exists."
else:
    # Insert the student into the database
    cursor.execute("INSERT INTO students (name, roll, marks) VALUES (?, ?, ?)", (name, roll, marks))
    conn.commit()

    # Get the ID of the newly inserted student
    student_id = cursor.lastrowid

    # Prepare the response with student details
    response["status"] = "success"
    response["message"] = "Student created successfully"
    response["student"] = {"id": student_id, "name": name, "roll": roll, "marks": marks}


    conn.close()

# Return the response as a JSON object
print(json.dumps(response))
