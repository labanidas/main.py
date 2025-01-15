import sqlite3
import cgi
import json

print("Content-Type: application/json\n")

# Fetch data from the SQLite database
def fetch_dashboard_data():
    conn = sqlite3.connect('../db/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stats")
    data = cursor.fetchall()
    conn.close()
    return data

if __name__ == "__main__":
    dashboard_data = fetch_dashboard_data()
    print(json.dumps(dashboard_data))