import _sqlite3

with _sqlite3.connect('new.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cars VALUES ('1990', 'BMW', 40)")

