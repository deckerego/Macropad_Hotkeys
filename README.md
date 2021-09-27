# Macropad Hotkeys

A derivative of the
[Macropad Hotkeys](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/LICENSE)
example from the
[Adafruit Learning System Guide](https://learn.adafruit.com/macropad-hotkeys/project-code).


## Modifications

- Rotary button no longer is an action, instead it turns on/off the displays
- Macros for Blender, Safari, generic number pad and Zoom
- Support for HID consumer control codes
- Support for mouse buttons
- When no HID connection is present (power only), keep LEDs off and provide a message
- Mount filesystem as read-only unless the encoder button is pressed on boot
- Refactored the code to make it (maybe) easier to modify

## Installing

When installing for the first time, copy all the Python (.py) files onto the
CIRCUITPY drive that apears when you plug in your Macropad. You will also need
the libraries listed in the
[Adafruit Learning System Guide](https://learn.adafruit.com/macropad-hotkeys/project-code)
and available as the [CircuitPython library bundle](https://circuitpython.org/libraries).

The libraries required by this version of Macropad Hotkeys includes:
- adafruit_debouncer.mpy
- adafruit_display_shapes
- adafruit_display_text
- adafruit_displayio_layout
- adafruit_hid
- adafruit_macropad.mpy
- adafruit_midi
- adafruit_pixelbuf.mpy
- adafruit_simple_text_display.mpy
- neopixel.mpy


## Updating

After you first install this version of Macropad Hotkeys and reboot the Macropad,
the CIRCUITPY filesystem will be mounted as read-only. When mounting the device
as read-only, Windows and MacOS won't complain if you unplug or reboot the device
without unmounting it, making it more like a regular old HID device.

To update or edit the code on the device, or to modify the macros, you first
need to reboot the device with the CIRCUITPY drive mounted in read/write mode.
To do that, reboot the device using the boot switch on the left of the
Macropad, and then after releasing the button immediately hold down the
rotary encoder button. You should see the text "Mounting Read/Write" quickly
appear on the screen, and then the CIRCUITPY drive will mount in read/write mode.
