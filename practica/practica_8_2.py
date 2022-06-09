'''
Created on 9 jun 2022
Manipulando ficheros
@author: txema
'''

#conjunto de funciones de manipulacion de ficheros

f = open('C:/Users/txema/Desktop/python/POO/prueba.txt','r')

#caracteres especiales = significado en open
# r=lectura
# a=append
# w=escritura
# x= create

# t=texto
# b=bynary

# +=

datos = f.readlines()
f.close()

print(datos)

