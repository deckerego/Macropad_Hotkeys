import time

class Sleep:
    def __init__(self):
        pass

    def press(self, state):
        if state["sleeping"]:
            state["screen"].resume()
            state["pixels"].resume()
        else:
            state["screen"].sleep()
            state["pixels"].sleep()
        state["sleeping"] = not state["sleeping"]

    def release(self, state):
        pass
