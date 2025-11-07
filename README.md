# Macropad Hotkeys II

A derivative of the
[Macropad Hotkeys](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/LICENSE)
example from the
[Adafruit Learning System Guide](https://learn.adafruit.com/macropad-hotkeys/project-code).


## Modifications

- Rotary button no longer is an action, instead it turns on/off the displays
- Macros for Blender, Safari, MIDI drum kit, generic number pad and Zoom
- Support for HID consumer control codes
- Support for mouse buttons
- Support for sending MIDI notes
- When no HID connection is present (power only), keep LEDs off and provide a message
- Mount filesystem as read-only unless the encoder button is pressed on boot
- Refactored the code to make it (maybe) easier to modify


## Using

You use the Macropad Hotkeys much like the original
[Adafruit version](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/LICENSE),
with a few differences.

Use the dial to select the macro template you would like to use. The macros appear
in the order specified within each config file (see [Configuration](#configuration) below for details).
Once you have the macro you like selected, you are free to hammer away at the keys.

Click the rotary dial to turn off the display & LEDs - click it again to turn it back on.
Note the keys continue to respond even when they are not lit.


## Configuration

The `macros/` folder has a list of macro templates to chose from, all of which
can be altered at your whim. First make sure to mount your Macropad in read/write
mode (see [Updating](#updating)) and then open up the `.py` examples in the
`macros/` folder. Note that each has a list of settings, including:

- The name that will show at the top of the OLED display
- The sequential order that it will be shown when rotating the encoder dial
- A list of macros, sorted by row

Each macro consists of an LED color, a label to appear on the OLED display,
and a sequence of keys. A "key" can be text, a keyboard key, a consumer control
key (like play/pause), a mouse action, or a MIDI note. More than one key can
be specified in a sequence.


## Installing

First make sure that your Macropad has the
[latest version of CircuitPython 10.0 installed](https://circuitpython.org/board/adafruit_macropad_rp2040/).
See [https://learn.adafruit.com/adafruit-macropad-rp2040/circuitpython](https://learn.adafruit.com/adafruit-macropad-rp2040/circuitpython)
for instructions on how to update the Macropad to have the latest version of
CircuitPython.

When installing Macropad Hotkeys for the first time, extract the latest
[MacroPad Hotkeys.zip](https://github.com/deckerego/Macropad_Hotkeys/releases/latest)
into a directory, then copy the contents of that extracted archive
into the CIRCUITPY drive that appears when you plug in your Macropad.
Ensure that the contents of the `lib/` subdirectory are also copied - these are
the precompiled Adafruit libraries that power the Macropad.


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
