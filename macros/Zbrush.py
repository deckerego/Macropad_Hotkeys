# MACROPAD Hotkeys example: Krita for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.mouse import Mouse

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Zbrush', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0E0007, 'Undo', [Keycode.CONTROL, 'z']),
        (0x0E0007, 'Redo', [Keycode.CONTROL, Keycode.SHIFT, 'Z']),
        (0x000080, 'Brush', 'b'),  # Brush
        # 2nd row ----------
        (0x0E0007, 'Draw', 'q'),  #
        (0x0E0007, 'Move', 'w'), #
        (0x0E0007, 'PFrame', [Keycode.SHIFT, 'F']),    # Poly Frame
        # 3rd row ----------
        (0x000080, 'Pallete', [{'buttons':Mouse.RIGHT_BUTTON}]), # Pallete
        (0x0E0007, 'DSize', 's'),  # Draw Size
        (0x0E0007, 'ZInten', 'u'),  # Z Intensity
        # 4th row ----------
        (0x990000, 'Shift', [Keycode.SHIFT, '']),  # Shift
        (0x990000, 'Ctrl', [Keycode.CONTROL, '']),  # Ctrl
        (0x990000, 'Alt', [Keycode.ALT, '']),  # Alt
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.SHIFT, 'S']) # Save As
    ]
}
