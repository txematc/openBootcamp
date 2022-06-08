'''
Created on 5 jun 2022

@author: txema
'''
import time

hora = time.strftime("%H")
minutos = time.strftime("%M")

if int(hora)>= 19:
    print("Es hora de ir a casa")
    
else:
    print("Quedan {} horas y {} minutos para acabar el curro". format(18 - int(hora), 59-int(minutos)))

