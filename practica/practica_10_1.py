'''
Created on 11 jun 2022

@author: txema
'''
from tkinter import ttk
import tkinter

def miFuncion():
    print('clicado')

ventana= tkinter.Tk()
ventana.columnconfigure(0, weight =1)

selecionado = tkinter.StringVar()
r1 = ttk.Radiobutton(ventana, text = 'si', value = 1, variable = selecionado, command = miFuncion)
r2 = ttk.Radiobutton(ventana, text = 'no', value = 2, variable = selecionado, command = miFuncion)
r3 = ttk.Radiobutton(ventana, text = 'quizas', value = 3, variable = selecionado, command = miFuncion)

r1.grid(column = 0, row = 1, ipadx=50,ipady=10)
r2.grid(column = 0, row = 2, ipadx=50,ipady=10)
r3.grid(column = 0, row = 3, ipadx=50,ipady=10)

ventana.mainloop(0)
