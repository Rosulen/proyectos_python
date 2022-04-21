# Juego diana o tiro al blanco

El siguiente codigo presenta una solución de como hacer un juego de diana o tiro al blanco mediante la librería de python opencv, el juego consiste en tener una camara donde se muestre la diana y con un laser apuntar al objetivo, luego se replica una diana y se replican los objetivos apuntados y se determina el puntaje de este

____
## Detección de la diana, radio y contorno

Primero se debe identificar el radio mayor para tener una referencia de las coordenadas del punto cuando se apunte con el laser rojo, el codigo utilizado para esto es el siguiente codigo, las condiciones para que pueda detectar el circulo dependen de las condiciones de la luz, y para este las condiciones de luz son controladas lo que hace más facil la detección y binarización del mismo.

```py
import cv2
import numpy as np
import matplotlib.pylab as plt

# Cargar video
cv2.namedWindow('Normal') # nombre de la ventana
cap = cv2.VideoCapture(0) # dirección de la camara que se va a utilizar

while(1):

    _, frame = cap.read() # Take each frame 
    
    binario = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # pasar a blanco y negro la imagen original
    ret,binario = cv2.threshold(binario,80,255,cv2.THRESH_BINARY_INV) # Bnarizar la imagen original

    contornos, hierarchy = cv2.findContours(binario,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # encontrar los contornos de la imagen binarizada
        
    for c in contornos:

        if cv2.contourArea(c) > 70000: # Aplicar el circulo a las areas mayores a 70000 
            # Dibujar circulo
            (x,y),radius = cv2.minEnclosingCircle(c) # Paramatros encontrados
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(frame,center,radius,(0,255,0),2) # graficación del circulo, tamaño de grosor de contorno 2
            cv2.circle(frame,center, 5 ,(0,255,0),-1) # punto en el centro 
            # Poner todo en la misma imagen
            cv2.imshow("Normal", frame)
            # print(cv2.contourArea(c))

    cv2.imshow('Normal',frame)
    cv2.imshow('Binarizado',binario)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
```
<p align="center"> <img src=./imagenes/radioycontorno.png> </p>

____
## Detección del brillos o laser

Ahora se debe detectar los pixeles más brillantes, para esto se debe jugar con los parametros asignados a una mascara que solamente detecte los colroes rojos, pero los rojos más brillantes, entonces se varian los parametros de saturación, valor y matiz, para esto se usa el siguiente codigo.

```py
import cv2
import numpy as np

cap = cv2.VideoCapture(0) # Video

while(1):

    # Take each frame
    _, frame = cap.read() # video

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([150,20,255]) # de 150 - 180 se visualiza el espectro del color rojo
    upper_blue = np.array([180,20,255]) # 20 y 255, son parametros que se puden variar para detectar los pixeles más brillantes 

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    byn = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,normal = cv2.threshold(byn,60,255,cv2.THRESH_BINARY_INV)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask= mask)
    
    kernel = np.ones((15,15),np.uint8) # los valores del kernel (15,15) se puden variar dependiendo de como se quiera visualizar el punto, si más grandeo o más pequeño

    dilat = cv2.dilate(mask,kernel,iterations = 1)
    
    cv2.imshow('Normal',frame)
    cv2.imshow('Dilatación',dilat)
    # cv2.imshow('BInarizada',normal) ## para visualizar la imagen binarizada
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
```
<p align="center"> <img src=./imagenes/deteccion_brillos.png> </p>

_____
## Combinación de algoritmos

Ahora se combinan los algoritmos para que se pueda visualizar la imagen binarizada y a su vez detecte los piexeles más drillantes y pinte un punto donde se detecten los pixeles brillantes

```py
import cv2
import numpy as np
import matplotlib.pylab as plt

# Cargar video
cv2.namedWindow('Normal')
cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read() # Take each frame
    height, width = frame.shape[:2] 
    # print(f'{height},{width}')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Convert BGR to HSV
    lower_blue = np.array([150,20,255]) # Definir el rango de color, en este caso solamente los rojos más brillantes
    upper_blue = np.array([180,20,255]) # es decir, el rojo de la luz laser
    mask = cv2.inRange(hsv, lower_blue, upper_blue) # mascara para binarizar en el rango

    binario = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # pasar a blanco y negro la imagen original
    ret,binario = cv2.threshold(binario,80,255,cv2.THRESH_BINARY_INV) # Bnarizar la imagen original

    kernel = np.ones((15,15),np.uint8)
    dilat = cv2.dilate(mask,kernel,iterations = 1)

    contornos, hierarchy = cv2.findContours(binario,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
    for c in contornos:

        contador = contador + 1

        if cv2.contourArea(c) > 70000:
            # Dibujar circulo
            (x,y),radius = cv2.minEnclosingCircle(c)
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(frame,center,radius,(0,255,0),2)
            cv2.circle(frame,center, 5 ,(0,255,0),-1)
            print(f'El radio es = {radius}')
            cv2.imshow("Normal", frame)
            
    contornos, hierarchy = cv2.findContours(dilat,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for c in contornos:
        
        # Todos los puntos que encuentre en dilat, les asignará un punto en la imagen original
        cv2.contourArea(c)
        (x,y),radius = cv2.minEnclosingCircle(c)
        center = (int(x),int(y))
        radius = int(radius)
        cv2.circle(frame,center, 5 ,(0,255,0),-1)

    cv2.imshow('Normal',frame)
    cv2.imshow('Dilatación',dilat)
    cv2.imshow('Binarizado',binario)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
```
<p align="center"> <img src=./imagenes/dilatacion.png> </p>

____
## Creación de la imagen digital

Se crea una imagen digital exactamente igual a la diana original para poner la puntiación donde corresponde, las casillaes en blanco y negro correponden al valor x1, la primera circunferencia corresponde al valor x2, la segunda circunferencia corresponde al valor de x3, la circunferencia verde corresponde a 60 y la circuenferencia más pequeña corresponde a 100, como se muestra en la siguiente figura.

<p align="center"> <img src=./imagenes/diana_puntuacion.png> </p>

Como cada segmento de la diana simboliza un valor de puntaje, entonces se crea otra imagen, pero con los valores de puntaje es decir, se toma la imagen original y para este caso, se tomo la matriz roja como referencia, las otras matrices son nulas, entonces la imagen queda de la siguiente manera. 

<p align="center"> <img src=./imagenes/referencia.png> </p>

Y así con todos los valores respectivamente, y de esta manera la matriz roja representa el puntaje de esa casilla.

_____
## Puntuación 
