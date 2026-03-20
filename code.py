import time
from adafruit_macropad import MacroPad
from app import App
from keys import Keys
from screen import ScreenListener
from pixels import PixelListener
from hid import InputDeviceListener
import usb_hid # type: ignore (part of CircuitPython standard libs)

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

# Core objects
macropad = MacroPad()
screen = ScreenListener(macropad)
pixels = PixelListener(macropad)
hid = InputDeviceListener(macropad)

# State variables
last_time_seconds = time.monotonic()
last_position = macropad.encoder
sleep_remaining = None
keys = None
macro_changed = False
app_index = 0

# Fractions of a second that have elapsed since this method's last run
def elapsed_seconds():
    global last_time_seconds
    current_seconds = time.monotonic()
    elapsed_seconds = current_seconds - last_time_seconds
    last_time_seconds = current_seconds
    return elapsed_seconds

# Set the macro page (app) at the given index
def set_app(index):
    global app_index, keys, screen, sleep_remaining

    macropad.keyboard.release_all()
    screen.initialize()
    app_index = index

    sleep_remaining = apps[app_index].timeout
    screen.setTitle(apps[app_index].name)
    try:
        keys = Keys(apps[app_index])
        keys.addListener(hid)
        keys.addListener(screen)
        keys.addListener(pixels)
    except Exception as err:
        print(err)
        screen.setText("Error loading macro")

# Load available macros
apps = App.load_all(MACRO_FOLDER)
if not apps:
    screen.setTitle('NO MACRO FILES FOUND')
    while True:
        time.sleep(60.0)

# Load our first app page
screen.initialize()
screen.setTitle(' CONNECTING... ')
set_app(app_index)

while True: # Input event loop
    macropad.encoder_switch_debounced.update()
    sleep_remaining -= elapsed_seconds()
    event = macropad.keys.events.get()
    
    if (event and event.released) or last_position != macropad.encoder or macropad.encoder_switch_debounced.released:
        keys.release(Keys.KEY_SLEEP)                 # Don't go to sleep!
        sleep_remaining = apps[app_index].timeout
    if sleep_remaining <= 0:                         # Go to sleep and slow down
        keys.press(Keys.KEY_SLEEP)
        time.sleep(1.0)
    elif event and event.pressed:                    # Key was pressed
        keys.press(event.key_number)
    elif event and event.released:                   # Key was released
        keys.release(event.key_number)
    elif macropad.encoder_switch and macropad.encoder < last_position:
        last_position = macropad.encoder             # Push down and turn (left)
        set_app((app_index - 1) % len(apps))
        macro_changed = True
    elif macropad.encoder_switch and macropad.encoder > last_position:
        last_position = macropad.encoder             # Push down and turn (right)
        set_app((app_index + 1) % len(apps))
        macro_changed = True
    elif macropad.encoder < last_position:           # Encoder counter-clockwise
        while macropad.encoder < last_position:
            keys.press(Keys.KEY_ENC_LEFT)
            last_position -= 1
        keys.release(Keys.KEY_ENC_LEFT)
    elif macropad.encoder > last_position:           # Encoder clockwise
        while macropad.encoder > last_position:
            keys.press(Keys.KEY_ENC_RIGHT)
            last_position += 1
        keys.release(Keys.KEY_ENC_RIGHT)
    elif macropad.encoder_switch_debounced.released and macro_changed:
        keys.press(Keys.KEY_LAUNCH)                  # Press the "new page" button
        keys.release(Keys.KEY_LAUNCH)
        macro_changed = False
    elif macropad.encoder_switch_debounced.released: # Encoder button "pressed"
        keys.press(Keys.KEY_ENC_BUTTON)
