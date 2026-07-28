from gamecraft_alt_controller_jam_board import configurations, keyboard


# Pick one of the following to run as a keyboard:

# Defaults to pico-8 style controles for player one
keyboard.main(configurations.PICO_8_PLAYER_1)

# Use this instead for pico-8 player 2
# keyboard.main(configurations.PICO_8_PLAYER_2)

# Use this for Nintendo style layouts
# keyboard.main(configurations.NINTENDO)

# Use this instead for arrow keys and wasd
# keyboard.main(Sconfigurations.TEAM)
