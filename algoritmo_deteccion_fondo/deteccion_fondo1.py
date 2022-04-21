import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

cv2.namedWindow('Valores')

cv2.createTrackbar('Thao','Valores',0,255,nothing)

cap1 = cv2.VideoCapture(1) # Iniciar video
captura_fondo = 1

while (True):

    rec1, frame1 = cap1.read()
    frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
    cv2.imshow('Valores',frame1)
    
    thao = cv2.getTrackbarPos('Thao','Valores')

    if captura_fondo == 1: # La primera imagen es la imagen de fondo
        cv2.imwrite('fondo.jpg',frame1)
        captura_fondo = 0
        thao = cv2.setTrackbarPos('Thao','Valores',80)
    
    cv2.imwrite('nueva.jpg',frame1) # se toma la nueva imagen y se guarda

    fondo = cv2.imread('fondo.jpg') # se leen las imagenes guardadas
    nueva = cv2.imread('nueva.jpg')
    
    fondo = cv2.cvtColor(fondo,cv2.COLOR_BGR2GRAY) #convierte a grises
    nueva = cv2.cvtColor(nueva,cv2.COLOR_BGR2GRAY) 
    fondo = fondo.astype(np.int) # se convierten a un formato donde se peudan operar las matrices
    nueva = nueva.astype(np.int)
    calculando = abs(fondo - nueva) # se restan las imagenes
    calculando = calculando.astype(np.uint8)

    ret,thresh2 = cv2.threshold(calculando,thao,255,cv2.THRESH_BINARY) # se binariza la imagen obtenida

    kernel = np.ones((20,20),np.uint8)
    erosion = cv2.erode(thresh2,kernel,iterations = 1)
    dilat=cv2.dilate(thresh2,kernel,iterations = 1)

    # contours, hierarchy = cv2.findContours(dilat, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    contornos, hierarchy = cv2.findContours(dilat,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow('binarizada',dilat)

    for c in contornos:
        
        if cv2.contourArea(c) > 500:
            # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
            (x, y, w, h) = cv2.boundingRect(c)
            # Dibujamos el rectángulo del bounds
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow("Valores", frame1)


    # if len(contours) != 0:
    #     for contour in contours:
    #         cv2.drawContours(frame1, contour, -1, (0, 255, 0), 3)
    #     cv2.imshow("Valores", frame1)

    else:
        cv2.imwrite('fondo.jpg',frame1)

    if cv2.waitKey(1)  & 0xff==ord('q'):
        break

cap1.release()
cv2.destroyAllWindows()