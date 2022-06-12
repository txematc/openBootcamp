'''
Created on 12 jun 2022

@author: txema
'''
import tkinter
from tkinter import ttk

def salir(event):
    ventana.quit()

ventana = tkinter.Tk()
ventana.columnconfigure(0,weight =1)

selecionado = tkinter.StringVar()
r1 = ttk.Radiobutton(ventana, text = 'opcion 1', value = 1, variable = selecionado )
r2 = ttk.Radiobutton(ventana, text = 'opcion 2', value = 2, variable = selecionado )
r3 = ttk.Radiobutton(ventana, text = 'opcion 3', value = 3, variable = selecionado)

r1.grid(column = 0, row = 1, ipadx=50,ipady=10)
r2.grid(column = 0, row = 2, ipadx=50,ipady=10)
r3.grid(column = 0, row = 3, ipadx=50,ipady=10)


botonSalir = tkinter.Button(ventana, text='salir')
botonSalir.grid(column = 1, row = 4, ipadx=20, ipady=30)
botonSalir.bind('<Button-1>',salir)

ventana.mainloop(0)