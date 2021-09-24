# pylint: disable=import-error, unused-import, too-few-public-methods

import os
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad
from app import App
from consumer import Toolbar
from mouse import Mouse
from sleeper import Sleep
from keyboard import Keyboard

MACRO_FOLDER = '/macros'

macropad = MacroPad()
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False
group = displayio.Group()

def init_display():
    for key_index in range(12):
        x = key_index % 3
        y = key_index // 3
        group.append(
            label.Label(terminalio.FONT,
                text='',
                color=0xFFFFFF,
                anchored_position=((macropad.display.width - 1) * x / 2,
                macropad.display.height - 1 - (3 - y) * 12),
                anchor_point=(x / 2, 1.0)
            )
        )
    group.append(Rect(0, 0, macropad.display.width, 12, fill=0xFFFFFF))
    group.append(
        label.Label(
            terminalio.FONT,
            text='',
            color=0x000000,
            anchored_position=(macropad.display.width//2, -2),
            anchor_point=(0.5, 0.0)
        )
    )
    macropad.display.show(group)

def switch(app):
    group[13].text = app.name   # Application name
    for i in range(12):
        if i < len(app.macros): # Key in use, set label + LED color
            macropad.pixels[i] = app.macros[i][0]
            group[i].text = app.macros[i][1]
        else:  # Key not in use, no label or LED
            macropad.pixels[i] = 0
            group[i].text = ''
    macropad.keyboard.release_all()
    macropad.pixels.show()
    macropad.display.refresh()

def make_key(item):
    if isinstance(item, Toolbar):
        return item
    elif isinstance(item, Mouse):
        return item
    elif isinstance(item, float):
        return Sleep(item)
    else:
        return Keyboard(item)

init_display()
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
    group[13].text = 'NO MACRO FILES FOUND'
    macropad.display.refresh()
    quit()

apps.sort(key=lambda m:m.order)

last_position = None
sleeping = False
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0
switch(apps[app_index])

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
            macropad.pixels[key_number] = 0xFFFFFF
            macropad.pixels.show()
        elif key_number is 12:
            if not sleeping:
                macropad.pixels.fill((0, 0, 0))
                macropad.pixels.show()
                macropad.display.auto_brightness = False
                macropad.display.brightness = 0
                macropad.display.show(displayio.Group())
                macropad.display.refresh()
            else:
                macropad.display.brightness = 1
                macropad.display.auto_brightness = True
                macropad.display.show(group)
                macropad.display.refresh()
                switch(apps[app_index])
            sleeping = not sleeping

        for item in sequence:
            make_key(item).press(macropad)

    else:
        # Release any still-pressed keys
        for item in sequence:
            make_key(item).release(macropad)
        if not sleeping and key_number < 12: # No pixel for encoder button
            macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
            macropad.pixels.show()
