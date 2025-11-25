class Keyboard:
    def __init__(self, key):
        self.key = key

    def press(self, state):
        macropad = state["macropad"]
        if not isinstance(self.key, int):
            macropad.keyboard_layout.write(self.key)
        elif self.key < 0:
            macropad.keyboard.release(self.key)
        else:
            macropad.keyboard.press(self.key)

    def release(self, state):
        if isinstance(self.key, int) and self.key >= 0:
            state["macropad"].keyboard.release(self.key)
