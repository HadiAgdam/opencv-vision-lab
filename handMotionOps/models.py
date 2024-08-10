# get gesture and convert it to string
class Gesture:
    def __init__(self, hand) -> None:
        self.finger = [False]*5

        self.finger[0] = hand.landmark[4].x < hand.landmark[2].x
        self.finger[1] = hand.landmark[8].y < hand.landmark[6].Y
        self.finger[2] = hand.landmark[12].y < hand.landmark[10].Y
        self.finger[3] = hand.landmark[16].y < hand.landmark[14].Y
        self.finger[4] = hand.landmark[20].y < hand.landmark[18].Y

    def to_string(self) -> str:
        j = ""
        for i in self.fingr:
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
