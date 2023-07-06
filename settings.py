# size of window
WIDTH = 1000
HEIGHT = 1000

# size of tile
TILE_WIDTH = 100
TILE_HEIGHT = 100

# circle piece dimensions
radius = 45
center = [50, 50]

# color RGB[a] values
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (153,0,0)
GREY = (96,96,96)
GREEN = (0,102,0)
BROWN = (133,94,66)


# game board
board = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "O", "X", ".", ".", "."],
            [".", ".", ".", "X", "O", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

possible_moves = {
                    'up': (0, -1),
                    'down': (0, 1),
                    'left': (-1, 0),
                    'right': (1, 0),
                    'upper_left': (-1, -1),
                    'upper_right': (1, -1),
                    'bottom_left': (-1, 1),
                    'bottom_right': (1, 1)}

font = 'PlayfairDisplay-Regular.otf'

player_colors = {"BLACK": (0, 0, 0),
                 "WHITE": (255, 255, 255),
                 "PURPLE": (127, 0, 255),
                 "BLUE": (0, 128, 255),
                 "YELLOW": (255, 255, 0),
                 "ORANGE": (255, 128, 0),
                 "PINK": (255, 102, 255),
                 "RED": (204, 0, 0)
                 }
