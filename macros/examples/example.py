# MACROPAD Hotkeys: Sample of a full configuration with all options

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.mouse import Mouse as MouseCode

from consumer import Toolbar
from mouse import Mouse
from sleep import Sleep
from midi import Midi

app = {
    'name' : 'Example Macro',
    'order': 0,
    'launch': 
        (0x000000, None, [Keycode.SHIFT]),
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x540908, 'Hello  ', [[Keycode.SHIFT, Keycode.H], [Keycode.E, Keycode.L, Keycode.L], Keycode.O]),
        (0x544408, 'World  ', [[Keycode.SHIFT, Keycode.W], 2.0, Keycode.O, 1.0, [Keycode.R, Keycode.L], 3.0, Keycode.D]),
        (0x04541B, 'o      ', Keycode.O),
        # 2nd row ----------
        (0x095E06, '< Tab  ', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x000000, '',     []),
        (0x095E06, 'Tab >  ', [Keycode.CONTROL, Keycode.TAB]),
        # 3rd row ----------
        (0x000754, 'LeftBtn', Mouse(MouseCode.LEFT_BUTTON)),
        (0x540908, 'MidBtn ', Mouse(MouseCode.MIDDLE_BUTTON)),
        (0x000754, 'RghtBtn', Mouse(MouseCode.RIGHT_BUTTON)),
        # 4th row ----------
        (0x540908, 'Bass',    Midi(35)),
        (0x540908, 'Kick',    Midi(36)),
        (0x04541B, 'Cowbell', Midi(56)),
        # Rotary Encoder ---
        (0x000000, None, Sleep()),
        (0x000000, None, Toolbar(ConsumerControlCode.VOLUME_DECREMENT)),
        (0x000000, None, Toolbar(ConsumerControlCode.VOLUME_INCREMENT)),
    ]
}
