import sqlite3
import json
import collections

mydb = sqlite3.connect("PAS.db")
cur = mydb.cursor()

stringSQL = '''SELECT Users.first_name, Party.date, Party.score FROM
 Users JOIN Party ON Users.id = Party.user'''

rows = cur.execute(stringSQL)
lista_salida = []
for r in rows:
    d = {}
    d["nombre"] = r[0]
    d["fecha"] = r[1]
    d["puntaje"] = r[2]
    lista_salida.append(d)
j = json.dumps(lista_salida)
print(j)    

f = open("salidaJSON.txt", "w")
f.write(j)
f.close()

mydb.close()
