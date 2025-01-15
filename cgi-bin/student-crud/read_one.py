import sqlite3
import cgi
import os
import json

print("Content-Type: application/json\n")

response = {"status": "failure", "message": "Unknown error"}

form = cgi.FieldStorage()
id = form.getvalue('id') 

db_path = os.getcwd() + "/db/students.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT id, name, roll, marks FROM students WHERE id = ?", (id,))
student = cursor.fetchone()

if student:
    response["status"] = "success"
    response["message"] = {
        "id": student[0],
        "name": student[1],
        "roll": student[2],
        "marks": student[3]
    }

conn.close()

print(json.dumps(response))
