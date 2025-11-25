class Mouse:
    def __init__(self, keycode):
        self.keycode = keycode

    def press(self, state):
        if self.keycode < 0:
            state["macropad"].mouse.release(self.keycode)
        else:
            state["macropad"].mouse.press(self.keycode)

    def release(self, state):
        state["macropad"].mouse.release(self.keycode)
