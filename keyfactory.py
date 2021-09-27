from consumer import Toolbar
from mouse import Mouse
from sleeper import Sleep
from keyboard import Keyboard

def get(item):
    if isinstance(item, Toolbar):
        return item
    elif isinstance(item, Mouse):
        return item
    elif isinstance(item, float):
        return Sleep(item)
    else:
        return Keyboard(item)
