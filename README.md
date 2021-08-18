# Guia herramientas básicas de procesamiento digital de señales con python (DSP)

# Procesamiento digital de señales en audios

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

ver el archivo [Leer, gráficar y recortar audio](./codigos/read_audio.py)

ver el archivo [grabar un audio y guardarlo](./codigos/write_audio.py)

### Operaciones con audios

ver el archivo [suma de audios](./codigos/suma.py)

### FFT

Para hacer la transformada rápida de fourier con dos señales

ver archivo [transformada de fourier de dos señales](./codigos/fft.py)

ver archivo [tranformada de fourier aplicada a audios](./codigos/fft_audio.py)

## Filtros 

Ver archivo [filtros pasa altos y pasa bajos](./codigos/high_low_filters.py)

ver archivo [filtros pasabanda y rechaza banda](./codigos/pass_stop_filters.py)

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

## Poner imagenes en botones

---
FALTA 
---

## Check botton en python

```py
from tkinter import *

def lenguajes(): # Esta función imprime los valores asignados de los botones selesccionados en consola

    c=selc.get()
    cc=selecc.get()
    java=seljava.get()
    ruby=seleruby.get()
    php=selephp.get()
    python=selpython.get()
    print(c)
    print(cc)
    print(java)
    print(ruby)
    print(php)
    print(python)

    if(c==1): # si el primero está seleccionado, entonces la ventana se cerrará
        ventana.destroy()
        
ventana=Tk()
ventana.geometry("500x500+100+100")
ventana.title("Ejemplo checkbutton")
lblpregunta=Label(ventana,text="Que lenguajes conoces").place(x=100,y=40)

#creando los checkbox
selc=IntVar()
selecc=IntVar()
seljava=IntVar()
seleruby=IntVar()
selpython=IntVar()
selephp=IntVar()

chkc=Checkbutton(ventana,text="c",variable=selc, # La variable selc es la variable que pbtendrá el valor del boton
                   onvalue=1,offvalue=0).place(x=100,y=60)
chkcc=Checkbutton(ventana,text="c++",variable=selecc,
                   onvalue=1,offvalue=0).place(x=100,y=80)
chkjava=Checkbutton(ventana,text="java",variable=seljava,
                   onvalue=1,offvalue=0).place(x=100,y=100)
chkruby=Checkbutton(ventana,text="ruby",variable=seleruby,
                   onvalue=1,offvalue=0).place(x=100,y=120)
chkpython=Checkbutton(ventana,text="python",variable=selpython,
                   onvalue=1,offvalue=0).place(x=100,y=140)
chkphp=Checkbutton(ventana,text="php",variable=selephp,
                   onvalue=1,offvalue=0).place(x=100,y=160)

btnlenguajes=Button(ventana,text="Cuales Seleccione",command=lenguajes # Se crea un boton que redirecciona a la funcion lenguajes
                    ).place(x=100,y=220)

ventana.mainloop()
```

<p align="center"> <img src=./imagenes/seleccionar_check.png> </p>

## Radio button

```py

from tkinter import *
from tkinter import messagebox

def estado():
    s=selec.get()
    
    #tkMessageBox.showinfo(title="Tu Diagnostico",message="HOY  "+str(s))

    if s==1:
        messagebox.showinfo(title="Tu Diagnostico", message="Exelente")
    elif s==2:
        messagebox.showinfo(title="Tu Diagnostico", message="Muy Bien")
    elif s==3:
        messagebox.showinfo(title="Tu Diagnostico",message="Bien")
    elif s==4:
        messagebox.showinfo(title="Tu Diagnostico", message="hola bienvenido")    
    elif s==5:
        messagebox.showinfo(title="Tu Diagnostico",  message="Muy Mal")
    
ventana=Tk()

ventana.geometry("500x500+100+100")
ventana.title("Ejemplo radiobutton")

## crear radio button
lblanime=Label(ventana,text="como te sientes hoy"
               ).place(x=100,y=70)

selec=IntVar()
rdbanimoE=Radiobutton(ventana,text="Exclente",
                     value=1,variable=selec,command=estado).place(x=100,y=100) # se pone el valor que tomará una vez esté activado
rdbanimoMB=Radiobutton(ventana,text="Muy Bien",
                     value=2,variable=selec,command=estado).place(x=100,y=130)
rdbanimoB=Radiobutton(ventana,text="Bien",
                     value=3,variable=selec,command=estado).place(x=100,y=160)
rdbanimoM=Radiobutton(ventana,text="Mal",
                     value=4,variable=selec,command=estado).place(x=100,y=190)
rdbanimoP=Radiobutton(ventana,text="Muy Mal",
                     value=5,variable=selec,command=estado).place(x=100,y=220)

ventana.mainloop()
```

