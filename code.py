import time
from adafruit_macropad import MacroPad
from app import App
from screen import Screen
from keys import Keys

## DEPRECATED 
# Ensure backwards compatibility for the 2.x series
# So we don't have to change import statements in old macros
import sys
import commands
sys.modules['keyboard'] = commands
sys.modules['mouse'] = commands
sys.modules['pause'] = commands
sys.modules['sleep'] = commands
sys.modules['midi'] = commands
sys.modules['consumer'] = commands

MACRO_FOLDER = '/macros'

macropad = MacroPad()
screen = Screen(macropad)
keys = None
app_index = 0

# Set the macro page (app) at the given index
def set_app(index):
    global app_index, sleep_remaining, keys, screen
    app_index = index
    macropad.keyboard.release_all()
    screen.setApp(apps[app_index])
    keys = Keys(macropad, apps[app_index])

# Load available macros
screen.initialize()
apps = App.load_all(MACRO_FOLDER)
if not apps:
    screen.setTitle('NO MACRO FILES FOUND')
    while True:
        pass

try: # Test the USB HID connection
    macropad.keyboard.release_all()
except OSError as err:
    print(err)
    screen.setTitle('NO USB CONNECTION')
    while True:
        pass

# Prep before the run loop
set_app(app_index)

while True: # Event loop
    macropad.encoder_switch_debounced.update()
    time.sleep(0.5)
