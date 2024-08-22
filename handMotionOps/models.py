# get gesture and convert it to string
class Gesture:
    def __init__(self, fingers) -> None:
        self.fingers = fingers

    def to_string(self) -> str:
        j = ""
        for i in self.fingers:
            if i:
                j += '1'
            else:
                j += '0'
        return j


class Command:
    def __init__(self, text: str) -> None:
        self.text = text

    def execute(self):
        # TODO execute maybe using system.os
        pass


def get_gesture_from_hand(hand) -> Gesture:
    fingers = [hand.landmark[4].x > hand.landmark[2].x,
               hand.landmark[8].y < hand.landmark[6].y,
               hand.landmark[12].y < hand.landmark[10].y,
               hand.landmark[16].y < hand.landmark[14].y,
               hand.landmark[20].y < hand.landmark[18].y]
    return Gesture(fingers)


def get_gesture(gesture: str) -> Gesture:
    fingers = []

    for i in gesture:
        if i == "0":
            fingers.append(False)
        elif i == "1":
            fingers.append(True)

    return Gesture(fingers)
