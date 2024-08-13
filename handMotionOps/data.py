from models import Command, Gesture, get_gesture
from json import dumps, loads

# we define a function to save the data recieved from user to our json file


def save(gesture: Gesture, command: Command):
    # ./ is incorrenct. If you want to get a file from upper directory, you should use ../

    # open json file that we save our data in it

    with open("data/data.json", 'r') as f:
        data_list = loads(f.read)

    data_list = [item for item in data_list if not (get_gesture(item["gesture"]) == gesture and Command(item["command"]) != command)]

    data_list.append({
        "gesture": gesture.to_string(),
    })

    with open("data/data.json", "w") as f:
        dumps(data_list, f, indent=4)