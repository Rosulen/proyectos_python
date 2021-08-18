import cv2
import numpy as np
import matplotlib.pylab as plt
import statistics
import time
import turtle

# Cargar video

wn = turtle.Screen() # ventana
wn.title("Score")
wn.bgcolor("pink")
wn.setup(width = 400, height = 100)
wn.tracer(0)
texto = turtle.Turtle()
texto.speed(0)
texto.color("blue")
texto.penup()
texto.hideturtle()
texto.goto(0,0)
texto.write("Score: 0",align = "center", font = ("Curier", 24, "normal"))



cv2.namedWindow('Normal')
cap = cv2.VideoCapture(0)

referencia = cv2.imread('/home/angie/Documents/git/python_dsp/diana_opencv/referencia_diana.png') ## El cero es para poner la imagen en blanco y negro
referencia = cv2.resize(referencia, (640, 480))
diana = cv2.imread('/home/angie/Documents/git/python_dsp/diana_opencv/diana.png')
diana = cv2.resize(diana, (640, 480))

cv2.imshow('Diana',diana)
#referencia = np.adiana = cv2.resize(diana, (640, 480))rray(referencia)
red = referencia[:,:,2]
contador = 0
score = 0

while(1):

    _, frame = cap.read() # Take each frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)# Convert BGR to HSV
    lower_blue = np.array([150,20,255]) # Definir el rango de color, en este caso solamente los rojos más brillantes
    upper_blue = np.array([180,20,255]) # es decir, el rojo de la luz laser
    mask = cv2.inRange(hsv, lower_blue, upper_blue) # mascara para binarizar en el rango

    binario = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # pasar a blanco y negro la imagen original
    ret,binario = cv2.threshold(binario,80,255,cv2.THRESH_BINARY_INV) # Bnarizar la imagen original

    kernel = np.ones((10,10),np.uint8)
    dilat = cv2.dilate(mask,kernel,iterations = 1)

    # contornos, hierarchy = cv2.findContours(binario,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    # for c in contornos:

    #     if cv2.contourArea(c) > 70000:
    #         # Dibujar circulo
    #         (x,y),radius = cv2.minEnclosingCircle(c)
    #         center = (int(x),int(y))
    #         radius = int(radius)
    #         cv2.circle(frame,center,radius,(0,255,0),2)
    #         cv2.circle(frame,center, 5 ,(0,255,0),-1)
    #         # print(f'El radio es = {radius}')
    #         # Imprimir la imagen con los curculos y demás
    #         cv2.imshow("Normal", frame)
    #         # print(cv2.contourArea(c))

    contornos, hierarchy = cv2.findContours(dilat,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(contornos) > 0:
        print(len(contornos))
    if len(contornos) == 1:

        for c in contornos:

            cv2.contourArea(c)
            (x,y),radius = cv2.minEnclosingCircle(c)
            center = (int(x),int(y))
            radius = int(radius)
            x2 = int(x) #(x*700)/480
            y2 = int(y) #(y*1000)/640
            center2 = (int(x2),int(y2))
            cv2.circle(diana,center2, 5 ,(255,0,0),-1)
            print(f'{int(x2),int(y2)}')
            score = score + red[int(y2),int(x2)]

            texto.clear()
            texto.write("Score: {}".format(score) ,align = "center", font = ("Curier", 24, "normal"))

    
    elif len(contornos) > 1 and len(contornos) < 4:
        xp = []
        yp = []
        for c in contornos:
            
            cv2.contourArea(c)
            (x,y),radius = cv2.minEnclosingCircle(c)
            x2 = int(x) # (x*700)/480
            y2 = int(y) # (y*1000)/640
            center = (int(x2),int(y2))
            print(f' Para promediar: {center}')
            xp.append(center[0])
            yp.append(center[1]) 
            center2 = (int(statistics.mean(xp)),int(statistics.mean(yp)))
        
        cv2.circle(diana,center2, 5 ,(255,0,0),-1)
        print(red.size)
        print(center)

        score = score + red[int(statistics.mean(yp)),int(statistics.mean(xp))]
        texto.clear()
        texto.write("Score: {}".format(score) ,align = "center", font = ("Curier", 24, "normal"))

    elif len(contornos) >= 4:

        center = (int(480/2),int(640/2))
        cv2.circle(diana,center, 5 ,(255,0,0),-1)
        score = score + red[int(statistics.mean(yp)),int(statistics.mean(xp))]
        texto.clear()
        texto.write("Score: {}".format(score) ,align = "center", font = ("Curier", 24, "normal"))



    time.sleep(0.1)

    #         yp.append(center[0])
    #         xp.append(center[1])
        
    #     # print("amarillo")
    #     # center2 = (int(statistics.mean(xp)),int(statistics.mean(yp)))
    #     # cv2.circle(diana,center2, 5 ,(0,255,255),-1)
        
    #     print(center2)

    #     print("fin")



    cv2.imshow('Normal',frame)
    cv2.imshow('Dilatación',dilat)
    cv2.imshow('Binarizado',binario)
    cv2.imshow('Diana',diana)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

