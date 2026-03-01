class MacroPad:
    def __init__(self):
        self.keyboard = Keyboard()
        self.encoder_switch_debounced = EncoderSwitch() 
        self.display = Display()

class Display:
    def __init__(self):
        self.width = 0
        self.height = 0

    def release_all(self):
        pass
    
    def refresh(self):
        pass

class Keyboard:
    def __init__(self):
        pass

    def release_all(self):
        pass

class EncoderSwitch:
    def __init__(self):
        pass
    
    def update(self):
        pass