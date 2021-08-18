import cv2
import numpy as np

cap = cv2.VideoCapture(0) # Video

while(1):

    # Take each frame
    _, frame = cap.read() # video

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([150,20,255])
    upper_blue = np.array([180,20,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    byn = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,normal = cv2.threshold(byn,60,255,cv2.THRESH_BINARY_INV)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask= mask)
    
    kernel = np.ones((15,15),np.uint8)
    dilat = cv2.dilate(mask,kernel,iterations = 1)
    
    cv2.imshow('Normal',frame)
    cv2.imshow('Dilatación',dilat)
    # cv2.imshow('BInarizada',normal)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()




# import cv2
# import numpy as np

# img = cv2.imread('/home/angie/Documents/git/python_dsp/diana_opencv/diana1.jpeg')

# # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convierte a grises
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # cv2.imshow('hsv',hsv)


# # frame_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
# # frame_cr = cv2.extractChannel(frame_ycrcb, 0) ## 0- red, 1-green, 2-blue

# lower_blue = np.array([90,127,127]) 
# upper_blue = np.array([180,255,255])

# mask = cv2.inRange(hsv, lower_blue, upper_blue)

# # frame_cr = cv2.resize(frame_cr, (500,500) , interpolation =cv2.INTER_AREA)
# # cv2.imshow('titulo de la ventanda',frame_cr)

# res = cv2.bitwise_and(img, img, mask= mask)
# #cv2.imshow('b',mask)

# # hsv = cv2.cvtColor(frame_cr, cv2.COLOR_ycr_cb2HSV)

# # lower_blue = np.array([168,50,50]) 
# # upper_blue = np.array([180,255,255])

# # mask = cv2.inRange(frame_cr, lower_blue, upper_blue)


# cv2.imshow('Diana',res)
# cv2.imshow('Dia',mask)

# while (True):
    
#     k = cv2.waitKey(1) & 0xFF

#     # Metodo de salida

#     if k==ord('e'):
#         cv2.destroyAllWindows()
#     elif k==ord('s'):
#         cv2.imwrite("hola.png",img) ## se guarda la imagen
#         # cv2.destroyAllWindows()