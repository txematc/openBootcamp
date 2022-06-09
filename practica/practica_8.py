'''
Created on 9 jun 2022
 Estos son ejercicios del video 8 del curso
@author: txema
'''

numero = 511
texto = "El quijote"
otromas = 1.2

#Está es la forma que se usaba hasta Python 3.6
# print("El numero es {} y el texto {} y tiene {}".format(numero,texto,otromas))


#Esta es la nueva forma, es codigo python lo cual
#nos permite añadir funcionalidades a las variables 
#como en el ejemplo upper que nos convierte la variable texto a mayusculas.

#tambien podemos ejecutar una funcion como suma por ejemplo
def suma(a,b):
    return a+b

print(f"El número es {suma(numero,numero)} y el texto {texto.upper()} y tiene {otromas}")


#otra cosa del video

class Juguete:
    nombre = ""
    precio = 0.0
    
    #creamos el constructor
    def __init__(self, nombre,precio):
        self.nombre = nombre
        self.precio = precio
        
        
    # Vamos a hacer lo que se llama sobrecarga de metodo
    #todas las clases tienen este metodo
    
    def __str__(self):
        return f"Mi nombre es {self.nombre} y tengo un precio de {self.precio}"
      
    # tambien podemos sobrecargar con el siguiente metodo que es similar
    
    def __repr__(self):
        return f"Mi nombre es {self.nombre} y tengo un precio de {self.precio}"
        
    
    
j1 = Juguete("Potato", 10.5)

print(j1)

j2 = Juguete("Dino", 8.5)

print(j2)

# Otras funciones

cadena = "En un lugar de la Mancha"
print(cadena.capitalize())
print(cadena.upper())
print(cadena.lower().count("a"))
print(cadena.split())