<p align="center"> <img src=./imagenes/seleccionar_radio.png> </p> <p align="center"> <img src=./imagenes/seleccionar_radio1.png> </p>

## Agregar Imagen a un boton

```py
from tkinter import *
from tkinter import messagebox

def saluda():
    messagebox.showinfo("saludando con messagebox",message="hola bienvenido")

ventana=Tk()
ventana.geometry("500x500+100+100")
ventana.title("Ejemplo imagen a botton y messagebox")

imgbottoon=PhotoImage(file="imagen.gif")
btnsaluda=Button(ventana,image=imgbottoon,command=saluda,height=312,width=344).place(x=100,y=100)

ventana.mainloop()
```

<p align="center"> <img src=./imagenes/boton_imagen.png> </p>

Una vez se da clic en el boton con la imagen, como resulatado se obtiene un mensaje flotante

<p align="center"> <img src=./imagenes/boton_mensaje.png> </p>

## Creación de slider

```py
from tkinter import *
from tkinter import messagebox

def temperatura(): # Muestra un mensaje del valor de la temperatura
    temper="Estamos a "+ str(valor.get())
    print(temper)
    messagebox.showinfo(title="temperatura",message=temper)

ventana=Tk()
ventana.geometry("500x500+100+100")
ventana.title("Ejemplo slider")

## Creacion del slider

valor=IntVar()
sldbarra=Scale(ventana,label="Temperaturas C",orient=HORIZONTAL,length=350,width=25,from_=-15,to=50,tickinterval=10,variable=valor).place(x=100,y=100) # Titulo del slider, se selecciona si es horizontal o vertical, tamaño, de que valor a que valor y los intervalos en los que va a crecer  
btnver=Button(ventana,text="Ver temperatura",command=temperatura).place(x=100,y=200) # Boton que llama a la función temperatura

ventana.mainloop()
```
<p align="center"> <img src=./imagenes/slider.png> </p>

## spinbox

```py
from tkinter import *

ventana=Tk()
ventana.geometry("500x300+100+100")
ventana.title("Ejemplo spinbox")

## Creando un spinbox de palabras
lblcalifT=Label(text="calificaciones en texto:",fg="blue",
               font=("Agency FB",14) ).place(x=20,y=100) # El texto
spncaliT=Spinbox(ventana,values=("Reprobado","Setenta",
                                 "Ochenta","Noventa","Cien")) # Las opciones que trandrá la caja

#concatenar el 88
spncaliT.insert(END,"88") # concatenar en número 88 en la primera casilla
spncaliT.place(x=280,y=105)


lblcalifN=Label(text="calificaciones en numero:",fg="blue",
               font=("Agency FB",14) ).place(x=20,y=150) # E texto
spncaliN=Spinbox(ventana,from_=70,to=100).place(x=280,y=155) # Las opciones de numeros, la minima es 70 y la maxima es 100

ventana.mainloop()
```

<p align="center"> <img src=./imagenes/spinbox.png> </p>

## Creación de menus

```py

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
```
<p align="center"> <img src=./imagenes/menu.png> </p>

---
# Procesamiento digital de señales en imagenes

### leer y publicar una imagen

Se usa la librería OpenCV

```py
import cv2 as cv 
import sys

img=cv.imread('/home/angie/Documents/git/python_dsp/imagen.png',0) ## El cero es para poner la imagen en blanco y negro
cv.imshow('titulo de la ventanda',img) 

while (True):
    
    k = cv.waitKey(1) & 0xFF

    # Metodo de salida

    if k==ord('e'):
        cv2.destroyAllWindows()
    elif k==ord('s'):
        cv2.imwrite("hola.png",img) ## se guarda la imagen
        cv2.destroyAllWindows()

```
Como la ventana queda en un loop infinito se debe poner un metodo de salida, en este caso será la tecla e, para salir y la tecla s para guardar

