import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR, age INTEGER)')

cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Bronte', 14))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Lucien', 21))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Catharine', 21))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Bendeguz', 32))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Tymom', 28))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Simra', 13))


cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

conn.commit()
for row in cur:
	print (row)
	break

cur.close()

conn.close()