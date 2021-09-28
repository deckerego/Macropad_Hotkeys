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
last_position = None
sleeping = False
last_encoder_switch = macropad.encoder_switch_debounced.pressed
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

while True:
    position = macropad.encoder
    if position != last_position:
        last_position = position
        app_index = position % len(apps)
        macropad.keyboard.release_all()
        screen.setApp(apps[app_index])
        pixels.setApp(apps[app_index])

    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch != last_encoder_switch:
        last_encoder_switch = encoder_switch
        key_number = 12
        pressed = encoder_switch
    else:
        event = macropad.keys.events.get()
        if not event or event.key_number >= len(apps[app_index].macros):
            continue # No key events, or no corresponding macro, resume loop
        key_number = event.key_number
        pressed = event.pressed

    sequence = apps[app_index].macros[key_number][2] if key_number < 12  else []
    if pressed:
        if not sleeping and key_number < 12:
            pixels.highlight(key_number, 0xFFFFFF)
        elif key_number is 12:
            if not sleeping:
                screen.sleep()
                pixels.sleep()
            else:
                screen.resume()
                pixels.resume()
            sleeping = not sleeping

        for item in sequence:
            keyfactory.get(item).press(macropad)

    else:
        # Release any still-pressed keys
        for item in sequence:
            keyfactory.get(item).release(macropad)
        if not sleeping and key_number < 12: # No pixel for encoder button
            pixels.reset(key_number)
