import cv2 as cv
import sys

img=cv.imread('/home/angie/Documents/git/python_dsp/imagen.png',0)
cv.imshow('primer ejemplo',img)


while (True):
    
    k = cv.waitKey(1) & 0xFF

    if k==ord('e'):
        cv2.destroyAllWindows()
    elif k==ord('s'):
        cv2.imwrite("hola.png",img)
        cv2.destroyAllWindows()

# while True:
#     try:
#         k = cv.waitKey(1) & 0xFF

#     except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
#             print("Keyboard interrupt")

#     finally:
#         print("clean up")
    