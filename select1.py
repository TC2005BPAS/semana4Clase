import sqlite3

mydb = sqlite3.connect("PAS.db")
cur = mydb.cursor()

stringSQL = '''SELECT id, first_name, last_name, email 
FROM Users'''

rows = cur.execute(stringSQL)

for r in rows:
    print(r[0], r[1], r[2], r[3])

mydb.close()
