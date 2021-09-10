class Keyboard:
    def __init__(self, key):
        self.key = key

    def press(self, macropad):
        if not isinstance(self.key, int):
            macropad.keyboard_layout.write(self.key)
        elif self.key < 0:
            macropad.keyboard.release(self.key)
        else:
            macropad.keyboard.press(self.key)

    def release(self, macropad):
        if isinstance(self.key, int) and self.key >= 0:
            macropad.keyboard.release(self.key)
