from unittest import mock, TestCase
from keys import Keys, Key
from screen import ScreenListener
from commands import Commands, Sleep
from adafruit_display_shapes.rect import Rect

class MockKeys(Keys):
    def __init__(self, listeners, app):
        self.keys = [
            Key(mock.Mock(), "Test01"),
            Key(mock.Mock(), "Test02"),
            Key(mock.Mock(), "Test03"),
            Key(mock.Mock(), "Test04"),
            Key(mock.Mock(), "Test05"),
            Key(mock.Mock(), "Test06"),
            Key(mock.Mock(), "Test07"),
            Key(mock.Mock(), "Test08"),
            Key(mock.Mock(), "Test09"),
            Key(mock.Mock(), "Test10"),
            Key(mock.Mock(), "Test11"),
            Key(mock.Mock(), "Test12"),
            Key(mock.Mock(), "TestButton"),
            Key(mock.Mock(), "TestLeft"),
            Key(mock.Mock(), "TestRight"),
        ]

class MockMacroPad:
    def __init__(self):
        self.display = MockDisplay()

class MockDisplay:
    def __init__(self):
        self.width = 128
        self.height = 64
        self.release_all = mock.Mock()
        self.refresh = mock.Mock()

class TestScreen(TestCase):
    def test_initalize(self):
        macropad = MockMacroPad()
        screen = ScreenListener(macropad)
        screen.initialize()

        elementCount = len(screen.display.root_group)
        self.assertEqual(screen.display.root_group[0].color, 0xFFFFFF)
        self.assertIsInstance(screen.display.root_group[elementCount - 2], Rect)
        self.assertEqual(screen.display.root_group[elementCount - 1].color, 0x000000)

    def test_sleep(self):
        macropad = MockMacroPad()
        screen = ScreenListener(macropad)
        screen.initialize()
        screen.sleep()

        self.assertEqual(len(screen.display.root_group), 0)
        self.assertEqual(screen.display.brightness, 0)

    def test_resume(self):
        macropad = MockMacroPad()
        screen = ScreenListener(macropad)
        screen.initialize()
        screen.sleep()
        screen.resume()

        self.assertEqual(len(screen.display.root_group), 14)
        self.assertEqual(screen.display.brightness, 1)

    def test_highlight(self):
        macropad = MockMacroPad()
        screen = ScreenListener(macropad)
        screen.initialize()
        screen.highlight(1)

        self.assertEqual(screen.display.root_group[0].color, 0xFFFFFF)
        self.assertEqual(screen.display.root_group[0].background_color, 0x000000)
        self.assertEqual(screen.display.root_group[1].color, 0x000000)
        self.assertEqual(screen.display.root_group[1].background_color, 0xFFFFFF)

    def test_reset(self):
        macropad = MockMacroPad()
        screen = ScreenListener(macropad)
        screen.initialize()
        screen.highlight(1)
        screen.reset(1)

        self.assertEqual(screen.display.root_group[0].color, 0xFFFFFF)
        self.assertEqual(screen.display.root_group[0].background_color, 0x000000)
        self.assertEqual(screen.display.root_group[1].color, 0xFFFFFF)
        self.assertEqual(screen.display.root_group[1].background_color, 0x000000)

    def test_title(self):
        macropad = MockMacroPad()
        screen = ScreenListener(macropad)
        screen.initialize()
        screen.group[1].text = "Two"
        screen.setTitle("Title")

        self.assertEqual(screen.group[1].text, 'Two')
        self.assertEqual(screen.group[13].text, 'Title')

    def test_set_keys(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        screen = ScreenListener(macropad)
        screen.initialize()
        screen.register(keys)

        self.assertEqual(screen.group[0].text, 'Test01')
        self.assertEqual(screen.group[1].text, 'Test02')
        self.assertEqual(screen.group[2].text, 'Test03')
        self.assertEqual(screen.group[13].text, '')

    def test_press(self):
        keys = MockKeys([], None)
        class MockScreenListener(ScreenListener):
            highlight = mock.Mock()
            reset = mock.Mock()
        macropad = MockMacroPad()
        screen = MockScreenListener(macropad)
        screen.initialize()
        screen.register(keys)
        screen.pressed(keys, 1)

        screen.highlight.assert_called_once()
        screen.reset.assert_not_called()

    def test_release(self):
        keys = MockKeys([], None)
        class MockScreenListener(ScreenListener):
            highlight = mock.Mock()
            reset = mock.Mock()
        macropad = MockMacroPad()
        screen = MockScreenListener(macropad)
        screen.initialize()
        screen.register(keys)
        screen.released(keys, 1)

        screen.reset.assert_called_once()
        screen.highlight.assert_not_called()

    def test_press_encoder(self):
        keys = MockKeys([], None)
        class MockScreenListener(ScreenListener):
            highlight = mock.Mock()
            reset = mock.Mock()
        macropad = MockMacroPad()
        screen = MockScreenListener(macropad)
        screen.initialize()
        screen.register(keys)

        screen.display.refresh.reset_mock()
        screen.pressed(keys, Keys.KEY_ENC_BUTTON)

        screen.display.refresh.assert_not_called()

    def test_release_encoder(self):
        keys = MockKeys([], None)
        class MockScreenListener(ScreenListener):
            highlight = mock.Mock()
            reset = mock.Mock()
        macropad = MockMacroPad()
        screen = MockScreenListener(macropad)
        screen.initialize()
        screen.register(keys)

        screen.display.refresh.reset_mock()
        screen.released(keys, Keys.KEY_ENC_BUTTON)

        screen.display.refresh.assert_not_called()

    def test_sleep(self):
        keys = MockKeys([], None)
        keys[0].commands = Commands(Sleep())
        class MockScreenListener(ScreenListener):
            highlight = mock.Mock()
            reset = mock.Mock()
            sleep = mock.Mock()
        macropad = MockMacroPad()
        screen = MockScreenListener(macropad)
        screen.initialize()
        screen.register(keys)
        screen.pressed(keys, 0)

        screen.sleep.assert_called_once()
