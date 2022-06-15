import sqlite3

conn = sqlite3.connect('miaplicacion2.db')
cursor =conn.cursor()

conn.execute(""" CREATE TABLE IF NOT EXISTS alumnos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre text,
                        apellido text
)""")

conn.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?,?)",('Txema','Gonzalez'))
conn.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?,?)",('Soraya','Mateos'))
conn.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?,?)",('Claudia','Ortega'))
conn.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?,?)",('Mauro','Fernanadez'))
conn.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?,?)",('Jesús','Garcia'))
conn.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?,?)",('Juan Carlos','Menacho'))
conn.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?,?)",('Ursula','Martinez'))
conn.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?,?)",('Patry','Perez'))

conn.commit()
cursor.close()
conn.close()


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