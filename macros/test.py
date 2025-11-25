# MACROPAD Hotkeys: Test Hotkey Scenarios

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from consumer import Toolbar

app = {
    'name' : 'Test',
    'order': 0,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x540908, 'Hello  ', [[Keycode.SHIFT, Keycode.H], [Keycode.E, Keycode.L, Keycode.L], Keycode.O]),
        (0x544408, 'World  ', [[Keycode.SHIFT, Keycode.W], 2.0, Keycode.O, 1.0, [Keycode.R, Keycode.L], 3.0, Keycode.D]),
        (0x04541B, 'o      ', Keycode.O),
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
