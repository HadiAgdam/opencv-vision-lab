# we decet and save hand gestures
# TODO reaad commands
# TODO get gesture
# TODO save as json file

from models import Gesture, Command
from data import save
from interface import Interface, destroy_windows

print("Welcome to HandMotionOps.")

command = Command(input("enter command :"))

print("Show gesture to camera with your left hand, hold it for 3 seconds to save ...")


def end(g: Gesture):
    save(g, command)
    print("saved successfully")
    destroy_windows()
    exit()


i = Interface(end)

if __name__ == "__main__":
    i.start()
