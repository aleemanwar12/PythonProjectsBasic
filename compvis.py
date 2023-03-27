import cv2
import serial
import time
arduino = serial.Serial('COM3', 9600)
cascade = cv2.CascadeClassifier('face_detection.xml')

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    face_detect = cascade.detectMultiScale(grayscale, 1.5, 5)
    for (x, y, w, h) in face_detect:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        centerX = int((x + w/2) * 180 / img.shape[1])
        centerY = int((y + h/2) * 180 / img.shape[0])
        print(centerX, centerY)
        arduino.write(f'{centerX}, {centerY}\n'.encode())
        cv2.imshow("Webcam", img)
        cv2.imshow("gray_webcam", grayscale)
        time.sleep(0.1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break