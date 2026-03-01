# Adafruit Macropad Libraries

In packaged versions of this app, these MicroPython compiled libraries are provided as a 
convenience when installing Macropad Hotkeys. See the Macropad
[Adafruit Learning System Guide](https://learn.adafruit.com/macropad-hotkeys/project-code)
for additional details.

If you instead cloned this repository, you will receive the mocked version
of the libraries used for automated testing. To install Macropad Hotkeys
from a repository, remove the `*.py` files from `lib/` and replace them
with the corresponding files from the
[CircuitPython library bundle](https://circuitpython.org/libraries).

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

The production libraries are individually licensed in each of their GitHub 
repositories and are provided by Adafruit under the MIT license
(see also [LICENSE](./LICENSE) in this directory)
