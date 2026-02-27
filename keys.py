from commands import Commands
from enum import Enum

class Key:
    def __init__(self, macro, label='', color=0xF0F0F0):
        self.commands = Commands(macro)
        self.label = label
        self.color = color    

class Keys:
    listeners = []
    keys = []
    app = None

    def __init__(self, app):
        self.app = app
        
        self.keys = []
        for i in range(len(self.app.macros)):
            color, label, macro = self.app.macros[i]
            self.keys += [Key(macro, label, color)]

    def __del__(self):
        self.listeners.clear()
        self.keys.clear()
        self.app = None

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
