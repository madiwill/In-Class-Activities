import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()


cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR, age INTEGER)')



cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
    ('Lenny', 17))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
    ('Nikash', 38))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
    ('Coban', 25))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
    ('Abdullah', 23))


cur.execute('SELECT name FROM Ages ORDER BY name')

conn.commit()
for row in cur:
     print(row)

cur.close()

conn.close()

# Code: http://www.py4e.com/code3/db1.py
# Or select Download from this trinket's left-hand menu