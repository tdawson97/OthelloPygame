import pygame, sys
from settings import *
from tile import Tile


class Game:
    """
    A class to represent the game being played.

    Attributes
    ----------
    screen : Surface
        The entire window the game is played on
    border : Rect
        The border separating the board from the edge of the screen

    Methods
    ----------
    setup_game_board():
        sets up the initial game board
    run():
        keeps window open and updated until player exits
    """
    def __init__(self):
        """
        Constructs the necessary attributes for Game object.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(GREEN)
        self.border = pygame.Rect(0, 0, WIDTH, HEIGHT)
        pygame.draw.rect(self.screen, BROWN, self.border, 90, 100)
        pygame.display.set_caption('Othello')

    def setup_game_board(self):
        """
        Communicated with tile.py to create Tile objects and draw pieces
        on the board.
        """
        for row_index, row in enumerate(board):
            for i in range(8):
                x = i * TILE_WIDTH + 100
                y = row_index * TILE_HEIGHT + 100
                if row[i] == '.':
                    tile = Tile(GREY)
                    tile.draw_piece()
                    self.screen.blit(tile.surface, (x, y))
                elif row[i] == 'X':
                    tile = Tile(BLACK)
                    tile.draw_piece()
                    self.screen.blit(tile.surface, (x, y))
                else:
                    tile = Tile(WHITE)
                    tile.draw_piece()
                    self.screen.blit(tile.surface, (x, y))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.setup_game_board()
    game.run()
