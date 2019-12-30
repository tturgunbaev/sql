import sqlite3

conn = sqlite3.connect('cars.db')
cursor = conn.cursor()

# cursor.execute("DELETE FROM inventory")

# cursor.execute("INSERT INTO inventory VALUES ('Ford', 'Focus', 15)")
# cursor.execute("INSERT INTO inventory VALUES ('Ford', 'Mondeo', 11)")
# cursor.execute("INSERT INTO inventory VALUES ('Ford', 'Fiesta', 43)")
# cursor.execute("INSERT INTO inventory VALUES ('Honda', 'Civic', 13)")
# cursor.execute("INSERT INTO inventory VALUES ('Honda', 'Accord', 30)")

# cursor.execute("UPDATE inventory SET quantity = 3 WHERE make = 'Honda'")
cursor.execute("SELECT * FROM inventory WHERE make = 'Ford'")

rows = cursor.fetchall()
for row in rows:
    print(row[0], row[1], row[2])

conn.commit()
conn.close()