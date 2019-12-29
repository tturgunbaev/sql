import _sqlite3

conn = _sqlite3.connect('new.db')
cursor = conn.cursor()

# cursor.execute("CREATE TABLE cars (Make TEXT, Model TEXT, Quantity INT)")
cursor.execute("INSERT INTO population VALUES ('New York City', 'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES ('San Francisco', 'CA', 800000)")
cursor.execute("INSERT INTO population VALUES ('Bishkek', 'Chui', 1000000)")

conn.commit()

conn.close()