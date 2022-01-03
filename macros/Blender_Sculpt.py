# MACROPAD Hotkeys example: Krita for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.mouse import Mouse

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Blender Sculpt', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0E0007, 'Undo', [Keycode.CONTROL, 'z']),
        (0x0E0007, 'Redo', [Keycode.CONTROL, Keycode.SHIFT, 'Z']),
        (0x0E0007, 'B Set', [{'buttons':Mouse.RIGHT_BUTTON}]),     #
        # 2nd row ----------

        (0x0E0007, '----', ''),  #
        (0x0E0007, '----', ''), #
        (0x0E0007, 'Favs', 'q'),  # Quick Favs
        # 3rd row ----------
        (0x002663, 'Mask', [Keycode.CONTROL, Keycode.SHIFT, [{'buttons':Mouse.LEFT_BUTTON}]] ), # Mask Lasso
        (0x002663, 'Mask P', 'a'),  # Mask settings
        (0x002663, 'Mask C', [Keycode.ALT, 'm']),  # Mask clear
        # 4th row ----------
         (0x990000, 'Shift', [Keycode.SHIFT, '']),  # Shift
        (0x990000, 'Ctrl', [Keycode.CONTROL, '']),  # Ctrl
        (0x990000, 'Alt', [Keycode.ALT, '']),  # Alt
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.SHIFT, 'S']) # Save As
    ]
}
