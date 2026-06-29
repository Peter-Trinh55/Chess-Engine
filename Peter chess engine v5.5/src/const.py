# Screen dimensions
# v6.2.5 keeps the chess board at 800x800, but adds a top and bottom
# player/timer strip so the live match UI is easier to read.
BOARD_SIZE = 800
HUD_HEIGHT = 50
BOARD_OFFSET_X = 0
BOARD_OFFSET_Y = HUD_HEIGHT
SIDEBAR_WIDTH = 260
WIDTH = BOARD_SIZE + SIDEBAR_WIDTH
HEIGHT = BOARD_SIZE + (HUD_HEIGHT * 2)

# Board dimensions
ROWS = 8
COLS = 8
SQSIZE = BOARD_SIZE // COLS
