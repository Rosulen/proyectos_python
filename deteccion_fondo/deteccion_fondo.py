import cv2
import numpy as np
from matplotlib import pyplot as plt

### It Imagen actual, bt-1 Imagen fondo, alpha que tan rapido un objeto se convierte en fondo
# 0-1, Thao, objetos mayores a x pixeles quitarlos

## Bt fondo actual, etiqueta binarización (?)

cap = cv2.VideoCapture(0)
plt.imshow(cap)
plt.show()


