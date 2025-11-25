# MACROPAD Hotkeys: Drum Kit
# https://en.wikipedia.org/wiki/General_MIDI#Percussion

from midi import Midi

app = {
    'name' : 'Drum Kit',
    'order': 3,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x544408, 'HatFot', Midi(44)),
        (0x544408, 'HatCls', Midi(42)),
        (0x544408, 'HatOpn', Midi(46)),
        # 2nd row ----------
        (0x04541B, 'XStick', Midi(37)),
        (0x095E06, 'Snare',  Midi(38)),
        (0x04541B, 'Rod',    Midi(91)),
        # 3rd row ----------
        (0x000754, 'FlorTom', Midi(43)),
        (0x000754, 'LowTom',  Midi(47)),
        (0x000754, 'HiTom',   Midi(48)),
        # 4th row ----------
        (0x540908, 'Bass',    Midi(35)),
        (0x540908, 'Kick',    Midi(36)),
        (0x04541B, 'Cowbell', Midi(56)),
        # Rotary Encoder ---
        (0x000000, None, Sleep()),
        (0x000000, None, []),
        (0x000000, None, []),
    ]
}
