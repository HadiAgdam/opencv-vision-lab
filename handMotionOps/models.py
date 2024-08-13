# get gesture and convert it to string
class Gesture:
    def __init__(self, hand) -> None:
        self.fingers = [False]*5

        self.fingers[0] = hand.landmark[4].x > hand.landmark[2].x
        self.fingers[1] = hand.landmark[8].y < hand.landmark[6].y
        self.fingers[2] = hand.landmark[12].y < hand.landmark[10].y
        self.fingers[3] = hand.landmark[16].y < hand.landmark[14].y
        self.fingers[4] = hand.landmark[20].y < hand.landmark[18].y

    def to_string(self) -> str:
        j = ""
        for i in self.fingrs:
            if i:
                j += '1'
            else:
                j += '0'
        return j


class Command:
    def __init__(self, text: str) -> None:
        self.text = text


def get_gesture(gesture: str) -> Gesture:
    l2 = []
    for k in gesture:
        l2.append(k == '1')
        # TODO return gesture
