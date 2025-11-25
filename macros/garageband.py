# MACROPAD Hotkeys: GarageBand Hotkeys

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from consumer import Toolbar

app = {
    'name' : 'GarageBand',
    'order': 6,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x034E59, 'Score',     Keycode.N),
        (0x000754, 'Smart Ctl', Keycode.B),
        (0x4F0354, 'Roll',      Keycode.P),
        # 2nd row ----------
        (0x04541B, 'Begin', Keycode.ENTER                ),
        (0x540908, 'Rec',   Keycode.R                    ),
        (0x544408, 'End',   Keycode.OPTION, Keycode.ENTER),
        # 3rd row ----------
        (0x04541B, 'Back',       Keycode.COMMA   ),
        (0x5E143E, 'Play/Pause', Keycode.SPACEBAR),
        (0x544408, 'Fwd',        Keycode.PERIOD  ),
        # 4th row ----------
        (0x080F54, 'Vol-', Toolbar(ConsumerControlCode.VOLUME_DECREMENT)),
        (0x000000, '',     []),
        (0x080F54, 'Vol+', Toolbar(ConsumerControlCode.VOLUME_INCREMENT)),
        # Rotary Encoder ---
        (0x000000, None, Sleep()),
        (0x000000, None, Toolbar(ConsumerControlCode.VOLUME_DECREMENT)),
        (0x000000, None, Toolbar(ConsumerControlCode.VOLUME_INCREMENT)),
    ]
}
