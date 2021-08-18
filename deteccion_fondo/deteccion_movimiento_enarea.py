import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Valores')

# Slider para variar el Tao y Alpha
cv2.createTrackbar('Tao','Valores',0,255,nothing)
cv2.createTrackbar('Alpha','Valores',0,1000,nothing)
cv2.createTrackbar('Area','Valores',1,500,nothing)

cambio_color = 0

# Inicialización de variables y video
cap1=cv2.VideoCapture(0)
rec1, frame1=cap1.read()
frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
rectangulo = np.array([0,0,0,0])
contador = 0
pos = 0

# Mascara para eliminación de pixeles
kernel= np.ones((1,1),np.uint8)
kernel2= np.ones((1,1),np.uint8)

# Captura la primera imagen que será el fondo
rec1, frame1=cap1.read()
frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
fondo = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

contador2 = 0

v = np.array([0,0,0,0])

# función para almacenar en rectangulo las coordenadas
def obtener_valores(event, x, y, etiquetas, parametros):
    global pos, rectangulo, contador, contador2
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        
        while pos <= 1:
            if pos == 0:
                rectangulo[contador2] = x
                
            else:
                rectangulo[contador2 + 1] = y

            contador = contador + 1
            pos = pos + 1
        
        contador2 = contador2 + 2
        if contador2 >= 3:
            contador2 = 0 

        pos = 0
        if contador%4 == 0:
            print(contador)

# Creación de ventana y llamado a la funcion
cv2.namedWindow(winname = 'Valores')
cv2.setMouseCallback('Valores',obtener_valores)

while(1):
    # Captura la nueva imagen que se comparará con el fondo
    rec1, frame1=cap1.read()
    frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
    nueva = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

    # Obtener valorse de Tao y Alpha
    tao = cv2.getTrackbarPos('Tao','Valores')
    alpha = cv2.getTrackbarPos('Alpha','Valores')
    area = cv2.getTrackbarPos('Area','Valores')

    coordenada = 0
    capacidad = 1

    # Algoritmo de la mediana
    fondo = ((alpha/1000)*nueva + (1 - (alpha/1000))*fondo)

    # Se resta el fondo con la nueva imagen
    resta = abs(fondo*(-1) - nueva*(-1))
    resta = np.uint8(resta)

    # Se binariza el resultado de la resta
    ret,thresh1 = cv2.threshold(resta,tao,255,cv2.THRESH_BINARY)
    resta_b = cv2.morphologyEx(thresh1,cv2.MORPH_OPEN,kernel)

    prueba = list(resta_b)
    prueba = np.array(prueba)

    # saber en que posición está el nuevo objeto
    contornos, hierarchy = cv2.findContours(resta_b,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if cambio_color == 0 or contornos == []:
        green = 255
        red = 0
    else:
        green = 0
        red = 255
    
    rectangulo = rectangulo.astype(np.int64)
    
    coordenada = 0
    # If para hacer el rectangulo en la pantalla
    if contador%4 == 0: # Cada que conatdor sea modulo de 4 puede graficar un rectangulo
        while capacidad <= contador/4:
            cv2.rectangle(frame1,(rectangulo[coordenada],rectangulo[pos+1]),(rectangulo[coordenada+2],rectangulo[coordenada+3]),(0,green,red),3)
            capacidad = capacidad + 1

    capacidad = 1
    coordenada = 0
    
    # Saber la posición de los objetos que se mueven en el fondo
    if contador%4 == 0 and contador != 0:
        

        prueba[:rectangulo[coordenada + 1]] = 0
        prueba[rectangulo[coordenada + 3]:] = 0
        prueba = np.transpose(prueba)
        prueba[:rectangulo[coordenada]] = 0
        prueba[rectangulo[coordenada + 2]:] = 0
        prueba = np.transpose(prueba)
        cv2.imshow('prueba', prueba)

        if np.amax(prueba) == 255:
            cambio_color = 1
        else:
            cambio_color = 0


        for c in contornos:
        
            if cv2.contourArea(c) > area:
                # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
                (x, y, w, h) = cv2.boundingRect(c)
                # Dibujamos el rectángulo del bounds
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imshow("Valores", frame1)

    cv2.imshow('Valores',frame1) # imprimir imagen
    cv2.imshow('binarización',resta_b)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
