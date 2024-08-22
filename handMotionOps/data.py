from models import Command, Gesture, get_gesture
from json import dumps, loads


# we define a function to save the data received from user to our json file


def save(gesture: Gesture, command: Command):
    # open json file that we save our data in it
    with open("data/data.json", 'r') as f:
        data_list = loads(f.read())

    for idx, i in enumerate(data_list):
        if i["gesture"] == gesture.to_string():
            data_list.pop(idx)

    data_list.append({
        "gesture": gesture.to_string(), "command": command.text
    })

    with open("data/data.json", "w") as f:
        f.write(dumps(data_list))


def read():
    saved_gestures = []
    with open("data/data.json", "r") as f:
        data_list = [item for item in loads(f.read())]
        for i in data_list:
            g = get_gesture(i["gesture"])
            c = Command(i["command"])
            saved_gestures.append((g, c))
    return saved_gestures


def get_command_by_gesture(g: Gesture) -> Command:
    with open("data/data.json", 'r') as f:
        data_list = loads(f.read())

        for i in data_list:
            if i["gesture"] == g.to_string():
                return Command(i["command"])

