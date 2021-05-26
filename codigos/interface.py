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

""" from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
img = PhotoImage(Image.open("/home/angie/Git/python_dsp/imagenes/ventana.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop() """


from tkinter import *

def abrir():
    print ("hiciste clic en abrir")
    venabrir=Tk()
    venabrir.geometry("400x200+200+200")
    venabrir.title("otra ventana")
    venabrir.mainloop()

ventana=Tk()
ventana.geometry("600x600+100+100")
ventana.title("Ejemplo menus")

## Pasos para crear un menú

# Paso 1 crear la barra de menus
barramenu=Menu(ventana)

# Paso 2 crear los menus
mnuarchivo=Menu(barramenu)
mnuedicion=Menu(barramenu)

# Paso 3 crear los comandos de los menus
# Menú archivo
mnuarchivo.add_command(label="Abrir",command=abrir)
mnuarchivo.add_command(label="Nuevo")
mnuarchivo.add_command(label="Guardar")
mnuarchivo.add_command(label="Cerrar")
mnuarchivo.add_separator() # Hacer una divición en el menú
mnuarchivo.add_command(label="Salir",command=ventana.destroy)

# Menú edición
mnuedicion.add_command(label="Copiar")
mnuedicion.add_command(label="Pegar")
mnuedicion.add_command(label="Deshacer")
mnuedicion.add_command(label="Rehacer")

# Paso 4 agergar los menus a la barra de menus
barramenu.add_cascade(label="Arcivo",menu=mnuarchivo)
barramenu.add_cascade(label="Edicion",menu=mnuedicion)

# Paso 5 indicamos que la barra de menus estara en la ventana
ventana.config(menu=barramenu)

ventana.mainloop()
