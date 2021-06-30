import cv2
import numpy as np
from matplotlib import pyplot as plt

fondo = cv2.imread("fondo.jpg")
nueva = cv2.imread("nueva.jpg")

cv2.imshow("fondo",fondo)
cv2.imshow("nueva",nueva)

fondo = cv2.cvtColor(fondo,cv2.COLOR_BGR2GRAY)#convierte a grises
nueva = cv2.cvtColor(nueva,cv2.COLOR_BGR2GRAY)#convierte a grises
fondo = fondo.astype(np.int)
nueva = nueva.astype(np.int)
calculando = abs(nueva - fondo)
calculando = calculando.astype(np.uint8)


cv2.imshow("resta",calculando)

while (True):
    
    k = cv2.waitKey(1) & 0xFF