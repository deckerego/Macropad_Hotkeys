import time

class Sleep:
    def __init__(self, seconds):
        self.seconds = seconds

    def press(self, macropad):
        time.sleep(self.seconds)

    def release(self, macropad):
        pass
