'''
Created on 11 jun 2022

@author: txema
'''
from functools import reduce

def pares(lista): 
    resultado = list(filter((lambda x: x % 2 == 0), lista)) 
    print(resultado)
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(resultado)
    
def pares1(numeros):
    resultado1 = list(filter((lambda x: x%2==0), numeros))
    print(resultado1)
    resultado1 = reduce((lambda x ,y: x+y),resultado1)
    print(resultado1)

lista = list(range(100))
numeros = [1,2,3,4,5,6,7,8,9,10]


pares(lista)
pares1(numeros)