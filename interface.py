""" import tkinter as tk
#from tkinter import PhotoImage
from PIL import Image

ventana = tk.Tk()

ventana.geometry("700x600+0+0") # Geometria de la ventana
ventana.title("Imagen") # Nombre de la interface

## Crear imagen

#imagenl = tk.PhotoImage(file="imagen.gif")
imagenp = Image.open("/home/angie/Git/python_dsp/imagenes/ventana.png")

lblimagen = tk.Label(ventana, image=imagenp.show()).place(x=100,y=100) # Ponet la palabra usuario en el formulario
imagenp.show()

ventana.mainloop() # Mostrar ventana """



""" import tkinter as tk
from PIL import Image
import os """

from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
img = PhotoImage(Image.open("/home/angie/Git/python_dsp/imagenes/ventana.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()