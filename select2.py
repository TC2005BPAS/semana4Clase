import sqlite3

email = input("Introduce email a buscar: ")
mydb = sqlite3.connect("PAS.db")
cur = mydb.cursor()

stringSQL = '''SELECT id, first_name, last_name, email FROM Users WHERE email = ?'''

rows = cur.execute(stringSQL,(email,))
r = rows.fetchone()
if r == None:
    print("No existe el registro")
else:
    print(r[3])
'''
for r in rows:
    print(r[0], r[1], r[2], r[3])
'''

mydb.close()
