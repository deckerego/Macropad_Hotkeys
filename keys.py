from commands import Commands
from enum import Enum

class Key:
    def __init__(self, macro, label='', color=0xF0F0F0):
        self.commands = Commands(macro)
        self.label = label
        self.color = color    

class Keys:
    LAUNCH = -1
    ENC_BUTTON = 12
    ENC_LEFT = 13
    ENC_RIGHT = 14
    MAX_LEDS = 12
    listeners = []

    def __init__(self, listeners, app):
        self.listeners = listeners
        self.app = app
        self.keys = []
        for i in range(len(self.app.macros)):
            color, label, macro = self.app.macros[i]
            self.keys += [Key(macro, label, color)]

    def __del__(self):
        self.listeners.clear()
        self.keys.clear()
        self.app = None

    def press(self, key_index):
        for listener in self.listeners:
            listener.pressed(self.keys[key_index])

    def release(self, key_index):
        for listener in self.listeners:
            listener.released(self.keys[key_index])
