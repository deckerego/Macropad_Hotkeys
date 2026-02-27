from unittest import mock, TestCase
from keys import Keys, Key
from hid import InputDeviceListener
from commands import Toolbar, Mouse
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.mouse import Mouse as MouseCode

class MockKeys(Keys):
    def __init__(self, listeners, app):
        self.keys = [
            Key('A'),
            Key(Keycode.A),
            Key([Keycode.A, Keycode.B]),
            Key([[Keycode.SHIFT, Keycode.A]]),
            Key(Toolbar(ConsumerControlCode.VOLUME_DECREMENT)),
            Key(Mouse(MouseCode.LEFT_BUTTON)),
        ]

class MockMacroPad:
    def __init__(self):
        self.keyboard = MockKeyboard()
        self.keyboard_layout = MockKeyboardLayout()
        self.consumer_control = MockConsumerControl()
        self.mouse = MockMouse()

class MockKeyboard:
    def __init__(self):
        self.press = mock.Mock()
        self.release = mock.Mock()
        self.release_all = mock.Mock()

class MockKeyboardLayout:
    def __init__(self):
        self.write = mock.Mock()

class MockConsumerControl:
    def __init__(self):
        self.press = mock.Mock()
        self.release = mock.Mock()

class MockMouse:
    def __init__(self):
        self.press = mock.Mock()
        self.release = mock.Mock()

class TestInputDevice(TestCase):
    def test_init_keyboard(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)

        macropad.keyboard.release_all.assert_called_once()        

    def test_press_alpha(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.pressed(keys, 0)

        macropad.keyboard_layout.write.assert_called_once()
        macropad.keyboard.press.assert_not_called()
        macropad.keyboard.release.assert_not_called()

    def test_release_alpha(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.released(keys, 0)

        macropad.keyboard_layout.write.assert_not_called()
        macropad.keyboard.release.assert_not_called()
        macropad.keyboard.press.assert_not_called()

    def test_press_keycode(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.pressed(keys, 1)

        macropad.keyboard.press.assert_called_once()
        macropad.keyboard.release.assert_not_called()

    def test_release_keycode(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.released(keys, 1)

        macropad.keyboard.release.assert_called_once()
        macropad.keyboard.press.assert_not_called()

    def test_press_toolbar(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.pressed(keys, 4)

        macropad.consumer_control.press.assert_called_once()
        macropad.consumer_control.release.assert_not_called()
        macropad.keyboard.press.assert_not_called()
        macropad.keyboard.release.assert_not_called()

    def test_release_toolbar(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.released(keys, 4)

        macropad.consumer_control.release.assert_called_once()
        macropad.consumer_control.press.assert_not_called()
        macropad.keyboard.release.assert_not_called()
        macropad.keyboard.press.assert_not_called()

    def test_press_mouse(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.pressed(keys, 5)

        macropad.mouse.press.assert_called_once()
        macropad.mouse.release.assert_not_called()

    def test_release_mouse(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.released(keys, 5)

        macropad.mouse.release.assert_called_once()
        macropad.mouse.press.assert_not_called()

    def test_press_sequence(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.pressed(keys, 3)

        macropad.keyboard.press.assert_has_calls([mock.call(0xE1), mock.call(0x04)])
        macropad.keyboard.release.assert_has_calls([mock.call(0xE1), mock.call(0x04)])

    def test_release_sequence(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.released(keys, 3)

        macropad.keyboard.release.assert_not_called()
        macropad.keyboard.press.assert_not_called()

    def test_press_series(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.pressed(keys, 2)

        macropad.keyboard.press.assert_has_calls([mock.call(0x04), mock.call(0x05)])
        macropad.keyboard.release.assert_not_called()

    def test_release_series(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.released(keys, 2)

        macropad.keyboard.release.assert_has_calls([mock.call(0x04), mock.call(0x05)])
        macropad.keyboard.press.assert_not_called()
