import time
import keyfactory
from adafruit_macropad import MacroPad
from app import App
from display import Display
from pixels import Pixels
from sleep import Sleep

KEY_LAUNCH = -1
KEY_ENC_BUTTON = 12
KEY_ENC_LEFT = 13
KEY_ENC_RIGHT = 14
MAX_KEYS = 14
MAX_LEDS = 12
MACRO_FOLDER = '/macros'
SLEEP_AFTER = 300 # Dim the display after 5 minutes

macropad = MacroPad()
last_position = macropad.encoder
last_time_seconds = time.monotonic()
sleep_remaining = SLEEP_AFTER
macro_changed = False
current_app = None

state = {
    "macropad": macropad,
    "screen": Display(macropad),
    "pixels": Pixels(macropad),
    "sleeping": False,
}

# Seconds (floating) since last invocation
def elapsed_seconds():
    global last_time_seconds
    current_seconds = time.monotonic()
    elapsed_seconds = current_seconds - last_time_seconds
    last_time_seconds = current_seconds
    return elapsed_seconds

def set_app(index):
    global current_app
    current_app = apps[index]
    state["macropad"].keyboard.release_all()
    state["screen"].setApp(current_app)
    state["pixels"].setApp(current_app)

def get_sequence(key):
    global current_app
    if key == KEY_LAUNCH:
        return current_app.launch[2] if current_app.launch else None
    try: # No such sequence for this key
        return current_app.macros[key][2] if key <= MAX_KEYS else []
    except (IndexError) as err:
        print("Couldn't find sequence for key number ", key)
        return None

# Load available macros
state["screen"].initialize()
apps = App.load_all(MACRO_FOLDER)
if not apps:
    state["screen"].setTitle('NO MACRO FILES FOUND')
    while True:
        pass

try: # Test the USB HID connection
    state["macropad"].keyboard.release_all()
except OSError as err:
    print(err)
    state["screen"].setTitle('NO USB CONNECTION')
    while True:
        pass

# Prep before the run loop
set_app(0)

while True: # Event loop
    position = state["macropad"].encoder
    state["macropad"].encoder_switch_debounced.update()
    pressed = False
    rotated = False

    # Do we need to press the "sleep" button?
    sleep_remaining -= elapsed_seconds()
    if not state["sleeping"] and sleep_remaining <= 0:
        Sleep().press(state)
        continue

    # Determine the event type
    if position != last_position and state["macropad"].encoder_switch:
        macro_changed = True
        last_position = position
        set_app(position % len(apps))
        continue # Changing macros, not a keypress event
    elif macro_changed and state["macropad"].encoder_switch_debounced.released:
        macro_changed = False
        key_number = KEY_LAUNCH
        rotated = True
    elif state["macropad"].encoder_switch_debounced.released:
        key_number = KEY_ENC_BUTTON
        pressed = state["macropad"].encoder_switch_debounced.released
    elif position != last_position:
        key_number = KEY_ENC_LEFT if position < last_position else KEY_ENC_RIGHT
        last_position = position
        rotated = True
    else:
        event = state["macropad"].keys.events.get()
        if not event or event.key_number >= len(current_app.macros):
            if state["sleeping"]: time.sleep(1.0) # Low power mode
            continue # No key events, or no corresponding macro, resume loop
        key_number = event.key_number
        pressed = event.pressed

    # Wake up if there is a key event while sleeping
    if state["sleeping"] and (pressed or rotated):
        Sleep().press(state)
        continue
    sleep_remaining = SLEEP_AFTER

    sequence = get_sequence(key_number)
    if sequence and (rotated or pressed):
        if not state["sleeping"] and (0 <= key_number < MAX_LEDS):
            state["pixels"].highlight(key_number, 0xFFFFFF)

        if type(sequence) is list:
            for item in sequence:
                if type(item) is list: # We have a macro to execute
                    for subitem in item: # Press the key combination
                        keyfactory.get(subitem).press(state)
                    for subitem in item: # Immediately release the key combo
                        keyfactory.get(subitem).release(state)
                else: # We have a key combination to press
                    keyfactory.get(item).press(state)
        else: # We just have a single command to execute
            keyfactory.get(sequence).press(state)
                
    if sequence and (rotated or not pressed):
        if type(sequence) is list: 
            for item in sequence:
                if type(item) is not list: # Release any still-pressed key combinations
                    keyfactory.get(item).release(state)
                # Macro key cobinations should already have been released
        else: # Release any still-pressed single commands
            keyfactory.get(sequence).release(state)
        if not state["sleeping"] and (0 <= key_number < MAX_LEDS): # No pixel for encoder button
            state["pixels"].reset(key_number)
