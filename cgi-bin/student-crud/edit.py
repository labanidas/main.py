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
id = form.getvalue('id')

if not name or not roll or not marks:
    response["message"] = "Missing required fields"
    print(json.dumps(response))
    exit()

db_path = os.getcwd() + "/db/students.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute(
    "UPDATE students SET name = ?, marks = ?, roll = ? WHERE id = ?",
    (name, marks, roll, id)
)

conn.commit()

if cursor.rowcount > 0:
    response["status"] = "success"
    response["message"] = "Student updated successfully"
else:
    response["message"] = "Student not found or no change made"

conn.close()

print(json.dumps(response))
