import cv2
import numpy as np

def boundary_of_image(img, classifier, scaleFactor, minNeighbours, color, text):
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    features = classifier.detectMultiScale(grayscale_img, scaleFactor, minNeighbours)
    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2, cv2.LINE_AA)
        coords = [x, y, w, h]
        print(coords)
        return coords, img

faceCasade = cv2.CascadeClassifier("face_detection.xml")
def detect(img, faceCasade):
    color = {"blue":(255, 0, 0), "red":(0, 0, 255), "green":(0,255,0)}
    coords = boundary_of_image(img, faceCasade, 1.1, 11, color['green'], "Face")
    return img


cap = cv2.VideoCapture(0)

while True:
    _, imge = cap.read()
    imge = detect(imge, faceCasade)
    cv2.imshow("Webcam", imge)
    print()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()