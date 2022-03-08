import sqlite3

mydb = sqlite3.connect("PAS.db")
cur = mydb.cursor()

stringSQL = '''SELECT Users.first_name, Party.date, Party.score FROM
 Users JOIN Party ON Users.id = Party.user'''

rows = cur.execute(stringSQL)

for r in rows:
    print(r[0], r[1], r[2])

mydb.close()
