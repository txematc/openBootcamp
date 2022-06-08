'''
Created on 4 jun 2022

@author: txema
'''

class Vehiculo:
    
    color = "" 
    puertas = 0
    ruedas = 0
    
class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0
    
    
miCoche =Coche()
miCoche.color="blanco"
miCoche.puertas = 4
miCoche.ruedas = 4
miCoche.velocidad = 220
miCoche.cilindrada = 2000

print("El color de mi coche es :", miCoche.color)
print("Mi coche tiene",miCoche.puertas, "puertas y tiene",miCoche.ruedas, "ruedas")
print("Alcanza una velocidad maxima de", miCoche.velocidad , "Km/h y tiene una cilindrada de", miCoche.cilindrada , "centrimetros cubicos")
    
    
