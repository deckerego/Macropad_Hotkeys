import board
import digitalio
import storage

# Mount the CIRCUITPY drive as read-only unless
# the encoder switch is held down
encoder_switch = digitalio.DigitalInOut(board.BUTTON)
encoder_switch.switch_to_input(pull=digitalio.Pull.UP)
if(encoder_switch.value):
    print("Mounting Read-Only")
else:
    print("Mounting Read/Write")
storage.remount("/", not encoder_switch.value)
