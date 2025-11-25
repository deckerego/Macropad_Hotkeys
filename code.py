import time
import keyfactory
from adafruit_macropad import MacroPad
from app import App
from display import Display
from pixels import Pixels

MACRO_FOLDER = '/macros'

macropad = MacroPad()
screen = Display(macropad)
pixels = Pixels(macropad)
last_position = macropad.encoder
macro_changed = False
sleeping = False
app_index = 0

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

screen.setApp(apps[0])
pixels.setApp(apps[0])

while True:
    position = macropad.encoder
    macropad.encoder_switch_debounced.update()

    if position != last_position and macropad.encoder_switch:
        macro_changed = True
        last_position = position
        app_index = position % len(apps)
        macropad.keyboard.release_all()
        screen.setApp(apps[app_index])
        pixels.setApp(apps[app_index])
        continue # Changing macros, not a keypress event
    elif macro_changed and macropad.encoder_switch_debounced.released:
        macro_changed = False
        continue # We've changed macros, ignore encoder press
    elif macropad.encoder_switch_debounced.released:
        key_number = 12
        pressed = macropad.encoder_switch_debounced.released
    elif position != last_position:
        key_number = 13 if position < last_position else 14
        last_position = position
        pressed = True
    else:
        event = macropad.keys.events.get()
        if not event or event.key_number >= len(apps[app_index].macros):
            continue # No key events, or no corresponding macro, resume loop
        key_number = event.key_number
        pressed = event.pressed

    try:
        sequence = apps[app_index].macros[key_number][2] if key_number <= 14  else []
    except (IndexError) as err:
        print("Couldn't find sequence for key number ", key_number)
        sequence = None

    if sequence and pressed:
        if not sleeping and key_number < 12:
            pixels.highlight(key_number, 0xFFFFFF)

        if type(sequence) is list:
            for item in sequence:
                if type(item) is list: # We have a macro to execute
                    for subitem in item: # Press the key combination
                        keyfactory.get(subitem).press(macropad)
                    for subitem in item: # Immediately release the key combo
                        keyfactory.get(subitem).release(macropad)
                else: # We have a key combination to press
                    keyfactory.get(item).press(macropad)
        else: # We just have a single command to execute
            keyfactory.get(sequence).press(macropad)
                
    elif sequence:
        if type(sequence) is list: 
            for item in sequence:
                if type(item) is not list: # Release any still-pressed key combinations
                    keyfactory.get(item).release(macropad)
                # Macro key cobinations should already have been released
        else: # Release any still-pressed single commands
            keyfactory.get(sequence).release(macropad)
        if not sleeping and key_number < 12: # No pixel for encoder button
            pixels.reset(key_number)
