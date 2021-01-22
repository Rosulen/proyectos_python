# Guia herramientas básicas de dps con python

### Creación de vectores y graficación

Para reconocer los valores como en matlab se usa la libreria numpy, algunas de las operaciones básicas y necesarias con vectores son:

```py
import numpy as np

## Definición de un vector
x = np.array([1,5,7,9,0]) # Los vectores empiezan desde la posicion 0
y = np.array([1,5,6,8,3])

## suma de vectores
c = x + y

## imprimir el valor de los vectores en posiciones especificas
print(x[3]) # imprimir el valor de x en la posicion 3, deberá imprimir 9
print(c) # Imprimir la suma de los vectores c

## Reemplazar vectores en posiciones especificas
l = x[1:3] # l tomará los valores de x desde la posicion 1 hasta la 3, entonces el valor de l será 5,7,9
x[1] = 10 # Reemplazar la posición 1 del vector x por 10
x = 2*x # Multiplicar todo un vector por un escalar

## Llenar matrices
n = np.zeros(10) # Llenar una matriz con ceros, llenar un vector de longitud 10 con 0
n1 = np.ones(10) # Llenar una matriz con ceros, llenar un vector de longitud 10 con 0
print(n)

```

Hacer un plot de los vectores

```py
import numpy as np
import matplotlib.pylab as plt

x = np.array([1,3,6,7,5])

plt.plot(x) # poner en grafica x
plt.show() # mostar la gráfica de x

```
### Lectura, grabar y gráficar audio

ver el archivo [Leer, gráficar y recortar audio](./read_audio.py)

ver el archivo [grabar un audio y guardarlo](./write_audio.py)

### Operaciones con audios

ver el archivo [suma de audios](./suma.py)

### FFT

Para hacer la transformada rápida de fourier con dos señales

ver archivo [transformada de fourier de dos señales](./fft.py)

ver archivo [tranformada de fourier aplicada a audios](./fft_audio.py)

## Filtros 

Ver archivo [filtros pasa altos y pasa bajos](./high_low_filters.py)

ver archivo [filtros pasabanda y rechaza banda](./pass_stop_filters.py)

# Interface gráfica con python (tk-inter)

## Mostrar un ventana sencilla, con texto adentro

```py

import tkinter as tk

ventana = tk.Tk()
ventana = tk.Frame(height=20,width=100, cursor="arrow") # Tamaño de la ventana
ventana.pack(padx=100,pady=100) # Contenedor de la ventana
texto = tk.Label(ventana,text="ventana de prueba", foreground='black') # Tenxo que va dentro de la ventana
texto.pack()

ventana.mainloop() # Mostrar ventana
```
<p align="center"> <img src=./imagenes/ventana.png> </p>

## Creación de botones y cuadros de texto

```py

import tkinter as tk

## Creación de botones
# En estos dos parametros se se define también el tipo de letra, tamaño y la posición dondé se imprimirá el resultado

def saludar():
    lblsaludar = tk.Label(ventana, text="Hola " + usuario.get(),font=("Consolas", 14)).place(x=10, y=150) # Definir los valores a imprimir cuando se presione el boton saludar, debe imprimir "Hola Camila"

def despedir():
    lbldespedir = tk.Label(ventana,text="Chao " + nombre.get(),font=("Consolas", 14)).place(x=10, y=200) # Definir los valores a imprimir cuando se presione el boton despedir, debe imprimir "Chao Rosulen"

ventana = tk.Tk()
ventana.geometry("500x300+100+200") # Geometria de la ventana
ventana.title("Nombre del formulario") # Nombre de la interface

lblusuario1 = tk.Label(text="Usuario", fg="black", font=("Consolas",14)).place(x=10,y=10) # Ponet la palabra usuario en el formulario
usuario = tk.StringVar() # Creando cuadro de texto para campo de respuesta 
usuario.set("Camila") # Llenar el cuadro de texto
txtusuario = tk.Entry(ventana, textvariable = usuario).place(x=90,y=13) # Tamaña del cuadro de texto

# Se repite el mismo procedimiento para los cuadros de texto restantes 
lblnombre = tk.Label(text="Nombre", fg="black", font=("Consolas",14)).place(x=10,y=50)
nombre = tk.StringVar()
nombre.set("Rosulen")
txtnombre = tk.Entry(ventana, textvariable = nombre).place(x=90,y=53)

btnsaludar = tk.Button(ventana,text="Saludar",command=saludar,font=("Agency FB",14)).place(x=100,y=100) # Creación del boton saludar 
btnsdespedir= tk.Button(ventana,text="Despedir",command=despedir,font=("Agency FB",14),).place(x=300,y=100) # Creación del boton despedir

ventana.mainloop() # Mostrar ventana

```

<p align="center"> <img src=./imagenes/formulario.png> </p>


