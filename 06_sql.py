import _sqlite3

conn = _sqlite3.connect('new.db')
cursor = conn.cursor()

c = cursor.execute("SELECT firstname, lastname FROM employees")

print(c)

rows = c.fetchall()

print(rows)