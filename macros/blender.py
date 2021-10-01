# MACROPAD Hotkeys: Blender

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Blender',
    'order': 1,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0A3B66, 'Top   ', [Keycode.KEYPAD_SEVEN]),
        (0x663F00, 'Rot/\\ ', [Keycode.KEYPAD_EIGHT]),
        (0x000000, '      ', [Keycode.KEYPAD_NINE]),
        # 2nd row ----------
        (0x663F00, 'Rot < ', [Keycode.KEYPAD_FOUR]),
        (0x660556, 'Persp ', [Keycode.KEYPAD_FIVE]),
        (0x663F00, 'Rot > ', [Keycode.KEYPAD_SIX]),
        # 3rd row ----------
        (0x0A3B66, 'Front ', [Keycode.KEYPAD_ONE]),
        (0x663F00, 'Rot\/ ', [Keycode.KEYPAD_TWO]),
        (0x0A3B66, 'Side  ', [Keycode.KEYPAD_THREE]),
        # 4th row ----------
        (0x660556, 'Camera', [Keycode.KEYPAD_ZERO]),
        (0x20660A, 'Zoom +', [Keycode.KEYPAD_PLUS]),
        (0x20660A, 'Zoom -', [Keycode.KEYPAD_MINUS])
    ]
}
