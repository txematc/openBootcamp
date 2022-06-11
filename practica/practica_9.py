'''
Created on 11 jun 2022
Practicas del video 9 
@author: txema
'''
#ejemplo de programción multihilo para ejecutar dos o mas hilos o funciones a la vez

import _thread
import time

def horaActual(nombre_thread, tiempo_de_espera):
    contador = 0
    while contador< 5:
        
        time.sleep(tiempo_de_espera)
        contador +=1
        print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')
        


_thread.start_new_thread(horaActual,('thread_uno', 1))
_thread.start_new_thread(horaActual,('theread_dos', 5))

while True:
    pass