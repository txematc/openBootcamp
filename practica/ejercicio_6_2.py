'''
Created on 4 jun 2022

@author: txema
'''
class Alumno:
    def iniciar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def imprimirPantalla(self):
        print("Nombre: ",self.nombre)
        print("Nota: ", self.nota)
        
    def evaluar(self):
        if self.nota < 5:
            print("El alumno está suspenso")
        else:
            print("El alumno ha aprobado")
            
alumno1 = Alumno()
alumno2=Alumno()
alumno3 = Alumno()

alumno1.iniciar("Txema", 5)
alumno2.iniciar("Soraya", 9)
alumno3.iniciar("Claudia", 4)

alumno1.imprimirPantalla()
alumno1.evaluar()

alumno2.imprimirPantalla()
alumno2.evaluar()

alumno3.imprimirPantalla()
alumno3.evaluar()