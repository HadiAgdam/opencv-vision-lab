# we decet and save hand gestures
# TODO reaad commands
# TODO get gesture
# TODO save as json file



import cv2
import mediapipe as mp
from models import Gesture, Command
from data import save
from time import time
from math import sqrt

print("Welcome to HandMotionOps.")

# command = Command(input("enter commnad :"))

print("Show gesture to camera with your right hand, hold it for 3 seconds to save ...")

vid = cv2.VideoCapture(0)

hands = mp.solutions.hands.Hands()
mpDraw = mp.solutions.drawing_utils

duration = 3

gesture: Gesture = None
start_time: float = None

def end():
    # save(g, command)
    print("saved successfully")
    cv2.destroyAllWindows()
    exit()


if __name__ == "__main__":

    while True:
        success, img = vid.read()
        h, w, c = img.shape
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                if results.multi_handedness[idx].classification[0].index == 0:
                    g = Gesture(hand_landmarks)
                    mpDraw.draw_landmarks(img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
                    if not gesture or g.fingers != gesture.fingers:
                        start_time = time()
                        gesture = g
                    cx5, cy5 = int(hand_landmarks.landmark[5].x * w), int(hand_landmarks.landmark[5].y * h)
                    cx17, cy17 = int(hand_landmarks.landmark[17].x * w), int(hand_landmarks.landmark[17].y * h)
                    cx0, cy0 = int(hand_landmarks.landmark[0].x * w), int(hand_landmarks.landmark[0].y * h)

                    cx8, cy8 = int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h)

                    # cv2.circle(img, (int((cx5 + cx17 + cx0) / 3), int((cy5 + cy17 + cy0) / 3)), 200, (255, 255, 255), 10)
                    # cv2.circle(img, (int((cx5 + cx0) / 2), int((cy5 + cy0) / 2)), 200, (255, 255, 255), 10)
                    cv2.circle(img, (cx5, cy5), 200, (255, 255, 255), 20)
                    cv2.ellipse(img, (cx5, cy5), (200, 200), 0,-90, -90 + (time() - start_time) * 120, (0, 80, 0), 20)
        else:
            start_time = None
            gesture = None
        
        if start_time and start_time + duration <= time():
            end()

        cv2.imshow("your video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
