import cv2
import numpy as np

# Inicialización de variables y video
cap1=cv2.VideoCapture(1)
rec1, img=cap1.read()
img = cv2.resize(img, (426,240) , interpolation =cv2.INTER_AREA)
rectangulo = np.array([])
contador = 0
pos = 0

# función para almacenar en rectangulo las coordenadas
def obtener_valores(event, x, y, etiquetas, parametros):
    global pos, rectangulo, contador
    if event == cv2.EVENT_LBUTTONDBLCLK:
        while pos <= 1:
            if pos == 0:
                rectangulo = np.append(rectangulo, x)
            else:
                rectangulo = np.append(rectangulo, y)
            contador = contador + 1
            pos = pos + 1
        print(rectangulo)
        pos = 0
        if contador%4 == 0:
            print(contador)

# Creación de ventana y llamado a la duncion
cv2.namedWindow(winname = 'imagen')
cv2.setMouseCallback('imagen',obtener_valores)

while(1):
    rec1, img=cap1.read()
    img = cv2.resize(img, (426,240) , interpolation =cv2.INTER_AREA)
    coordenada = 0
    g = 1
    
    rectangulo = rectangulo.astype(np.int64)
    
    if contador%4 == 0: # Cada que conatdor sea modulo de 4 puede graficar un rectangulo
        while g <= contador/4:
            cv2.rectangle(img,(rectangulo[coordenada],rectangulo[pos+1]),(rectangulo[coordenada+2],rectangulo[coordenada+3]),(255,0,0),3)
            coordenada = coordenada + 4
            g = g + 1

    cv2.imshow('imagen',img) # imprimir imagen
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Blanco y negro',gray)

    ret,binarizado = cv2.threshold(gray,160,255,cv2.THRESH_BINARY)
    cv2.imshow('Binarizacion',binarizado)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
