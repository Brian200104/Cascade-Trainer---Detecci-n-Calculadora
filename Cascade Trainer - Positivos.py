import cv2
import numpy as np
import imutils
import os

Datos = 'p'
if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)

url = "http://10.24.3.183:4747/video"
cap = cv2.VideoCapture(url)

x1, y1 = 190, 80
x2, y2 = 450, 398
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo recibir el video del celular")
        break

    imAux = frame.copy()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    objeto = imAux[y1:y2, x1:x2]

    k = cv2.waitKey(1)
    if k == ord('f'):
        filename = os.path.join(Datos, f'objeto_{count}.jpg')
        cv2.imwrite(filename, objeto)
        print('Imagen guardada:', filename)
        count += 1
    elif k == 27:
        break

    cv2.imshow('frame', frame)

cap.release()
cv2.destroyAllWindows()
