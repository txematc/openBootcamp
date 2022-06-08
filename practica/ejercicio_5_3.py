'''
Created on 28 may 2022

@author: txema
'''
def anoBisiesto():
    ano=int(input("Introduce el año que quieres comprobar"))
    
    if (ano%4==0):
        print(f"El año escogido es bisiesto.")
        
    else:
        print(f"El año escogido no es bisiesto")
        
print(anoBisiesto())