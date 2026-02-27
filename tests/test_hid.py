from unittest import mock, TestCase
from keys import Keys, Key
from hid import InputDeviceListener

class MockKeys(Keys):
    def __init__(self, listeners, app):
        self.keys = [
            Key(mock.Mock(), "", 0x0000FF),
            Key(mock.Mock(), "", 0x00FF00),
            Key(mock.Mock(), "", 0xFF0000),
        ]

class MockMacroPad:
    def __init__(self):
        self.keyboard = MockKeyboard()
        self.keyboard_layout = MockKeyboardLayout()

class MockKeyboard:
    press = mock.Mock()
    release = mock.Mock()
    release_all = mock.Mock()

class MockKeyboardLayout:
    write = mock.Mock()

class TestInputDevice(TestCase):
    def test_init_keyboard(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)

        macropad.keyboard.release_all.assert_called_once()        

    def test_press_keyboard(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.pressed(keys, 1)

        macropad.keyboard.press.assert_called_once()
        macropad.keyboard.release.assert_never_called()

    def test_release_keyboard(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.released(keys, 1)

        macropad.keyboard.release.assert_called_once()
        macropad.keyboard.press.assert_never_called()
