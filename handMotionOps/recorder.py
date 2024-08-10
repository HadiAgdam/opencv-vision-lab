# we decet and save hand gestures
# TODO reaad commands
# TODO get gesture
# TODO save as json file

import cv2
import mediapipe as mp
from models import Gesture, Command
from data import save


command = input("enter command")
print('show the gesture you want to save to this command')


vid = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    success, img = vid.read()
    h, w, c = img.shape
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        G = Gesture(hand)
        c = Command(command)
        save(G, c)
        print("save succesful")
        cv2.destroyAllWindows()
        exit()

    cv2.imshow("your video", img)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break