<p align="center"> <img src=./imagenes/dog.png>

```py
img=cv.imread('/home/angie/Documents/git/python_dsp/imagen.png')
```
</p><p align="center"> <img src=./imagenes/dog2.png> </p>

```py
img=cv.imread('/home/angie/Documents/git/python_dsp/imagen.png',0)
```

### Slider y matrices de color

```py
import cv2
import numpy as np

def nothing(x):
    pass

# Creacion de matrices
img = np.zeros((300,512,3), np.uint8) # Se crean 3 matrices de 300x512 con el valor de 0, es decir qua la imagen queda de color negro
cv2.namedWindow('image') # Nombre de la ventana

# Creacion de sliders para cambiar el color
cv2.createTrackbar('R','image',0,255,nothing) # Creacion de slider que contiene los rojos desde 0 - 255
cv2.createTrackbar('G','image',0,255,nothing) # Creacion de slider que contiene los verdes
cv2.createTrackbar('B','image',0,255,nothing) # Creacion de slider que contiene los azules

# Crear on off de programa
switch = '0 : OFF \n1 : ON' # Swicth para prender y apagar el programa
cv2.createTrackbar(switch, 'image',0,1,nothing) # el switch solo toma valores de 0 y 1

while(1):

    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: # Si la tecla e está activada entonces se sale del while
        break

    # SE toman los velores del los slides
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    # Se verifica el estado del switch
    if s == 0: # si está en 0 no hace nada
        img[:] = 0
    else:
        img[:] = [b,g,r] # Si está en uno combina los colores y los publica

cv2.destroyAllWindows()
```
El resultado será el siguiente, si el switch está apagado el resultado será el siguiente

</p><p align="center"> <img src=./imagenes/slider_negro.png> </p>

Si está encendido

</p><p align="center"> <img src=./imagenes/slider_color.png> </p>

El color del slider cambiará dependiendo de los valores del slider

### BInarización de una imagen

Hay varios tipos de metodos para binarizar una imágen, en el siguiente codigo se pueden ver 6 diferentes y como obtenerlos a travez del código.

```py
import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

img = cv.imread('/home/angie/Documents/git/python_dsp/imagen.png',0)
ret,thresh1 = cv.threshold(img,60,120,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,60,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,60,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    
     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
     plt.title(titles[i])
     plt.xticks([]),plt.yticks([])

plt.show()
```
El resultado será

</p><p align="center"> <img src=./imagenes/binarizar_imagen.png> </p>

### Uso de la camara

```py
import cv2
import numpy as np
from matplotlib import pyplot as plt


cap=cv2.VideoCapture(2) ## puerto de la camara
while (True):
    
    rec,frame=cap.read()
    

    cv2.imshow('video',frame)
    
    if cv2.waitKey(1)  & 0xff==ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
```

### Video con binarización

```py
import cv2
import numpy as np
from matplotlib import pyplot as plt


#cap=cv2.VideoCapture(0)
cap1=cv2.VideoCapture(2)

while (True):
   # rec, frame=cap.read()
    rec1, frame1=cap1.read()


    #cv2.imshow('video1',frame)
    cv2.imshow('video2',frame1)

    #f= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#convierte a grises
    #ret,thresh1 = cv2.threshold(f,127,255,cv2.THRESH_BINARY)
    #cv2.imshow('video3',thresh1)


    f= cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)#convierte a grises
    ret,thresh2 = cv2.threshold(f,127,255,cv2.THRESH_BINARY)
    cv2.imshow('video4',thresh2)
    
    ret,thresh3 = cv2.threshold(f,60,255,cv2.THRESH_TRUNC)
    cv2.imshow('video5',thresh3)
    ret,thresh4 = cv2.threshold(f,127,255,cv2.THRESH_TOZERO)
    cv2.imshow('video6',thresh4)
    ret,thresh5 = cv2.threshold(f,127,255,cv2.THRESH_TOZERO_INV)
    cv2.imshow('video7',thresh5)
    
    if cv2.waitKey(1)  & 0xff==ord('q'):
        break

#cap.release()
cap1.release()
cv2.destroyAllWindows()
```