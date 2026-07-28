import time

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard


def main(configuration):
    """Run as a keyboard using the given configuration

    :param configuration: Mapping of hardware pin to keycode
    :type configuration: dict[board.Pin, adafruit_hid.keycode.Keycode]
    """

    keypress_pins = [pin for pin in configuration.keys()]

    # Setup the keyboard
    time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
    keyboard = Keyboard(usb_hid.devices)

    digital_io_to_pins = {}
    key_pins = []
    # Configure the pins
    for i, pin in enumerate(keypress_pins):
        key_pin = digitalio.DigitalInOut(pin)
        key_pin.direction = digitalio.Direction.INPUT
        key_pin.pull = digitalio.Pull.UP
        digital_io_to_pins[i] = pin
        key_pins.append((i, key_pin))

    # Configure the LED to give feedback
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT

    pressed = set()

    while True:
        for i, key_pin in key_pins:
            if not key_pin.value:  # Is it grounded?
                if i in pressed:
                    continue
                led.value = True
                pressed.add(i)
                pin = digital_io_to_pins[i]
                keycode = configuration[pin]
                keyboard.press(keycode)
            elif key_pin.value:
                if i in pressed:
                    pin = digital_io_to_pins[i]
                    keycode = configuration[pin]
                    keyboard.release(keycode)
                    led.value = False
                    pressed.remove(i)
