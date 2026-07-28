"""Configurations for different styles of keyboard controllers

"""

from adafruit_hid.keycode import Keycode
from gamecraft_alt_controller_jam_board import hardware

# Pico-8 controller layout, player 1
PICO_8_PLAYER_1 = {
    hardware.DPad.UP: Keycode.UP_ARROW,
    hardware.DPad.DOWN: Keycode.DOWN_ARROW,
    hardware.DPad.LEFT: Keycode.LEFT_ARROW,
    hardware.DPad.RIGHT: Keycode.RIGHT_ARROW,
    hardware.SteamButtons.A: Keycode.X,
    hardware.SteamButtons.B: Keycode.Z,
    hardware.SteamButtons.X: Keycode.X,
    hardware.SteamButtons.Y: Keycode.Z,
}

# Pico-8 controller layout, player 2
PICO_8_PLAYER_2 = {
    hardware.DPad.UP: Keycode.E,
    hardware.DPad.DOWN: Keycode.D,
    hardware.DPad.LEFT: Keycode.S,
    hardware.DPad.RIGHT: Keycode.F,
    hardware.SteamButtons.A: Keycode.Q,
    hardware.SteamButtons.B: Keycode.TAB,
    hardware.SteamButtons.X: Keycode.Q,
    hardware.SteamButtons.Y: Keycode.TAB,
}

# Nintendo controller layout
NINTENDO = {
    hardware.DPad.UP: Keycode.UP_ARROW,
    hardware.DPad.DOWN: Keycode.DOWN_ARROW,
    hardware.DPad.LEFT: Keycode.LEFT_ARROW,
    hardware.DPad.RIGHT: Keycode.RIGHT_ARROW,
    hardware.NintendoButtons.A: Keycode.A,
    hardware.NintendoButtons.B: Keycode.B,
    hardware.NintendoButtons.X: Keycode.X,
    hardware.NintendoButtons.Y: Keycode.Y,
}

# Steam controller layout
STEAM = {
    hardware.DPad.UP: Keycode.UP_ARROW,
    hardware.DPad.DOWN: Keycode.DOWN_ARROW,
    hardware.DPad.LEFT: Keycode.LEFT_ARROW,
    hardware.DPad.RIGHT: Keycode.RIGHT_ARROW,
    hardware.SteamButtons.A: Keycode.S,
    hardware.SteamButtons.B: Keycode.D,
    hardware.SteamButtons.X: Keycode.A,
    hardware.SteamButtons.Y: Keycode.W,
}
