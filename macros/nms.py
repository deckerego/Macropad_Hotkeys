# MACROPAD Hotkeys: No Man's Sky

from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

app = {
    'name' : 'No Man\'s Sky',
    'order': 4,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004166, 'G Map', [Keycode.M]),
        (0x004166, '     ', []),
        (0x004166, 'Pulse', [Keycode.SPACE]),
        # 2nd row ----------
        (0x004166, 'Prev ', [Keycode.PERIOD]),
        (0x004166, '     ', []), # Needs to be Mouse.MIDDLE_BUTTON
        (0x004166, 'Next ', [Keycode.COMMA]),
        # 3rd row ----------
        (0x004166, 'Scan ', [Keycode.C]),
        (0x004166, 'Visor', [Keycode.F]),
        (0x004166, 'HUD  ', [Keycode.H]),
        # 4th row ----------
        (0x004166, 'Quick', [Keycode.X]),
        (0x640A66, '     ', []),
        (0x663F0A, 'Build', [Keycode.Z])
    ]
}
