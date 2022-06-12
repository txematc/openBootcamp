'''
Created on 11 jun 2022

@author: txema
'''
# Corresponde a las practicas del video 10 introducción a GUI (interfac grafica de usuario
from tkinter import ttk
import tkinter
from cgitb import text
from textwrap import fill
# Geometria pack
"""
COMENTADO PARA CONTINUAR OTRO EJERCICIO
ventana = tkinter.Tk()


label_saludo = tkinter.Label(ventana, text ='Hola!', bg='yellow')
label_saludo.pack(ipadx=100,ipady=80,fill='x')

label_medio = tkinter.Label(ventana, text ='Soy el intermedio', bg='green', fg='blue')
label_medio.pack(ipadx=150, ipady=200,expand=True)

label_adios = tkinter.Label(ventana, text = 'adios', bg='red')
label_adios.pack(ipadx = 50, ipady=80, fill='both')

ventana.mainloop(0)
"""
#geometria grid como una matriz se coloca en casillas

ventana1=tkinter.Tk()

ventana1.columnconfigure(0, weight=1)
ventana1.columnconfigure(0, weight=3)

#Usuario
username_label = ttk.Label(ventana1, text='username')
username_label.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5)

username_entry =ttk.Entry(ventana1)
username_entry.grid(column=1, row =0,sticky=tkinter.E, padx=10,pady=5)
#contraseña
pasword_label = ttk.Label(ventana1, text='pasword')
pasword_label.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)

pasword_entry =ttk.Entry(ventana1, show='*')
pasword_entry.grid(column=1, row =1,sticky=tkinter.E, padx=10,pady=5)
## Boton

login_button=ttk.Button(ventana1, text = 'enviar')
login_button.grid(column=2, row =2, sticky=tkinter.E)
ventana1.mainloop(0)