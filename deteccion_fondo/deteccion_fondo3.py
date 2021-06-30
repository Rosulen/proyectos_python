import cv2
import numpy as np
from matplotlib import pyplot as plt

cap1=cv2.VideoCapture(1)
band=0
alfa=0.09

kernel= np.ones((6,6),np.uint8)
kernel2= np.ones((6,6),np.uint8)

rec1, frame1=cap1.read()
frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
fondo = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
fila = len(fondo)
columna = len(fondo[0])

while(True):

    rec1,frame1=cap1.read()
    frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
    nueva = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    fondo = fondo.astype(np.float64)
    nueva = nueva.astype(np.float64)
    for a in range (0,fila):
        for b in range (0,columna):
            if(nueva[a][b] > fondo[a][b]):
                fondo[a][b] = fondo[a][b]+alfa
            elif(nueva[a][b] < fondo[a][b]):
                fondo[a][b] = fondo[a][b]-alfa
    fondo = (alfa*nueva+(1-alfa)*fondo)
    
    out=abs(fondo*(-1)-nueva*(-1))
    out2=np.uint8(out)
    
    ret,thresh1 = cv2.threshold(out2,45,255,cv2.THRESH_BINARY)
    punto = cv2.morphologyEx(thresh1,cv2.MORPH_OPEN,kernel)
    
    cv2.imshow('VIDEO',frame1)
    cv2.imshow('GRISES',punto)
    
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cap1.release()
cv2.destroyAllWindows()

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# cap1=cv2.VideoCapture(0)

# def nothing(x):
#     pass

# cv2.namedWindow('Valores')

# cv2.createTrackbar('Tao','Valores',0,255,nothing)
# cv2.createTrackbar('Beta','Valores',0,100,nothing)

# kernel= np.ones((2,2),np.uint8)
# kernel2= np.ones((2,2),np.uint8)

# rec1, frame1=cap1.read()
# frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
# fondo = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

# j_f = len(fondo)
# i_c = len(fondo[0])

# while(True):

#     rec1,frame1=cap1.read()
#     frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
#     imagen=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

#     tao = cv2.getTrackbarPos('Tao','Valores')
#     beta = cv2.getTrackbarPos('Alpha','Valores')

#     for a in range (0,j_f):
#         for b in range (0,i_c):
#             if(imagen[a][b] > fondo[a][b]):
#                 fondo[a][b] = fondo[a][b] + beta
#             elif(imagen[a][b] < fondo[a][b]):
#                 fondo[a][b] = fondo[a][b] - beta
#     fondo = (beta/100*imagen + (1 - beta/100)*fondo)
    
#     resta = abs(fondo*(-1) - imagen*(-1))
#     resta = np.uint8(resta)
    
#     ret,thresh1=cv2.threshold(resta,tao,255,cv2.THRESH_BINARY)
#     punto = cv2.morphologyEx(thresh1,cv2.MORPH_OPEN,kernel)
    
#     cv2.imshow('Frame',frame1)
#     cv2.imshow('Valores',punto)
    
#     k = cv2.waitKey(30) & 0xFF
#     if k == 27:
#         break

# cap1.release()
# cv2.destroyAllWindows()


























# import cv2
# import numpy as np

# cap = cv2.VideoCapture(1)

# beta = 10
# thao = 125

# while True:
#     rect, frame = cap.read()
#     x = cv2.resize(frame, (426,240) , interpolation =cv2.INTER_AREA)
#     cv2.imshow('x', x)

#     fondo = x

#     rect, frame = cap.read()
#     x = cv2.resize(frame, (426,240) , interpolation =cv2.INTER_AREA)
#     nueva = x

#     fondo = cv2.cvtColor(fondo,cv2.COLOR_BGR2GRAY)
#     nueva = cv2.cvtColor(nueva,cv2.COLOR_BGR2GRAY)
#     fondo = fondo.astype(np.int)
#     nueva = nueva.astype(np.int)

#     salida = 0

#     while salida < 240:
#         f1 = fondo[salida]
#         n1 = nueva[salida]
#         contador = 0
#         for i in n1:
#             if i > f1[contador]:
#                 f1[contador] = f1[contador] + beta
#             if i < f1[contador]:
#                 f1[contador] = f1[contador] - beta
#             contador = contador + 1
#         salida = salida + 1

#     salida = 0
#     contador = 0

#     fondo_binarizacion = list(fondo)
#     fondo_binarizacion = np.array(fondo_binarizacion)
#     fondo_binarizacion = fondo_binarizacion.astype(np.uint8)
#     rect,fondo_b = cv2.threshold(fondo_binarizacion,80,255,cv2.THRESH_BINARY_INV)
#     cv2.imshow('fondo_binarizado',fondo_b)

#     fondo_b = fondo_b.astype(np.int)
    
#     resta = abs(nueva-fondo)
#     fondo_b[resta <= thao] = 1
#     fondo_b[resta > thao] = 0
    
#     nueva = nueva.astype(np.uint8)
#     fondo = fondo.astype(np.uint8)
#     fondo_b = fondo_b.astype(np.uint8)

#     cv2.imshow('fondo_completo',fondo_b)

#     # rect,nueva_b = cv2.threshold(nueva,thao,255,cv2.THRESH_BINARY)
#     # cv2.imshow('nueva',nueva)
    
#     rect,fondo_b = cv2.threshold(fondo_b,thao,255,cv2.THRESH_BINARY)
#     cv2.imshow('fondo2',fondo_b)
    
#     if cv2.waitKey(1)  & 0xff==ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()