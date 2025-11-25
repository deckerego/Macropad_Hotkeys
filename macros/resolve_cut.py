# MACROPAD Hotkeys: DaVinci Resolve Cut Page

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'DV Resolve [Cut]',
    'order': 0,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '<<', 'j'),
        (0x000000, '>||', 'k'),
        (0x000000, '>>', 'l' ),
        # 2nd row ----------
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        # 3rd row ----------
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        # 4th row ----------
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        # Rotary Encoder ---
        (0x000000, None, []),
        (0x000000, None, [Keycode.LEFT_SHIFT, Keycode.LEFT_ARROW]),
        (0x000000, None, [Keycode.LEFT_SHIFT, Keycode.RIGHT_ARROW]),
    ]
}
