import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cities = [
('New York City', 'Northeast'),
('San Francisco', 'West'),
('Chicago', 'Midwest'),
('Houston', 'South'),
('Phoenix', 'West'),
('Boston', 'Northeast'),
('Los Angeles', 'West'),
('Houston', 'South'),
('Philadelphia', 'Northeast'),
('San Antonio', 'South'),
('San Diego', 'West'),
('Dallas', 'South'),
('San Jose', 'West'),
('Jacksonville', 'South'),
('Indianapolis', 'Midwest'),
('Austin', 'South'),
('Detroit', 'Midwest')
]

cursor.execute("SELECT population.city, population.population, regions.region FROM population, regions WHERE population.city = regions.city ORDER BY population.city ASC")
rows = cursor.fetchall()
for row in rows:
    print(row[0], row[1], row[2])