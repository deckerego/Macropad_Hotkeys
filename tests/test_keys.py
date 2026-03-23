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
        self.tick = mock.Mock()
    def register(self, _):
        pass

class TestKeys(TestCase):
    def test_init(self):
        app = MockApp()
        keys = Keys(app)
        keys.addListener(MockListener())
        
        self.assertEqual(len(keys.keys), 17)
        self.assertEqual(keys.keys[0].color, 0x0F0F0F)
        self.assertIsInstance(keys.keys[0].commands, Commands)

    def test_press(self):
        listenerOne = MockListener()
        listenerTwo = MockListener()
        app = MockApp()
        keys = Keys(app)
        keys.addListener(listenerOne)
        keys.addListener(listenerTwo)
        keys.press(0)
        
        listenerOne.pressed.assert_called_once()
        listenerOne.released.assert_not_called()
        listenerTwo.pressed.assert_called_once()
        listenerTwo.released.assert_not_called()

    def test_release(self):
        listenerOne = MockListener()
        listenerTwo = MockListener()
        app = MockApp()
        keys = Keys(app)
        keys.addListener(listenerOne)
        keys.addListener(listenerTwo)
        keys.release(0)
        
        listenerOne.released.assert_called_once()
        listenerOne.pressed.assert_not_called()
        listenerTwo.released.assert_called_once()
        listenerTwo.pressed.assert_not_called()

    def test_no_launch(self):
        listenerOne = MockListener()
        app = MockApp()
        keys = Keys(app)
        keys.addListener(listenerOne)
        keys.press(Keys.KEY_LAUNCH)
        keys.release(Keys.KEY_LAUNCH)

        listenerOne.released.assert_called_once()
        listenerOne.pressed.assert_called_once()

    def test_launch(self):
        listenerOne = MockListener()
        app = MockApp()
        app.launch = 0x000000, None, [],
        keys = Keys(app)
        keys.addListener(listenerOne)
        keys.press(Keys.KEY_LAUNCH)
        keys.release(Keys.KEY_LAUNCH)

        listenerOne.released.assert_called_once()
        listenerOne.pressed.assert_called_once()

    def test_tick_no_frames(self):
        listenerOne = MockListener()
        app = MockApp()
        app.launch = 0x000000, None, [],
        keys = Keys(app)
        keys.addListener(listenerOne)

        keys.tick(0.01)
        listenerOne.tick.assert_not_called()

    def test_tick_one_frame(self):
        listenerOne = MockListener()
        app = MockApp()
        app.launch = 0x000000, None, [],
        keys = Keys(app)
        keys.addListener(listenerOne)

        keys.tick(0.05)
        listenerOne.tick.assert_not_called()

        keys.tick(0.05)
        listenerOne.tick.assert_called_once()

    def test_tick_two_frames(self):
        listenerOne = MockListener()
        app = MockApp()
        app.launch = 0x000000, None, [],
        keys = Keys(app)
        keys.addListener(listenerOne)

        keys.tick(0.05)
        listenerOne.tick.assert_not_called()

        keys.tick(0.15)
        listenerOne.tick.assert_called_once()