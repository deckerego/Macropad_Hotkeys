class Toolbar:
    def __init__(self, keycode):
        self.keycode = keycode

    def press(self, macropad):
        if self.keycode < 0:
            macropad.consumer_control.release()
        else:
            macropad.consumer_control.press(self.keycode)

    def release(self, macropad):
        macropad.consumer_control.release()
