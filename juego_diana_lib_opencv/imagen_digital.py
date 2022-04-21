import tkinter as tk
from io import BytesIO
from turtle import TurtleScreen, RawTurtle
from PIL import Image, ImageTk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

import cv2 as cv 
import sys
np.set_printoptions(threshold=sys.maxsize)

img = cv.imread('/home/angie/Documents/git/python_dsp/diana_opencv/diana.png') ## El cero es para poner la imagen en blanco y negro
matrices = np.array(img)
red = matrices[:,:,2]
print(red[350,700])
print(red.shape)
cv.imshow('s',img)

while (True):
    
    k = cv.waitKey(1) & 0xFF

    # Metodo de salida

    if k==ord('e'):
        cv2.destroyAllWindows()
    elif k==ord('s'):
        cv2.imwrite("hola.png",img) ## se guarda la imagen
        cv2.destroyAllWindows()


# root = tk.Tk()

# # Plot graph

# # score = ['5', '20', '5', '4', '3', '20', '2', '10']
# size1 = [20, 20, 20, 20, 20, 20, 20, 20]
# colors = ['#000000','#ffffff','#000000','#ffffff','#000000','#ffffff','#000000','#ffffff']
# c_circles = ['#ff0000','#008000','#ff0000', '#008000','#ff0000', '#008000','#ff0000','#008000']

# fig = plt.figure(figsize =(10, 7))
# score = ['5', '20', '5', '4', '3', '20', '2', '10'] 
# circle1 = [20, 20, 20, 20, 20, 20, 20, 20]
# plt.pie(size1, colors = c_circles, radius = 1.55)
# plt.pie(size1, colors = colors, radius = 1.4)
# plt.pie(size1, colors = c_circles, radius = 0.85)
# plt.pie(size1, colors = colors, radius = 0.7)
# plt.pie([20, 20], colors = ['#008000','#008000'], radius = 0.2)
# plt.pie([20, 20], colors = ['#ff0000','#ff0000'], radius = 0.08)
# plt.savefig('/home/angie/Documents/git/python_dsp/diana_opencv/digital.png')
# plt.show()




