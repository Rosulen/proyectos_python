import cv2

haar_file = '/home/angie/Documents/git/python_dsp/reconocimiento_facial/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(1)

while True:
    (_, img) = webcam.read()
    # img = cv2.resize(img, (426,240) , interpolation =cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    if len(faces) > 0:
        print("laser_prendido")
    else: print("")

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv2.imshow('face', img)

    key = cv2.waitKey(10)
    if key == 27:
        break