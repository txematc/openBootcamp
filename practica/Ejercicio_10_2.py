'''
Created on 12 jun 2022

@author: txema
'''
from tkinter import *


ventana = Tk()
pais = StringVar()
listbox = Listbox(ventana)

for item in ["España", "Maruecos", "Estonia", "Francia", "Italia", "Suiza", "Portugal", "Suecia"]:
    listbox.insert(END, item)

listbox.pack()

label = Label(text="Lista de nombres de paises")
label.pack()

ventana.mainloop()