'''
Created on 26 may 2022

@author: txema
'''

numero_inicial = int(input("Introduce un número "))
numero_final = int(input("Introducce otro número "))

numeros_impares :[int]=[]

while numero_inicial >= numero_final:
    numero_final: int= int(input("El numero es más pequeño que el primero, introduce otro número, por favor"))
    
for i in range(numero_inicial,numero_final+1):
    if (i % 2 != 0):
        numeros_impares.append(i)
print(f"Lista de numeros elegidos {numero_inicial} y {numero_final}:")
print(numeros_impares)