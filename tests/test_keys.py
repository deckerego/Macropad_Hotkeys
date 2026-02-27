from unittest import TestCase, mock
from keys import Keys
from adafruit_hid.keycode import Keycode
from commands import Commands

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

class MockListener:
    def __init__(self):
        self.pressed = mock.Mock()
        self.released = mock.Mock()

class TestKeys(TestCase):
    def test_init(self):
        listeners = [MockListener()]
        app = MockApp()
        keys = Keys(listeners, app)
        
        self.assertEqual(len(keys.keys), 1)
        self.assertEqual(keys.keys[0].color, 0x0F0F0F)
        self.assertIsInstance(keys.keys[0].commands, Commands)

    def test_press(self):
        listenerOne = MockListener()
        listenerTwo = MockListener()
        app = MockApp()
        keys = Keys([listenerOne, listenerTwo], app)
        keys.press(0)
        
        listenerOne.pressed.assert_called_once()
        listenerOne.released.assert_not_called()
        listenerTwo.pressed.assert_called_once()
        listenerTwo.released.assert_not_called()

    def test_release(self):
        listenerOne = MockListener()
        listenerTwo = MockListener()
        app = MockApp()
        keys = Keys([listenerOne, listenerTwo], app)
        keys.release(0)
        
        listenerOne.released.assert_called_once()
        listenerOne.pressed.assert_not_called()
        listenerTwo.released.assert_called_once()
        listenerTwo.pressed.assert_not_called()
