import sqlite3
import cgi
import os
import json

print("Content-Type: application/json\n")

# Initialize response
response = {"status": "failure", "message": "Unknown error"}

db_path = os.getcwd() + "/db/students.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll TEXT UNIQUE NOT NULL,
    marks INTEGER NOT NULL
)
''')

cursor.execute("SELECT id, name, roll, marks FROM students")
students = cursor.fetchall()

student_list = []  

for student in students:
    student_list.append({"id": student[0], "name": student[1], "roll": student[2], "marks": student[3]})


response["status"] = "success"
response["data"] = student_list


print(json.dumps(response))
