import time
from adafruit_macropad import MacroPad
from app import App
from keys import Keys
from screen import ScreenListener
from pixels import PixelListener
from hid import InputDeviceListener
from commands import Sleep

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
screen = ScreenListener(macropad)
pixels = PixelListener(macropad)
hid = InputDeviceListener(macropad)
last_time_seconds = time.monotonic()
sleep_remaining = None
keys = None
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
    app_index = index

    sleep_remaining = apps[app_index].timeout
    screen.setTitle(apps[app_index].name)
    macropad.keyboard.release_all()

    keys = Keys(apps[app_index])
    keys.addListener(hid)
    keys.addListener(screen)
    keys.addListener(pixels)

# Load available macros
screen.initialize()
apps = App.load_all(MACRO_FOLDER)
if not apps:
    screen.setError('NO MACRO FILES FOUND')
    while True:
        pass

try: # Test the USB HID connection
    macropad.keyboard.release_all()
except OSError as err:
    print(err)
    screen.setError('NO USB CONNECTION')
    while True:
        pass

# Prep before the run loop
set_app(app_index)

while True: # Event loop
    macropad.encoder_switch_debounced.update()
    sleep_remaining -= elapsed_seconds()
    event = macropad.keys.events.get()
    last_position = macropad.encoder

    if event:                                        # Don't go to sleep!
        sleep_remaining = apps[app_index].timeout
    if sleep_remaining <= 0:                         # Go to sleep and slow down
        keys.press(Sleep())
        time.sleep(1.0)
    elif event and event.pressed:                    # Key was pressed
        keys.press(event.key_number)
    elif event and event.released:                   # Key was released
        keys.release(event.key_number)
    elif macropad.encoder < last_position:           # Rotated counter-clockwise
        last_position = macropad.encoder
        keys.press(Keys.KEY_ENC_LEFT)
    elif macropad.encoder > last_position:           # Rotated clockwise
        last_position = macropad.encoder
        keys.press(Keys.KEY_ENC_RIGHT)
    elif macropad.encoder_switch:                    # Encoder button pressed
        keys.press(Keys.KEY_ENC_BUTTON)
    elif macropad.encoder_switch_debounced.released: # Encoder button released
        keys.release(Keys.KEY_ENC_BUTTON)
