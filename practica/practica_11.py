## ejercicios de practicas del video 11 de OpenBootcam
#se trata de las bases de datos desde Python
import sqlite3

conexion=sqlite3.connect("miaplicacion.db")
conexion.execute("""create table if not exists usuarios (
                          id integer primary key AUTOINCREMENT,
                          usuario text,
                          password text
                    )""")
conexion.close()


conexion=sqlite3.connect("miaplicacion.db")

conexion.execute("insert into usuarios(usuario,password ) values (?,?)", ("Txema", 'clave1'))
conexion.execute("insert into usuarios(usuario,password ) values (?,?)", ("Soraya", 'clave2'))
conexion.execute("insert into usuarios(usuario,password ) values (?,?)", ("Claudia", 'clave3'))
conexion.commit()

conexion.close()

conexion=sqlite3.connect("miaplicacion.db")

cursor=conexion.execute("select id,usuario,password  from usuarios")
for fila in cursor:
    print(fila)

conexion.close()

