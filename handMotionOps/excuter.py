# in this file we detect order and and excute the related command from json file
# TODO read json
# TODO check for gesture all the time
# TODO if seen a saved gesture check for its order
# TODO do the related order

from data import get_command_by_gesture
from models import Gesture
from interface import Interface


duration = 1.5
r = 150


def execute(g: Gesture):
    command = get_command_by_gesture(g)
    command.execute()


interface = Interface(execute, 2)


if __name__ == "_main__":
    interface.init_camera_source()
    interface.start()
