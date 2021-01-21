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

