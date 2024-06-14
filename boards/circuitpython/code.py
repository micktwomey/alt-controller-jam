from adafruit_hid.keycode import Keycode
from alt_controller_jam import hardware, keyboard

# Go to the bottom of this file to pick a configuration to use

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


# Pick one of the following to run as a keyboard:

# Defaults to pico-8 style controles for player one
keyboard.main(PICO_8_PLAYER_1)

# Use this instead for pico-8 player 2
# keyboard.main(PICO_8_PLAYER_2)

# Use this for Nintendo style layouts
# keyboard.main(NINTENDO)

# Use this instead for arrow keys and wasd
# keyboard.main(STEAM)
