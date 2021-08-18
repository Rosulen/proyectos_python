# import tkinter as tk
# from io import BytesIO
# from turtle import TurtleScreen, RawTurtle
# from PIL import Image, ImageTk
# import numpy as np

# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# from matplotlib import pyplot as plt
# import cv2

# # root = tk.Tk()

# # # Plot graph

# # # score = ['5', '20', '5', '4', '3', '20', '2', '10']
# # size1 = [20, 20, 20, 20, 20, 20, 20, 20]
# # colors = ['#000000','#ffffff','#000000','#ffffff','#000000','#ffffff','#000000','#ffffff']
# # c_circles = ['#ff0000','#008000','#ff0000', '#008000','#ff0000', '#008000','#ff0000','#008000']

# # fig = plt.figure(figsize =(10, 7))
# # score = ['5', '20', '5', '4', '3', '20', '2', '10'] 
# # circle1 = [20, 20, 20, 20, 20, 20, 20, 20]
# # plt.pie(size1, colors = c_circles, radius = 1.55)
# # plt.pie(size1, colors = colors, radius = 1.4)
# # plt.pie(size1, colors = c_circles, radius = 0.85)
# # plt.pie(size1, colors = colors, radius = 0.7)
# # plt.pie([20, 20], colors = ['#008000','#008000'], radius = 0.2)
# # plt.pie([20, 20], colors = ['#ff0000','#ff0000'], radius = 0.08)
# # plt.pie([20, 20], colors = ['#ff0000','#ff0000'], radius = 1.55)
# # plt.savefig('/home/angie/Documents/git/python_dsp/diana_opencv/punto_rojo.png')
# # plt.show()

# img = cv2.imread('/home/angie/Documents/git/python_dsp/diana_opencv/punto_rojo.png',0)

# ret,thresh1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)

# contornos, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# for c in contornos:

#     cv2.contourArea(c)
#     (x,y),radius = cv2.minEnclosingCircle(c)
#     center = (int(x),int(y))
#     radius = int(radius)
#     print(radius)
#     cv2.circle(img,center, 335 ,(0,255,0),2)
#     cv2.circle(img,center, 5 ,(0,255,0),-1)

# cv2.imshow('x',img)
# cv2.imshow('s',thresh1)

# while (True):

#     k = cv2.waitKey(1) & 0xFF

#     # Metodo de salida

#     if k==ord('e'):
#         cv2.destroyAllWindows()
#     elif k==ord('s'):
#         cv2.imwrite("hola.png",img) ## se guarda la imagen
#         cv2.destroyAllWindows()












import turtle
tr = turtle.Turtle()
wn = turtle.Screen()
wn.setup(width=900, height=800)
wn.bgpic("/home/angie/Documents/git/python_dsp/diana_opencv/diana.png")
wn.mainloop()

# # Creación de elementos gráficos (circulos de la diana)
c3 = turtle.Turtle() # c3 - circulo 3
c3.speed(0)
c3.shape("circle")
c3.color("blue")
c3.goto(0,-40)
c3.shapesize(230)











# # Make memory image of graph
# invisible_figure_canvas = FigureCanvasTkAgg(fig, root)
# buffer = BytesIO()
# Figure.savefig(buffer, format="png")
# buffer.seek(0)

# # Open memory as tkinter image
# image = Image.open(buffer)
# photoImage = ImageTk.PhotoImage(image)
# buffer.close()

# # Now do our turtle drawing embedded in tkinter
# canvas = tk.Canvas(root, width=500, height=500)
# canvas.pack()

# screen = TurtleScreen(canvas)
# screen._setbgpic(screen._bgpic, photoImage)  # bypass restrictions (protected access)

# turtle = RawTurtle(screen, shape='turtle')
# turtle.shapesize(0.5)


# def hilbertCurve(n, angle):
#     if n <= 0:
#         return

#     turtle.left(angle)
#     hilbertCurve(n - 1, -angle)
#     turtle.forward(10)
#     turtle.right(angle)
#     hilbertCurve(n - 1, angle)
#     turtle.forward(10)
#     hilbertCurve(n - 1, angle)
#     turtle.right(angle)
#     turtle.forward(10)
#     hilbertCurve(n - 1, -angle)
#     turtle.left(angle)

# hilbertCurve(4, 90)

# screen.mainloop()








# import turtle

# # Creación y configuración de la ventana principal
# wn = turtle.Screen()
# wn.title("Diana")
# wn.bgcolor("pink")
# wn.setup(width=600, height=600)
# wn.tracer(0)

# # Creación de elementos gráficos (circulos de la diana)
# c3 = turtle.Turtle() # c3 - circulo 3
# c3.speed(0)
# c3.shape("circle")
# c3.color("green")
# c3.goto(0,-40)
# c3.shapesize(24)

# c2 = turtle.Turtle() # c2 - circulo 2
# c2.speed(0)
# c2.shape("circle")
# c2.color("yellow")
# c2.goto(0,-40)
# c2.shapesize(16)

# c1 = turtle.Turtle() # c1 - circulo 1
# c1.speed(0)
# c1.shape("circle")
# c1.color("blue")
# c1.goto(0,-40)
# c1.shapesize(8)

# while True:
#     wn.update()


# Import libraries








# # create data
# size_of_groups = [20, 20, 20, 20, 20, 20, 20, 20]

# # Create a pieplot
# plt.pie(size_of_groups)

# # add a circle at the center to transform it in a donut chart
# my_circle=plt.Circle( (0,0), 0.7, color='white')
# p=plt.gcf()
# p.gca().add_artist(my_circle)

# plt.show()