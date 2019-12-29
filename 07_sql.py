import sqlite3


conn = sqlite3.connect('new.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM population WHERE state='Chui'")

conn.commit()