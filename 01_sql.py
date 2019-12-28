import _sqlite3

conn = _sqlite3.connect('new.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE population (city TEXT, state TEXT, population INT)")

conn.close()