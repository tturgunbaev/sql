import sqlite3
import csv

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

employees = csv.reader(open('employees.csv', 'rU'))


try:
    # cursor.execute("CREATE TABLE employees (firstnale TEXT, lastname TEXT)")
    cursor.executemany("INSERT INTO employees VALUES (?, ?)", employees)
    conn.commit()
except sqlite3.OperationalError as e:
    print (f"We cath error:  '{e}'")
finally:
    conn.close()