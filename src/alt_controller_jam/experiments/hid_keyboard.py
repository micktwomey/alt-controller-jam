# 2023-10-30: Adapted from https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse

# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Keyboard example"""
import time

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


def main():
    key_mapping = [
        (board.GP2, Keycode.A),  # SW4
        (board.GP3, Keycode.Z),  # SW3
        (board.GP4, Keycode.S),  # SW2
        (board.GP5, Keycode.X),  # SW1
        (board.GP10, Keycode.LEFT_ARROW),  # SW4
        (board.GP11, Keycode.DOWN_ARROW),  # SW3
        (board.GP12, Keycode.UP_ARROW),  # SW2
        (board.GP13, Keycode.RIGHT_ARROW),  # SW1
    ]

    # The pins we'll use, each will have an internal pullup
    keypress_pins = [key[0] for key in key_mapping]
    # Our array of key objects
    key_pin_array = []
    # The Keycode sent for each button, will be paired with a control key
    keys_pressed = [key[1] for key in key_mapping]

    # The keyboard object!
    time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
    keyboard = Keyboard(usb_hid.devices)
    # keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

    # Make all pin objects inputs with pullups
    for pin in keypress_pins:
        key_pin = digitalio.DigitalInOut(pin)
        key_pin.direction = digitalio.Direction.INPUT
        key_pin.pull = digitalio.Pull.UP
        key_pin_array.append(key_pin)

    # For most CircuitPython boards:
    led = digitalio.DigitalInOut(board.LED)
    # For QT Py M0:
    # led = digitalio.DigitalInOut(board.SCK)
    led.direction = digitalio.Direction.OUTPUT

    print("Waiting for key pin...")

    pressed = set()

    while True:
        # Check each pin
        for key_pin in key_pin_array:
            if not key_pin.value:  # Is it grounded?
                i = key_pin_array.index(key_pin)
                print("Pin #%d is grounded." % i)

                if i in pressed:
                    continue

                # Turn on the red LED
                led.value = True

                pressed.add(i)

                # while not key_pin.value:
                #     pass  # Wait for it to be ungrounded!
                # # "Type" the Keycode or string
                key = keys_pressed[i]  # Get the corresponding Keycode or string
                # if isinstance(key, str):  # If it's a string...
                #     keyboard_layout.write(key)  # ...Print the string
                # else:  # If it's not a string...
                keyboard.press(key)  # "Press"...

            elif key_pin.value:
                i = key_pin_array.index(key_pin)
                if i in pressed:
                    key = keys_pressed[i]  # Get the corresponding Keycode or string
                    keyboard.release(key)  # ..."Release"!

                    # Turn off the red LED
                    led.value = False
                    pressed.remove(i)

        time.sleep(0.01)
