from models import Command, Gesture, get_gesture
from json import dumps, loads

# we define a function to save the data recieved from user to our json file


def save(gesture: Gesture, command: Command):
    # ./ is incorrenct. If you want to get a file from upper directory, you should use ../

    # open json file that we save our data in it

    with open("data/data.json", 'r') as f:
        data_list = loads(f.read())

    data_list = [item for item in data_list]
    for idx, ges in enumerate(data_list):
        if ges["gesture"] == gesture.to_string():
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



