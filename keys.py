from commands import Commands, Sleep

class Key:
    def __init__(self, macro, label='', color=0xF0F0F0):
        self.commands = Commands(macro)
        self.label = label
        self.color = color    

class Keys:
    KEY_ENC_BUTTON = 12 # Virtual key for encoder press
    KEY_ENC_LEFT   = 13 # Virtual key for encoder rotation left
    KEY_ENC_RIGHT  = 14 # Virtual key for encoder rotation right
    KEY_SLEEP      = 15 # Hidden key for sleeping
    
    listeners = []
    keys = []
    app = None

    def __init__(self, app):
        self.app = app
        
        self.keys = [None] * 16
        for i in range(len(self.app.macros)):
            color, label, macro = self.app.macros[i]
            self.keys[i] = Key(macro, label, color)
        self.keys[15] = Key(Sleep())

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
