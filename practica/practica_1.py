## Control de flujo con condicionales
from pickle import TRUE

a=5
b=6
c=7
resultado= (a<b and c==7) 
print(resultado)

##Tabla de la verdad en AND

print("T y T", True  and True)
print("T y F", True and False)
print("F y T", False and True)
print("F y F", False and False)


print()
## Tabla de la verdad OR

print("T y T", True  or True)
print("T y F", True or False)
print("F y T", False or True)
print("F y F", False or False)

resultado = (a>=5 or c<7)
print()
print(resultado)