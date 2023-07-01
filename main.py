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
    pieces : list of lists
        contains all tile objects, formatted the same as board in settings.py
    active_player : tuple
        the color code of the player that has the next move
    inactive_player : tuple
        the color code of the player that is waiting for their turn
    available_positions : list
        the available tiles to move on for the player that has the next move
    black_pieces : list
        all the black player's pieces on the board
    white_pieces : list
        all the white player's pieces on the board

    Methods
    ----------
    setup_game_board():
        sets up the initial game board
    find_available_positions():
        outlines all available positions for the active player
    check_direction():
        checks each direction from a specified piece
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

        self.pieces = []
        self.active_player = WHITE
        self.inactive_player = BLACK
        self.available_positions = []

        self.black_pieces = []
        self.white_pieces = []

    def setup_game_board(self):
        """
        Communicates with tile.py to create Tile objects and draw pieces
        on the board.
        """
        for row_index, row in enumerate(board):
            hold_pieces = []
            for i in range(8):
                x = i * TILE_WIDTH + 100
                y = row_index * TILE_HEIGHT + 100
                if row[i] == '.':
                    tile = Tile(GREY, (i + 1, row_index + 1), (x, y))
                elif row[i] == 'X':
                    tile = Tile(BLACK, (i + 1, row_index + 1), (x, y))
                    self.black_pieces.append(tile)
                else:
                    tile = Tile(WHITE, (i + 1, row_index + 1), (x, y))
                    self.white_pieces.append(tile)
                tile.draw_piece()
                self.screen.blit(tile.surface, (x, y))
                hold_pieces.append(tile)
            self.pieces.append(hold_pieces)

    def find_available_positions(self):
        """
        Outlines in red the pieces that the active player can make a valid move on.
        Calls the check direction method for validation of move.
        """
        if self.active_player == BLACK:
            pieces_list = self.black_pieces
        else:
            pieces_list = self.white_pieces

        for piece in pieces_list:
            for direction in possible_moves.values():
                self.check_direction(piece, direction)

        for piece in self.available_positions:
            piece.draw_outline()
            self.screen.blit(piece.surface, piece.pixel_pos)

    def check_direction(self, piece, direction):
        """
        Checks each direction from a piece, updates self.available_positions, opponent_pieces_jumped
        :param piece: the tile piece to check around
        :param direction: the tuple representing which direction to check

        """
        opponent_pieces_jumped = []
        list_pos = (piece.coord_pos[1] - 1 + direction[1])
        item_pos = (piece.coord_pos[0] - 1 + direction[0])

        # check if outside of game board
        if list_pos not in range(0, 7) or item_pos not in range(0, 7):
            return

        check_position = self.pieces[list_pos][item_pos]

        # continue checking in the same direction if check position is opponents
        # could also try 'while check_position is in (opponent pieces) <--some variable ?
        while check_position.color == self.inactive_player:
            list_pos = (check_position.coord_pos[1] - 1 + direction[1])
            item_pos = (check_position.coord_pos[0] - 1 + direction[0])
            opponent_pieces_jumped.append(check_position)

            if list_pos not in range(0, 7) or item_pos not in range(0, 7):
                return

            check_position = self.pieces[list_pos][item_pos]

        if check_position.color == GREY and len(opponent_pieces_jumped) > 0:
            self.available_positions.append(check_position)
            return

    def run(self):
        self.setup_game_board()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.find_available_positions()
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()

