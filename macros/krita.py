# MACROPAD Hotkeys example: Krita for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.mouse import Mouse

app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Krita', # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0E0007, 'Undo', [Keycode.CONTROL, 'z']),
        (0x0E0007, 'Redo', [Keycode.CONTROL, Keycode.SHIFT, 'Z']),
        (0x0E0007, 'Brush', 'b'),     # Brush
        # 2nd row ----------

        (0x0E0007, 'Swap', 'x'),  # Swap
        (0x0E0007, 'Mirror', 'm'), # Mirror image
        (0x0E0007, 'Eraser', 'e'),    # Erase toggle
        # 3rd row ----------
        (0x002000, 'Pallete', [{'buttons':Mouse.RIGHT_BUTTON}]), # Pallete
        (0x0E0007, 'Move', 't'),  # Move
        (0x0E0007, 'Select', 's'),  # Select Freehand
        # 4th row ----------
        (0x0E0007, 'Brush- ', '['),   # Brush decrease
        (0x0E0007, 'Brush+ ', ']'), # Brush increase
        (0x0E0007, 'Sample', 'p'),    # Sample
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.SHIFT, 'S']) # Save As
    ]
}
