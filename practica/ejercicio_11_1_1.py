import sqlite3

conn = sqlite3.connect("miaplicacion2.db")
cursor = conn.cursor()
    

busqueda = input("Escribe tu búsqueda: ")

if not busqueda:
	print("Búsqueda inválida")
	exit()
 
sentencia = "SELECT * FROM alumnos WHERE nombre LIKE ?;"
 
cursor.execute(sentencia, [ "%{}%".format(busqueda) ])
	
alumnos = cursor.fetchall()

print(alumnos)
    

cursor.close()
conn.close()


