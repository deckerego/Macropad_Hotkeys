# MACROPAD Hotkeys: No Man's Sky

from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse as MouseCode
from mouse import Mouse

app = {
    'name' : 'No Man\'s Sky',
    'order': 4,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x544408, 'G Map', [Keycode.M]),
        (0x000000, 'Boost', [Keycode.LEFT_SHIFT]),
        (0x540908, 'Pulse', [Keycode.SPACE]),
        # 2nd row ----------
        (0x000754, 'Prev ', [Keycode.PERIOD]),
        (0x540908, 'Target', [Mouse(MouseCode.MIDDLE_BUTTON)]),
        (0x000754, 'Next ', [Keycode.COMMA]),
        # 3rd row ----------
        (0x080F54, 'Scan ', [Keycode.C]),
        (0x080F54, 'Light', [Keycode.T]),
        (0x080F54, 'HUD  ', [Keycode.H]),
        # 4th row ----------
        (0x095E06, 'Quick', [Keycode.X]),
        (0x000000, '     ', []),
        (0x095E06, 'Build', [Keycode.Z])
    ]
}
