import _sqlite3

conn = _sqlite3.connect('new.db')
cursor = conn.cursor()

cities = [
('Boston', 'MA', 600000),
('Chicago', 'IL', 2700000),
('Houston', 'TX', 2100000),
('Phoenix', 'AZ', 1500000)
]

cursor.executemany('INSERT INTO population VALUES (?, ?, ?)', cities)

conn.commit()
conn.close()