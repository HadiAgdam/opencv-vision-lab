# we decet and save hand gestures
# TODO reaad commands
# TODO get gesture
# TODO save as json file



import cv2
import mediapipe as mp
from models import Gesture, Command
from data import save
from time import time

print("Welcome to HandMotionOps.")

command = Command(input("enter commnad :"))

print("Show gesture to camera with your right hand, hold it for 3 seconds to save ...")

vid = cv2.VideoCapture(0)

hands = mp.solutions.hands.Hands()
mpDraw = mp.solutions.drawing_utils

duration = 3000


def end(g: Gesture):
    save(g, command)
    print("saved successfully")
    cv2.destroyAllWindows()
    exit()


if __name__ == "__main__":
    start_time = None
    g = None

    while True:
        success, img = vid.read()
        h, w, c = img.shape
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                if results.multi_handedness[idx].classification[0].index == 0:
                    ge = Gesture(hand_landmarks)
                    if ge != g:
                        start_time = time()
                        g = ge
                    if not start_time:
                        start_time = time()
                        g = ge
                    mpDraw.draw_landmarks(img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            if start_time and len(results.multi_hand_landmarks) == 1 and results.multi_handedness[idx].classification[0].index == 0:
                start_time = time()
                g = None
        else:
            start_time = None


        cv2.imshow("your video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
