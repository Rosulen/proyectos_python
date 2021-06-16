import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([90,127,127]) 
    upper_blue = np.array([120,255,255])

    # 00 - 30, amarillo
    # 30 - 60, verde
    # 90 - 120, azul
    #

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    kernel = np.ones((6,6),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations = 1)
    dilat=cv2.dilate(mask,kernel,iterations = 1)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    cv2.imshow('erode',erosion)
    cv2.imshow('dilate',dilat)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()