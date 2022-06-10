'''
Created on 9 jun 2022

@author: txema
'''
from pickle import * 

class Vehiculo:
    combustible = ''
    ruedas = 0
    
    def __init__(self, combustible,ruedas):
        self.combustible = combustible
        self.ruedas = ruedas
        
    def __str__(self):
        return f'El vehiculo esta impulsado por {self.combustible} y tiene {self.ruedas} ruedas'
    
peugeot = Vehiculo('diesel', '4')
print(peugeot)

f = open('vehiculo_escogido', 'w+b')

dump(peugeot,f)

f.seek(0)
nuevo_peugeot = load(f)

print(nuevo_peugeot)
f.close()