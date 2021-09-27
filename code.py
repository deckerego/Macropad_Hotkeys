import os
import time
import keyfactory
from adafruit_macropad import MacroPad
from app import App
from display import Display
from pixels import Pixels

MACRO_FOLDER = '/macros'

macropad = MacroPad()
macropad.pixels.auto_write = False
screen = Display(macropad)
pixels = Pixels(macropad)

def switch(app):
    macropad.keyboard.release_all()
    screen.setApp(app)
    pixels.setApp(app)

screen.initialize()
apps = []
files = os.listdir(MACRO_FOLDER)
for filename in files:
    if filename.endswith('.py'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.app))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError, IndexError, TypeError) as err:
            print(err)
            pass

if not apps:
    display.setText('NO MACRO FILES FOUND')
    quit()

apps.sort(key=lambda m:m.order)

last_position = None
sleeping = False
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0

while True:
    try:
        switch(apps[app_index])
        break
    except OSError as err:
        print(err)
        display.setText('NO USB CONNECTION')
        time.sleep(5000)

while True:
    position = macropad.encoder
    if position != last_position:
        app_index = position % len(apps)
        switch(apps[app_index])
        last_position = position

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
                display.sleep()
                pixels.off()
            else:
                display.resume()
                switch(apps[app_index])
            sleeping = not sleeping

        for item in sequence:
            keyfactory.get(item).press(macropad)

    else:
        # Release any still-pressed keys
        for item in sequence:
            keyfactory.get(item).release(macropad)
        if not sleeping and key_number < 12: # No pixel for encoder button
            pixels.reset(key_number)
