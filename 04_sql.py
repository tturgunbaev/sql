import _sqlite3
import csv

conn = _sqlite3.connect('new.db')
cursor = conn.cursor()

employees = csv.reader(open("employees.csv", "r"))

cursor.execute("CREATE TABLE employees (firstname TEXT, lastname TEXT)")
cursor.executemany("INSERT INTO employees VALUES (?, ?)", employees)

conn.commit()
conn.close()