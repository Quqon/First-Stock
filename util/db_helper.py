import sqlite3
conn = sqlite3.connect('universe_price.db', isolation_level=None)
cur = conn.cursor()

cur.execute('select * from balance')

row = cur.fetchone()
print(row)