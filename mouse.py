class Mouse:
    def __init__(self, keycode):
        self.keycode = keycode

    def press(self, macropad):
        if self.keycode < 0:
            macropad.mouse.release(self.keycode)
        else:
            macropad.mouse.press(self.keycode)

    def release(self, macropad):
        macropad.mouse.release(self.keycode)
