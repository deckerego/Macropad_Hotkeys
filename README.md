# Macropad Hotkeys II

A rebuild of the
[Macropad Hotkeys](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/LICENSE)
example from the
[Adafruit Learning System Guide](https://learn.adafruit.com/macropad-hotkeys/project-code).


## Modifications

- A number of sample macros for things such as Blender, a MIDI drum kit, DaVinici Resolve, and more
- Support for HID consumer control codes
- Support for mouse buttons
- Support for sending MIDI notes
- When no HID connection is present (power only), keep LEDs off and provide a message
- Stop your OS from shouting when you unplug the Macropad - mount filesystem as read-only unless the KEY1 button is pressed on boot
- Refactored the code to make it (maybe) easier to modify


## Demo

<a href="http://www.youtube.com/watch?feature=player_embedded&v=rzTTRM9xGms" target="_blank">
 <img src="http://img.youtube.com/vi/rzTTRM9xGms/mqdefault.jpg" alt="Macropad Hotkeys II Demo" width="320" height="240" border="10" />
</a>


## Using

You use the Macropad Hotkeys in a similar way to the original
[Adafruit version](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/LICENSE),
with several improvements.

At first install you don't have any macros installed - however several examples are provided
in the `macros/examples` directory. The [Macropad Hotkeys II Wiki](https://github.com/deckerego/Macropad_Hotkeys/wiki)
has a number of additional templates you can customize for things like DaVinci Resolve or Baldur's Gate III. 
See [Configuration](#configuration) for details.

Once you have some macros installed, push down & rotate the dial to select the macro template you 
would like to use; the macros appear in the order specified within each config file. 
Once you have the macro you like selected, you are free to hammer away at the keys.


## Configuration

The `macros/examples/` folder has template macro pages to start from, or you can view
some read-made macro pages in the 
[Macropad Hotkeys II Wiki](https://github.com/deckerego/Macropad_Hotkeys/wiki).

To add a new macro page, first make sure to mount your Macropad in read/write
mode (see [Updating](#updating)) and then copy a `.py` example in the
`macros/` folder. Note that each has a list of settings, including:

- The name that will show at the top of the OLED display
- The sequential order that it will be shown when rotating the encoder dial
- An optional timeout before the LEDs and display go to sleep
- A macro to launch when switching to this screen
- A list of macros, sorted by row
- A list of macros for the rotary encoder

Each macro consists of an LED color, a label to appear on the OLED display,
and a sequence of keys. A "key" can be text, a keyboard key, a consumer control
key (like play/pause), a mouse action, or a MIDI note. More than one key can
be specified in a sequence.

The example in `macros/examples/minimal.py` is a good starter for your own custom macro.
From this example you can see the triplets which specify color, label, and commands and
visualize the key layout for the configuration.

Note the "launch" setting is a macro that will run when you switch to a given screen.
It does not run when the macropad first starts, but it will once you switch from another screen.
See `macros/examples/example.py` for an example of all configuration options.


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

You can also install some initial macros to get started. Copy any of the .py files from the `macros/examples` directory
into `macros/` to start with a pre-built example. Modify the examples to change LED colors, label text, or key/mouse/control
macros as needed. You can also copy-and-paste macros listed in the 
[Macropad Hotkeys II Wiki](https://github.com/deckerego/Macropad_Hotkeys/wiki) then tweak as needed.


## Updating

After you first install this version of Macropad Hotkeys and reboot the Macropad,
the CIRCUITPY filesystem will be mounted as read-only. When mounting the device
as read-only, Windows and MacOS won't complain if you unplug or reboot the device
without unmounting it, making it more like a regular old HID device.

To update or edit the code on the device, or to modify the macros, you first
need to reboot the device with the CIRCUITPY drive mounted in read/write mode.
To do that, reboot the device using the boot switch on the left of the
Macropad, and then after releasing the button immediately hold down the
blinking top-left key on the keypad (KEY1). You should see the text 
"Mounting Read/Write" quickly appear on the screen, and then the CIRCUITPY 
drive will mount in read/write mode.
