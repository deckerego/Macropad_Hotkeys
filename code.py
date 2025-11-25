import time
import keyfactory
from adafruit_macropad import MacroPad
from app import App
from display import Display
from pixels import Pixels
from sleep import Sleep

MACRO_FOLDER = '/macros'
SLEEP_AFTER = 300 # Dim the display after 5 minutes

macropad = MacroPad()
last_position = macropad.encoder
last_time_seconds = time.monotonic()
sleep_remaining = SLEEP_AFTER
macro_changed = False
app_index = 0

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
state["screen"].setApp(apps[0])
state["pixels"].setApp(apps[0])

while True:
    position = state["macropad"].encoder
    state["macropad"].encoder_switch_debounced.update()
    pressed = False
    rotated = False

    # Do we need to press the "sleep" button?
    sleep_remaining -= elapsed_seconds()
    if not state["sleeping"] and sleep_remaining <= 0:
        Sleep().press(state)

    # Determine the event type
    if position != last_position and state["macropad"].encoder_switch:
        macro_changed = True
        last_position = position
        app_index = position % len(apps)
        state["macropad"].keyboard.release_all()
        state["screen"].setApp(apps[app_index])
        state["pixels"].setApp(apps[app_index])
        continue # Changing macros, not a keypress event
    elif macro_changed and state["macropad"].encoder_switch_debounced.released:
        macro_changed = False
        continue # We've changed macros, ignore encoder press
    elif state["macropad"].encoder_switch_debounced.released:
        key_number = 12
        pressed = state["macropad"].encoder_switch_debounced.released
    elif position != last_position:
        key_number = 13 if position < last_position else 14
        last_position = position
        rotated = True
    else:
        event = state["macropad"].keys.events.get()
        if not event or event.key_number >= len(apps[app_index].macros):
            if state["sleeping"]: time.sleep(1.0) # Low power mode
            continue # No key events, or no corresponding macro, resume loop
        key_number = event.key_number
        pressed = event.pressed

    try: # No such sequence for this key
        sequence = apps[app_index].macros[key_number][2] if key_number <= 14  else []
    except (IndexError) as err:
        print("Couldn't find sequence for key number ", key_number)
        sequence = None

    # Wake up if there is a key event while sleeping
    if state["sleeping"] and (pressed or rotated):
        Sleep().press(state)
        sleep_remaining = SLEEP_AFTER
        continue

    if sequence and (pressed or rotated):
        if not state["sleeping"] and key_number < 12:
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
                
    if sequence and (not pressed or rotated):
        if type(sequence) is list: 
            for item in sequence:
                if type(item) is not list: # Release any still-pressed key combinations
                    keyfactory.get(item).release(state)
                # Macro key cobinations should already have been released
        else: # Release any still-pressed single commands
            keyfactory.get(sequence).release(state)
        if not state["sleeping"] and key_number < 12: # No pixel for encoder button
            state["pixels"].reset(key_number)
