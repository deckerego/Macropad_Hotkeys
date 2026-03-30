from commands import Commands, Sleep
import time

class Key:
    def __init__(self, macro, label='', color=0xF0F0F0):
        self.commands = Commands(macro)
        self.label = label
        self.color = color    

class Keys:
    KEY_ENC_BUTTON = 12 # Virtual key for encoder press
    KEY_ENC_LEFT   = 13 # Virtual key for encoder rotation left
    KEY_ENC_RIGHT  = 14 # Virtual key for encoder rotation right
    KEY_LAUNCH     = 15 # Hidden key for launching a new page
    KEY_SLEEP      = 16 # Hidden key for sleeping
    
    listeners = None
    keys = None
    tick_count = None

    def __init__(self, app):
        self.keys = [None] * 17
        self.listeners = []

        for i in range(len(app.macros)):
            color, label, macro = app.macros[i]
            self.keys[i] = Key(macro, label, color)

        self.keys[Keys.KEY_LAUNCH] = Key(app.launch[2]) if app.launch else Key([])
        self.keys[Keys.KEY_SLEEP] = Key(Sleep())

        self.tick_count = 0

    def __del__(self):
        if self.listeners: self.listeners.clear()
        if self.keys: self.keys.clear()

    def __bool__(self):
        return len(self.keys) > 0
    
    def __iter__(self):
        return iter(self.keys)

    def __getitem__(self, index):
        return self.keys[index]

    def __len__(self):
        return len(self.keys)

    def addListener(self, listener):
        self.listeners += [listener]
        listener.register(self)

    def press(self, key_index):
        for listener in self.listeners:
            listener.pressed(self.keys, key_index)

    def release(self, key_index):
        for listener in self.listeners:
            listener.released(self.keys, key_index)

    def tick(self, elapsed_seconds):
        self.tick_count += elapsed_seconds
        frames = int(self.tick_count / 0.1)
        if frames >= 1:
            self.tick_count = 0
            for listener in self.listeners:
                listener.tick(self.keys, frames)
