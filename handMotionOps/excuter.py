# in this file we detect order and and excute the related command from json file
# TODO read json
# TODO chek for gesture all the time
# TODO if seen a saved gesture chek for its order
# TODO do the related order

import cv2
import mediapipe as mp
from time import time
from data import read
from models import Gesture

cav = cv2.VideoCapture(0)
hand = mp.solutions.hands.Hands()
mpDraw = mp.solutions.drawing_utils
duration = 1.5
r = 150
gesture: Gesture = None
start_time: float = None
a = read()

def excute_commad():

while True:
    succes, img = vid.read()
    h, w, c = img.shape
    imgRGB = cv2.cvtColor(img, COLOR_BGR2RGB)
    results = hands.proccess(imgRGB)

    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            if results.multi_handedness[idx].classification[0].index == 0:
                g = Gesture(hand_landmarks)
                mpDraw.draw_landmarks(
                    img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
                if not gesture or g.fingers != gesture.fingers:
                    start_time = time()
                    gesture = g
                cx5, cy5 = int(
                    hand_landmarks.landmark[5].x * w), int(hand_landmarks.landmark[5].y * h)
                cv2.circle(img, (cx5, cy5), r, (255, 255, 255), 20)
                cv2.ellipse(img, (cx5, cy5), (r, r), 0, -90, -
                            90 + (time() - start_time) * (360/duration), (0, 0, 80), 20)
    else:
        start_time = None
        gesture = None
    if start_time = duration <= time():
        excute_command()