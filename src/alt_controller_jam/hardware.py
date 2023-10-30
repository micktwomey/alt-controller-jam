"""Alt-Controller-Jam Controller Hardware
"""

import board


class Board:
    """Hardware boards

    Layout (facing the board from the button side):

        Header Pins
        |o|o|o|o|o|

            SW2
            O
        SW4 O   O SW1
            O
            SW3

    On bottom:

        Header Pins
        |SW1 |SW2 |SW3 |SW4 |GND|
        |GP5 |GP4 |GP3 |GP2 |GND|
        |GP9 |GP8 |GP7 |GP6 |GND|
        |GP13|GP12|GP11|GP10|GND|
        |GP18|GP19|GP20|GP21|GND|

    Header pins are grouped by matching sets on the pico
    """

    TOP = [board.GP4, board.GP8, board.GP12, board.GP19]  # SW2
    BOTTOM = [board.GP3, board.GP7, board.GP11, board.GP20]  # SW3
    LEFT = [board.GP2, board.GP6, board.GP10, board.GP21]  # SW5
    RIGHT = [board.GP5, board.GP9, board.GP13, board.GP18]  # SW1


class FirstBoard:
    TOP = Board.TOP[0]  # SW2
    BOTTOM = Board.BOTTOM[0]  # SW3
    LEFT = Board.LEFT[0]  # SW4
    RIGHT = Board.RIGHT[0]  # SW1


class SecondBoard:
    TOP = Board.TOP[1]  # SW2
    BOTTOM = Board.BOTTOM[1]  # SW3
    LEFT = Board.LEFT[1]  # SW4
    RIGHT = Board.RIGHT[1]  # SW1


class ThirdBoard:
    TOP = Board.TOP[2]  # SW2
    BOTTOM = Board.BOTTOM[2]  # SW3
    LEFT = Board.LEFT[2]  # SW4
    RIGHT = Board.RIGHT[2]  # SW1


class FourthBoard:
    TOP = Board.TOP[3]  # SW2
    BOTTOM = Board.BOTTOM[3]  # SW3
    LEFT = Board.LEFT[3]  # SW4
    RIGHT = Board.RIGHT[3]  # SW1


class DPad:
    """Directional Pad

           UP
           O
    LEFT O   O RIGHT
           O
          DOWN
    """

    UP = FirstBoard.TOP
    DOWN = FirstBoard.BOTTOM
    LEFT = FirstBoard.LEFT
    RIGHT = FirstBoard.RIGHT


class NintendoButtons:
    """Nintendo

        X
        O
    Y O   O A
        O
        B
    """

    A = ThirdBoard.RIGHT
    B = ThirdBoard.BOTTOM
    X = ThirdBoard.TOP
    Y = ThirdBoard.LEFT


class SteamButtons:
    """Steam / Xbox / Windows

        Y
        O
    X O   O B
        O
        A
    """

    A = ThirdBoard.BOTTOM
    B = ThirdBoard.RIGHT
    X = ThirdBoard.LEFT
    Y = ThirdBoard.TOP
