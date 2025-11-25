# MACROPAD Hotkeys: DaVinci Resolve Edit Page

from adafruit_hid.keycode import Keycode
from sleep import Sleep

app = {
    'name' : 'DV Resolve [Edit]',
    'order': 1,    
    'launch': 
        (0x000000, None, [Keycode.LEFT_SHIFT, Keycode.FOUR]),
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x2D2D4E, '- ', [Keycode.COMMAND, '-']),
        (0x0D0E50, 'Zoom', [Keycode.LEFT_SHIFT, 'z']),
        (0x2D2D4E, ' +', [Keycode.COMMAND, '=']),
        # 2nd row ----------
        (0x5BA004, '<<', 'j'),
        (0x0D0E50, '>||', Keycode.SPACE),
        (0x5BA004, '>>', 'l' ),
        # 3rd row ----------
        (0x5BA004, 'Prev', Keycode.UP_ARROW),
        (0x0D0E50, ' [*] ', 'k'),
        (0x5BA004, 'Next', Keycode.DOWN_ARROW),
        # 4th row ----------
        (0xF2CB05, 'In', 'i'),
        (0xA52226, 'Clear', 'x'),
        (0xF2CB05, 'Out', 'o'),
        # Rotary Encoder ---
        (0x000000, None, Sleep()),
        (0x000000, None, [Keycode.LEFT_SHIFT, Keycode.LEFT_ARROW], [Keycode.LEFT_SHIFT, Keycode.LEFT_ARROW], [Keycode.LEFT_SHIFT, Keycode.LEFT_ARROW]),
        (0x000000, None, [Keycode.LEFT_SHIFT, Keycode.RIGHT_ARROW], [Keycode.LEFT_SHIFT, Keycode.RIGHT_ARROW], [Keycode.LEFT_SHIFT, Keycode.RIGHT_ARROW]),
    ]
}
