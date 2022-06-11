'''
Created on 11 jun 2022

@author: txema
'''
# ejemplo de la libreria diversas funcionalidades 
from functools import reduce

#Aqui usamos filter
numeros = [1,2,3,4,5,6,7,8,9]

def mifuncion(x):
    if x % 2 ==0:
        return True
    
    return False



resultado = filter(mifuncion, numeros)
print(list(resultado))

# aqui usamos map
def cuadrado(x):
    return x * x 

resultado2 = map(cuadrado,[1,2,3,4,5,6,7,8,9,10])
print(list(resultado2))


# aqui usaremos reduce para lo cual importamos functools
def suma(a,b):
    print(f'a={a}, b={b}')
    return a+b 

res = reduce(suma,[1,2,3,4,5])
print(res)

#Otra funcion zip para unir elementos de una lista y una tupla

cursos =['java', 'python','git']
asistentes = [15,20,4]

demo = zip(cursos, asistentes)
print(list(demo))
