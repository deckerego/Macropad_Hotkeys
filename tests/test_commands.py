from unittest import TestCase
from keyboard import Keyboard # DEPRECATED switch to command module after 3.x
from pause import Pause       # DEPRECATED switch to command module after 3.x
from mouse import Mouse       # DEPRECATED switch to command module after 3.x
import commands

class TestKey(TestCase):
    def test_alpha(self):
        command = commands.get('O')
        self.assertIsInstance(command, Keyboard)

    def test_float(self):
        command = commands.get(1.0)
        self.assertIsInstance(command, Pause)
    
    def test_mouse(self):
        command = commands.get(Mouse(0))
        self.assertIsInstance(command, Mouse)
