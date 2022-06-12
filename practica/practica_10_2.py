'''
Created on 12 jun 2022

@author: txema
'''
## EVENTOS

import tkinter
from tkinter import ttk

ventana= tkinter.Tk()

def salir(event):
    print('Adios')
    ventana.quit()

def saludar(event):
    print('han hecho clik en saludar')
    
def saludarDobleClick(event):
    print('han hecho doble clik en saludar')
    
boton = tkinter.Button(ventana, text='Haz click')
boton.pack()
boton.bind('<Button-1>',saludar)
boton.bind('<Double-1>',saludarDobleClick)

botonSalir = tkinter.Button(ventana, text='salir')
botonSalir.pack()
botonSalir.bind('<Button-1>',salir)

ventana.mainloop(0)