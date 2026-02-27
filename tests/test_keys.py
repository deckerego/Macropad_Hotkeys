from unittest import mock
from unittest import TestCase
from keys import Keys, Key
from adafruit_hid.keycode import Keycode
from keyboard import Keyboard # pyright: ignore[reportMissingImports, reportMissingModuleSource] Switch to command module after 3.x

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

class MockCommand:
    def __init__(self):
        self.press = mock.Mock()
        self.release = mock.Mock()

class TestKeys(TestCase):
    def test_init(self):
        macropad = mock.Mock()
        app = MockApp()
        keys = Keys(macropad, app)
        
        self.assertEqual(len(keys.keys), 1)
        self.assertEqual(keys.keys[0].color, 0x0F0F0F)
        self.assertIsInstance(keys.keys[0].command, Keyboard)

class TestKey(TestCase):
    def test_press(self):
        macropad = mock.Mock()
        command = MockCommand()
        color = (0, 0, 0)
        key = Key(macropad, command, color)

        key.press()
        
        command.press.assert_called_once()
        command.release.assert_not_called()

    def test_release(self):
        macropad = mock.Mock()
        command = MockCommand()
        color = (0, 0, 0)
        key = Key(macropad, command, color)

        key.release()
        
        command.press.assert_not_called()
        command.release.assert_called_once()
