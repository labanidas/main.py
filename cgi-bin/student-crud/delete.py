import sqlite3
import cgi
import os
import json

print("Content-Type: application/json\n")

# Initialize response
response = {"status": "failure", "message": "Unknown error"}


form = cgi.FieldStorage()
id = form.getvalue('id')


db_path = os.getcwd() + "/db/students.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("DELETE FROM students WHERE id=?", (id,))
conn.commit()

if cursor.rowcount > 0:
    response["status"] = "success"
else:
    response["message"] = "No record found with the provided ID."

conn.close()


# Output the response as JSON
print(json.dumps(response))
