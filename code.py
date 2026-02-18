import time
from adafruit_macropad import MacroPad
from app import App
from display import Display
from keys import Keys

MACRO_FOLDER = '/macros'

macropad = MacroPad()
last_time_seconds = time.monotonic()
sleep_remaining = None
app_index = 0
keys = None
screen = Display(macropad)

# Fractions of a second that have elapsed since this method's last run
def elapsed_seconds():
    global last_time_seconds
    current_seconds = time.monotonic()
    elapsed_seconds = current_seconds - last_time_seconds
    last_time_seconds = current_seconds
    return elapsed_seconds

# Set the macro page (app) at the given index
def set_app(index):
    global app_index, sleep_remaining, keys, screen
    app_index = index
    sleep_remaining = apps[app_index].timeout
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
set_app(0)

while True: # Event loop
    macropad.encoder_switch_debounced.update()
    time.sleep(1.0)
