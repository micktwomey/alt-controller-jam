from alt_controller_jam import configurations
from alt_controller_jam import keyboard

# Pick one of the following to run as a keyboard:

# Defaults to pico-8 style controles for player one
keyboard.main(configurations.PICO_8_PLAYER_1)

# Use this instead for pico-8 player 2
# keyboard.main(configurations.PICO_8_PLAYER_2)

# Use this instead for arrow keys and wasd
# keyboard.main(configurations.STEAM)
