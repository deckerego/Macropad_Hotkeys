class Key:
    RELEASED = 0
    PRESSED  = 1    

    def __init__(self, macropad, command, color):
        self.macropad = macropad
        self.command = command
        self.color = color
        self.state = Key.RELEASED

    def press(self):
        self.state = Key.PRESSED
        self.command.press(self.state)

    def release(self):
        self.state = Key.RELEASED
        self.command.release(self.state)
