class Key:
    RELEASED = 0
    PRESSED  = 1    

    def __init__(self, macropad, command, label='', color=0xF0F0F0):
        self.macropad = macropad
        self.command = command
        self.label = label
        self.color = color
        self.state = Key.RELEASED

    def press(self):
        self.state = Key.PRESSED
        self.command.press(self.state)

    def release(self):
        self.state = Key.RELEASED
        self.command.release(self.state)
