import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

cv2.namedWindow('Valores')

cv2.createTrackbar('Tao','Valores',0,255,nothing)
cv2.createTrackbar('Alpha','Valores',0,1000,nothing)

cap1=cv2.VideoCapture(1)
tao=45
alpha=0.05

kernel= np.ones((2,2),np.uint8)
kernel2= np.ones((2,2),np.uint8)

rec1, frame1=cap1.read()
frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
fondo = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

while(True):
    rec1,frame1=cap1.read()

    frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
    nueva = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

    tao = cv2.getTrackbarPos('Tao','Valores')
    alpha = cv2.getTrackbarPos('Alpha','Valores')

    fondo = ((alpha/1000)*nueva + (1 - (alpha/1000))*fondo)
    
    resta = abs(fondo*(-1) - nueva*(-1))
    resta = np.uint8(resta)
    
    ret,thresh1=cv2.threshold(resta,tao,255,cv2.THRESH_BINARY)
    resta_b = cv2.morphologyEx(thresh1,cv2.MORPH_OPEN,kernel)
    
    cv2.imshow('Valores',frame1)
    cv2.imshow('binarización',resta_b)
    
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap1.release()
cv2.destroyAllWindows()


# import cv2
# import numpy as np
# import time

# def nothing(x):
#     pass

# cv2.namedWindow('Valores')

# cv2.createTrackbar('Thao','Valores',0,255,nothing)
# cv2.createTrackbar('Alpha','Valores',0,10,nothing)

# cap1 = cv2.VideoCapture(1) # Iniciar video
# primeros_valores = 0

# while (True):

#     rec1, frame1 = cap1.read()
#     frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
#     cv2.imshow('video',frame1)

#     thao = cv2.getTrackbarPos('Thao','Valores')
#     alpha = cv2.getTrackbarPos('Alpha','Valores')

#     fondo = frame1

#     rec1, frame1 = cap1.read()
#     frame1 = cv2.resize(frame1, (426,240) , interpolation =cv2.INTER_AREA)
    
#     # cv2.imwrite('nueva.jpg',frame1)
#     nueva = frame1
#     nueva = cv2.cvtColor(nueva,cv2.COLOR_BGR2GRAY)
#     fondo = cv2.cvtColor(fondo,cv2.COLOR_BGR2GRAY)
#     fondo = fondo.astype(np.int)
#     nueva = nueva.astype(np.int)

#     fondo = (nueva*(alpha/10)) + (1-(alpha/10))*fondo
#     fondo = fondo.astype(np.uint8)
#     cv2.imshow('fondo',fondo)

#     fondo = fondo.astype(np.int)
#     nueva = nueva.astype(np.int)
#     resta = abs(fondo-nueva)
    

#     fondo[resta > thao] = 1
#     fondo[resta < thao] = 0

#     fondo = fondo.astype(np.uint8)
#     nueva = nueva.astype(np.uint8)
#     cv2.imshow('estesies',fondo)

#     resta = resta.astype(np.uint8)
#     cv2.imshow('resta2',resta)

#     ret,thresh2 = cv2.threshold(resta,80,255,cv2.THRESH_BINARY)
#     cv2.imshow('fondo_2',thresh2)

#     kernel = np.ones((thao,thao),np.uint8)
#     erosion = cv2.erode(thresh2,kernel,iterations = 1)
    
#     thresh2[thresh2 < thao] = 1
#     thresh2[thresh2 > thao] = 0

#     if cv2.waitKey(1)  & 0xff==ord('q'):
#         break

# #cap.release()
# cap1.release()
# cv2.destroyAllWindows()