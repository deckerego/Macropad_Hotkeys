import time

class Pause:
    def __init__(self, seconds):
        self.seconds = seconds

    def press(self, state):
        time.sleep(self.seconds)

    def release(self, state):
        pass
