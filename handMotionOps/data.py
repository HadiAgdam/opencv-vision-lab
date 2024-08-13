from models import Command, Gesture, get_gesture
from json import dumps, loads

# we define a function to save the data recieved from user to our json file


def save(gesture: Gesture, command: Command):
    # open json file thta we save our data in it
    # TODO ask Hadi
    f = open("./data/data.json")
    # deserialize a JSON string into a Python object and read it
    l = loads(f.read())
    # check if gesture is already added
    for i in l:
        g = get_gesture(i["gesture"])
        c = Command(i["command"])

        if g == gesture and c == command:
            return

        if g == gesture and c != command:
            l.pop({
                "gesture": gesture.to_string(),
                "command": command.text
            })
    # Add the new command and gesture to the file
    l.append({
        "gesture": gesture.to_string(),
        "command": command.text
    })

    f = open(
        "/Users/hadi/pythonProjects/opencv-vision-lab/handMotionOps/data/data.json", "w+")
    # serialize the Python object to a JSON formatted string
    f.write(dumps(l))

    f.close()


# we run the function ti save the data
save(
    Gesture(None),
    Command("echo hello")
)
