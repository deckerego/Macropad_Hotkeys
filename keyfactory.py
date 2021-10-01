from consumer import Toolbar
from mouse import Mouse
from sleeper import Sleep
from keyboard import Keyboard
from midi import Midi

def get(item):
    if isinstance(item, Toolbar):
        return item
    elif isinstance(item, Mouse):
        return item
    elif isinstance(item, Midi):
        return item
    elif isinstance(item, float):
        return Sleep(item)
    else:
        return Keyboard(item)
