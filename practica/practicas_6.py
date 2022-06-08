'''
Created on 28 may 2022

@author: txema
'''


class Juguete:
    _encendido=True
    def apaga(self):
        print("Apago el aparato ")
        self._encendido=False
    
    def enciende(self):
        print("Enciendo el aparato")
        self._encendido=True
        
    def isEncendido(self):
        return self._encendido; 
    
    
class Potato(Juguete):
    def quitarOreja(self):
        pass
    
    def ponerOreja(self):
        pass
    
class Dino(Juguete):
    def __init__(self, nombre):
        print("Estoy en el constructor")
    
    def verEscamas(self):
        pass


p=Potato()
p.enciende()
print(p.isEncendido())
p.apaga()
print(p.isEncendido())

        
class Vehiculo:
    
    ruedas=0
    combustible=""
    color= ""
    
    def acelerar(self):
        return self.acelerar;
        print("esta acelerando")
        
    def frenar(self):
        return self.frenar;
        print("estoy frenado")
        
class Coche(Vehiculo):
    color = None
    combustible = None
    
    def __init__(self, ruedas,combustible, color):
        self.ruedas = 4
        self.color = ""
        self.combustible = ""
    
    def arrancar(self):
        pass

class Moto(Vehiculo):
    pass    

miCoche=Coche(4,"blanco","diesel")
print(miCoche.color)
print(miCoche.ruedas)
print(miCoche.combustible)

miCoche2= Coche(4, "gris","electrico")
print(miCoche2.color)
print(miCoche2.ruedas)
print(miCoche2.combustible)
