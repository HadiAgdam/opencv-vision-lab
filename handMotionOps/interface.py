import cv2
import mediapipe as mp

# initialazation
cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    success, img = cap.read()
    h, w, c = img.shape
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    cv2.imshow('ur video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
