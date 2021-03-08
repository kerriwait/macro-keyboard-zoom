import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Keyboard definition
keyboard = Keyboard(usb_hid.devices)

# Pin definitions
btn_change_pin = board.GP28
btn_mic_pin = board.GP0
btn_video_pin = board.GP14
btn_mode_pin = board.GP15

# Pin setup
btn_change = digitalio.DigitalInOut(btn_change_pin)
btn_change.direction = digitalio.Direction.INPUT
btn_change.pull = digitalio.Pull.DOWN

btn_mic = digitalio.DigitalInOut(btn_mic_pin)
btn_mic.direction = digitalio.Direction.INPUT
btn_mic.pull = digitalio.Pull.DOWN

btn_video = digitalio.DigitalInOut(btn_video_pin)
btn_video.direction = digitalio.Direction.INPUT
btn_video.pull = digitalio.Pull.DOWN

btn_mode = digitalio.DigitalInOut(btn_mode_pin)
btn_mode.direction = digitalio.Direction.INPUT
btn_mode.pull = digitalio.Pull.DOWN

# Windows/Mac toggle, defaults to Mac
mac = True

# Check for button presses
while True:
    if btn_change.value:
        if mac:
            keyboard.press(Keycode.COMMAND, Keycode.TAB)
            time.sleep(0.1)
            keyboard.release(Keycode.COMMAND, Keycode.TAB)
        else:
            keyboard.press(Keycode.ALT, Keycode.TAB)
            time.sleep(0.1)
            keyboard.release(Keycode.ALT, Keycode.TAB)
        time.sleep(0.25)
    if btn_mic.value:
        if mac:
            keyboard.press(Keycode.COMMAND, Keycode.SHIFT, Keycode.A)
            time.sleep(0.1)
            keyboard.release(Keycode.COMMAND, Keycode.SHIFT, Keycode.A)
        else:
            keyboard.press(Keycode.ALT, Keycode.A)
            time.sleep(0.1)
            keyboard.release(Keycode.ALT, Keycode.A)
        time.sleep(0.25)
    if btn_video.value:
        if mac:
            keyboard.press(Keycode.COMMAND, Keycode.SHIFT, Keycode.V)
            time.sleep(0.1)
            keyboard.release(Keycode.COMMAND, Keycode.SHIFT, Keycode.V)
        else:
            keyboard.press(Keycode.ALT, Keycode.V)
            time.sleep(0.1)
            keyboard.release(Keycode.ALT, Keycode.V)
        time.sleep(0.25)
    if btn_mode.value:
        mac = not mac
        time.sleep(0.25)

    time.sleep(0.1)
    
