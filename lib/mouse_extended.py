from adafruit_hid.mouse import Mouse as MouseBasic

try:
    from typing import Optional, Sequence
    import usb_hid # type: ignore (part of CircuitPython standard libs)
except ImportError:
    pass

class Mouse(MouseBasic):
    WHEEL = 0x118
    PAN = 0x119
    
    def __init__(self, devices: Sequence[usb_hid.Device], timeout: Optional[int] = None) -> None:
        super().__init__(devices, timeout)
        self.report = bytearray(7)

    # See also:
    # https://github.com/s117/Adafruit_CircuitPython_HID/blob/feature/better_mouse_forwarding/adafruit_hid/mouse.py
    def move(self, x: int = 0, y: int = 0, wheel: int = 0, pan: int = 0) -> None:
            while x != 0 or y != 0 or wheel != 0 or pan != 0:
                partial_x = self._limit_i16(x)
                partial_y = self._limit_i16(y)
                partial_wheel = self._limit_i8(wheel)
                partial_pan = self._limit_i8(pan)
                self.report[1] = partial_x & 0xFF
                self.report[2] = (partial_x >> 8) & 0xFF
                self.report[3] = partial_y & 0xFF
                self.report[4] = (partial_y >> 8) & 0xFF
                self.report[5] = partial_wheel & 0xFF
                self.report[6] = partial_pan & 0xFF
                self._mouse_device.send_report(self.report, 0x82)
                x -= partial_x
                y -= partial_y
                wheel -= partial_wheel
                pan -= partial_pan

    def _send_no_move(self, ex: bool = True) -> None:
        self.report[1] = 0
        self.report[2] = 0
        self.report[3] = 0
        self.report[4] = 0
        self.report[5] = 0
        self.report[6] = 0
        if ex:
            self._mouse_device.send_report(self.report, 0x82)
        else:
            self._mouse_device.send_report(self.report[:4])

    @staticmethod
    def _limit_i16(dist: int) -> int:
        return min(32767, max(-32767, dist))