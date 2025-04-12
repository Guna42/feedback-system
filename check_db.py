import sqlite3
conn = sqlite3.connect('feedback.db')
cursor = conn.execute('SELECT * FROM feedback')
for row in cursor:
    print(row)
conn.close()