from unittest import mock
from unittest import TestCase
from keys import Keys
from adafruit_hid.keycode import Keycode

class MockKeycode(Keycode):
    MOCK_1 = mock.Mock()

class MockApp:
    def __init__(self):
        self.name = ''
        self.order = 0
        self.launch = None
        self.timeout = 300
        self.macros  = [
            (0x0F0F0F, 'MOCK_1', MockKeycode.MOCK_1),
        ]

class TestKeys(TestCase):
    def test_init(self):
        macropad = mock.Mock()
        app = MockApp()
        keys = Keys(macropad, app)
        
        self.assertEqual(len(keys.keys), 1)
        self.assertEqual(keys.keys[0].color, 0x0F0F0F)
        self.assertEqual(keys.keys[0].command, MockKeycode.MOCK_1)
