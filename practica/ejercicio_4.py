'''
Created on 25 may 2022
@author: txema
'''
edad = int(input("Introduzca su edad: "))

if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
    

#ejerciccio 2

# Usaremos la función input("mensaje") para solicitar algo al usuario por consola
numero_inicial: int = int(input('Introduce un número: '))
numero_final: int = int(input('Inroduce otro número: '))
numeros_impares: [int] = []

# Mientras el número final sea menor al número inicial pedira que el segundo número sea mayor al primero.
while numero_final <= numero_inicial:
    numero_final: int = int(input('El segundo número debe ser mayor que el primero. Inroduce otro número: '))

# Recorremos el rango de los números para mostrar los números impares
for i in range(numero_inicial, numero_final+1):
    if(i % 2 != 0):
        numeros_impares.append(i)

print(f"Lista de Números impares entre {numero_inicial} y {numero_final}:")
print(numeros_impares)

# ejercicio 3
rango_1_100 = range(1,101)

# Se muestra el rango de números desde 100 hasta 1
for i in reversed(rango_1_100):
    print(f"- {i}")