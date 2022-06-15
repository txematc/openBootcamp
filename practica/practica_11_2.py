import sqlite3
import getpass
from unicodedata import name





def main():
    usuario= input('introduzca el nombre de usuario: ')
    password = input('Introduzca su contraseña: ')
    if verifica_credenciales(usuario, password):
        print('Login correcto')
    else:
        print('login incorrecto')

def verifica_credenciales(usuario, password ):
    conexion = sqlite3.connect('miaplicacion.db')
    cursor= conexion.cursor()
    query = cursor.execute(f"SELECT id FROM usuarios WHERE usuario='{usuario}' AND password ='{password }'")
    rows = cursor.execute(query)
    data = rows.fetchone()
    print(data)
    
    
    cursor.close()
    conexion.close()

conexion = sqlite3.connect('miaplicacion.db')
cursor = conexion.cursor()

conexion.execute("insert into usuarios(usuario,password ) values (?,?)", ("Patry", 'clave4'))
conexion.commit()
cursor.close()
conexion.close()


if __name__=='__main__':
    main()