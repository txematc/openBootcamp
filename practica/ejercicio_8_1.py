'''
Created on 9 jun 2022

@author: txema
'''
f = open('mifichero2.txt','w')
f.write('Este es el fichero de texto\n')
f.write('creado para la práctica del video 8\n')
f.write('del curso básico de Python en OpenBootcamp\n')
f.close()

f = open('mifichero2.txt','r')
texto1 = f.read()
print(texto1)