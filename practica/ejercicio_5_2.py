'''
Created on 28 may 2022

@author: txema
'''
def numeroPrimo():
    numero=int(input("introduce un número: "))
  
    if numero>1:
        for i in range(2,int(numero)):
            if(int(numero)%i==0):
                print(f"Lo siento, el número {numero} NO ES PRIMO. Es divisible entre el {i}")
                break
        else:
            print(f"Bravo, el número {numero} es primo")
    else:
        print(f"Ohhh, el número {numero} No es primo, los numeros primos tienen que ser mayores de 1")
         
       
print(numeroPrimo())