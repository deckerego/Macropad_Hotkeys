from consumer import Toolbar
from mouse import Mouse
from pause import Pause
from keyboard import Keyboard
from midi import Midi
from sleep import Sleep

def get(item):
    if isinstance(item, Toolbar):
        return item
    elif isinstance(item, Mouse):
        return item
    elif isinstance(item, Midi):
        return item
    elif isinstance(item, Sleep):
        return item
    elif isinstance(item, float):
        return Pause(item)
    else:
        return Keyboard(item)
