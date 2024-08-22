import cv2
import mediapipe as mp
from models import Gesture, Command, get_gesture_from_hand
from time import time

r = 150


def destroy_windows():
    cv2.destroyAllWindows()


class Interface:

    def __init__(self, event, duration=3):
        self.c = 0
        self.duration = duration
        self.start_time = None
        self.gesture = None
        self.event = event
        self.vid = cv2.VideoCapture(0)

        self.hands = mp.solutions.hands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

        self.gesture: Gesture
        self.start_time: float

    def init_camera_source(self):
        print("Welcome to HandMotionOps.")
        self.c = input("Please enter the source if vide file. If using camera put the camera index (default 0):")

        if self.c.isdigit():
            self.c = int(self.c)

    def loop(self):
        print("press q to exit")
        while True:
            success, img = self.vid.read()
            h, w, c = img.shape
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.hands.process(img_rgb)

            if results.multi_hand_landmarks:
                for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                    # TODO maybe remove this, both hands should be allowed
                    if results.multi_handedness[idx].classification[0].index == 0:
                        g = get_gesture_from_hand(hand_landmarks)
                        self.mpDraw.draw_landmarks(
                            img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
                        if not self.gesture or g.fingers != self.gesture.fingers:
                            start_time = time()
                            self.gesture = g
                        cx5, cy5 = int(
                            hand_landmarks.landmark[5].x * w), int(hand_landmarks.landmark[5].y * h)
                        cv2.circle(img, (cx5, cy5), r, (255, 255, 255), 20)
                        cv2.ellipse(img, (cx5, cy5), (r, r), 0, -90, -
                        90 + (time() - start_time) * (360 / self.duration), (0, 80, 0), 20)
                        print(start_time)
            else:
                self.start_time = None
                self.gesture = None

            if start_time and start_time + self.duration <= time():
                self.event(self.gesture)

            cv2.imshow("your video", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def start(self):
        # t = Thread(target=self.loop)
        # t.start()
        self.loop()
