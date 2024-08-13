from models import Command, Gesture, get_gesture
from json import dumps, loads





def save(gesture: Gesture, command: Command):
    f = open("/Users/hadi/pythonProjects/opencv-vision-lab/handMotionOps/data/data.json")

    l = loads(f.read())

    for i in l:
        g = get_gesture(i["gesture"])
        c = Command(i["command"])

        if g == gesture and c == command:
            return
        
        if g == gesture and c!= command:
            l.pop({
                "gesture": gesture.to_string(),
                "command": command.text
            })

    l.append({
        "gesture": gesture.to_string(),
        "command": command.text
    })

    f = open("/Users/hadi/pythonProjects/opencv-vision-lab/handMotionOps/data/data.json", "w+")
    
    f.write(dumps(l))

    f.close()
