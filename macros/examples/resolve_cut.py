# MACROPAD Hotkeys: DaVinci Resolve Cut Page

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from consumer import Toolbar
from sleep import Sleep

app = {
    'name' : 'DV Resolve [Cut]',
    'order': 0,
    'launch': 
        (0x000000, None, [Keycode.LEFT_SHIFT, Keycode.THREE]),
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x663F00, 'Vol -', Toolbar(ConsumerControlCode.VOLUME_DECREMENT)),
        (0x660556, 'Mute', Toolbar(ConsumerControlCode.MUTE)),
        (0x663F00, 'Vol +', Toolbar(ConsumerControlCode.VOLUME_INCREMENT)),
        # 2nd row ----------
        (0x663F00, '<<', 'j'),
        (0x660556, '>||', Keycode.SPACE),
        (0x663F00, '>>', 'l' ),
        # 3rd row ----------
        (0x663F00, 'Prev', Keycode.UP_ARROW),
        (0x660556, ' [*] ', 'k'),
        (0x663F00, 'Next', Keycode.DOWN_ARROW),
        # 4th row ----------
        (0x663F00, 'In', 'i'),
        (0x660556, 'Clear', 'x'),
        (0x663F00, 'Out', 'o'),
        # Rotary Encoder ---
        (0x000000, None, Sleep()),
        (0x000000, None, [Keycode.LEFT_SHIFT, Keycode.LEFT_ARROW], [Keycode.LEFT_SHIFT, Keycode.LEFT_ARROW], [Keycode.LEFT_SHIFT, Keycode.LEFT_ARROW]),
        (0x000000, None, [Keycode.LEFT_SHIFT, Keycode.RIGHT_ARROW], [Keycode.LEFT_SHIFT, Keycode.RIGHT_ARROW], [Keycode.LEFT_SHIFT, Keycode.RIGHT_ARROW]),
    ]
}
