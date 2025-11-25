class Toolbar:
    def __init__(self, keycode):
        self.keycode = keycode

    def press(self, state):
        if self.keycode < 0:
            state["macropad"].consumer_control.release()
        else:
            state["macropad"].consumer_control.press(self.keycode)

    def release(self, state):
        state["macropad"].consumer_control.release()
