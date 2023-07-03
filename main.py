import pygame
import sys
import math
from settings import *
from tile import Tile
from player import Player
from ui import UI


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
    change_piece():
        change a piece on the tile
    find_available_positions():
        outlines all available positions for the active player
    check_direction():
        checks each direction from a specified piece
    make_move():
        makes a move for the player at a player-selected valid position
    run():
        keeps window open and updated until player exits
    """
    def __init__(self):
        """
        Constructs the necessary attributes for Game object.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.border = pygame.Rect(0, 0, WIDTH, HEIGHT)
        pygame.display.set_caption('Othello')
        self.pieces = []


        self.available_positions = []
        self.black_pieces = []
        self.white_pieces = []

        self.player_1 = Player("Player 1", WHITE, True)
        self.player_2 = Player("Player 2", BLACK)



        self.ui = UI()
        self.paused = False

    def setup_game_board(self):
        """
        Communicates with tile.py to create Tile objects and draw pieces
        on the board.
        """
        self.screen.fill(GREEN)
        pygame.draw.rect(self.screen, BROWN, self.border, 90, 100)
        for row_index, row in enumerate(board):
            hold_pieces = []
            for i in range(8):
                x = i * TILE_WIDTH + 100
                y = row_index * TILE_HEIGHT + 100
                if row[i] == '.':
                    tile = Tile(GREY, (i + 1, row_index + 1), (x, y))
                elif row[i] == 'X':
                    tile = Tile(BLACK, (i + 1, row_index + 1), (x, y))
                    self.player_2.pieces.append(tile)
                else:
                    tile = Tile(WHITE, (i + 1, row_index + 1), (x, y))
                    self.player_1.pieces.append(tile)
                tile.draw_piece()
                hold_pieces.append(tile)
                self.screen.blit(tile.surface, tile.pixel_pos)
            self.pieces.append(hold_pieces)

        self.find_available_positions()
        for piece in self.available_positions:
            piece.draw_outline()
            self.screen.blit(piece.surface, piece.pixel_pos)


    def update_game_board(self):
        self.screen.fill(GREEN)
        pygame.draw.rect(self.screen, BROWN, self.border, 90, 100)

        for tile in self.pieces:
            for i in range(8):
                tile[i].draw_piece()
                self.screen.blit(tile[i].surface, tile[i].pixel_pos)

        self.find_available_positions()
        for piece in self.available_positions:
            piece.draw_outline()
            self.screen.blit(piece.surface, piece.pixel_pos)



    def change_piece(self, tile, color):
        """
        Changes the piece displayed on a tile.
        :param tile: the tile the piece is on
        :param color: the color to change the piece to
        """
        tile.set_color(color)
        tile.draw_piece()
        self.screen.blit(tile.surface, tile.pixel_pos)



    def find_available_positions(self):
        """
        Outlines in red the pieces that the active player can make a valid move on.
        Calls the check direction method for validation of move.
        """
        if self.player_1.active:
            active_player = self.player_1
            opponent = self.player_2
        else:
            active_player = self.player_2
            opponent = self.player_1

        self.available_positions = []
        for piece in active_player.pieces:
            for direction in possible_moves.values():
                self.check_direction(piece, direction, active_player, opponent)

        if not self.available_positions:
            self.declare_winner()


    def check_direction(self, piece, direction, active_player, opponent):
        """
        Checks each direction from a piece, updates self.available_positions, opponent_pieces_jumped
        :param piece: the tile piece to check around
        :param direction: the tuple representing which direction to check
        :returns: None, opponent_pieces_jumped
        """
        opponent_pieces_jumped = []
        list_pos = (piece.coord_pos[1] - 1 + direction[1])
        item_pos = (piece.coord_pos[0] - 1 + direction[0])

        # check if outside of game board
        if list_pos not in range(0, 8) or item_pos not in range(0, 8):
            return

        check_position = self.pieces[list_pos][item_pos]

        # continue checking in the same direction if check_position is opponent's piece

        while check_position in opponent.pieces:
            list_pos = (check_position.coord_pos[1] - 1 + direction[1])
            item_pos = (check_position.coord_pos[0] - 1 + direction[0])
            opponent_pieces_jumped.append(check_position)

            if list_pos not in range(0, 8) or item_pos not in range(0, 8):
                return

            check_position = self.pieces[list_pos][item_pos]

        if check_position.color == GREY and len(opponent_pieces_jumped) > 0:
            if check_position not in self.available_positions:
                self.available_positions.append(check_position)
                return
            return

        elif check_position in active_player.pieces:
            return opponent_pieces_jumped
        return

    def make_move(self, mouse_position):
        """
        Places player piece at mouse clicked position, updates other pieces according to rules of the game.
        Empties self.available_positions list and swaps active player at the end.
        :param mouse_position: (x,y) position of mouse click
        :returns: None
        """
        # find coord_pos to index into selected tile
        x = math.floor(mouse_position[0] // 100)
        y = math.floor(mouse_position[1] // 100)
        tile = self.pieces[y-1][x-1]

        if self.player_1.active:
            active_player = self.player_1
            opponent = self.player_2
        else:
            active_player = self.player_2
            opponent = self.player_1

        # check if tile is an available spot, update piece, return if not
        if tile in self.available_positions:
            self.available_positions.remove(tile)
            self.change_piece(tile, active_player.color)
            active_player.pieces.append(tile)
        else:
            return

        # check each direction from new piece, update others surrounding if needed
        for direction in possible_moves.values():
            switch_tiles = self.check_direction(tile, direction, active_player, opponent)
            if switch_tiles is not None:
                for piece in switch_tiles:
                    self.change_piece(piece, active_player.color)
                    active_player.pieces.append(piece)
                    opponent.pieces.remove(piece)

        # remove outline
        for tile in self.available_positions:
            self.change_piece(tile, GREY)

        # swap players
        self.available_positions = []
        active_player.switch_turns()
        opponent.switch_turns()

    def declare_winner(self):
        if len(self.player_1.pieces) > len(self.player_2.pieces):
            self.ui.show_winner_text(self.player_1)
        elif len(self.player_2.pieces) > len(self.player_1.pieces):
            self.ui.show_winner_text(self.player_2)
        else:
            self.ui.show_winner_text()

    def run(self):
        self.setup_game_board()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.paused = not self.paused
                if self.paused is False:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mouse_position = pygame.mouse.get_pos()
                        self.make_move(mouse_position)
                    self.update_game_board()
                else:
                    self.ui.display_options_screen(self.player_1, self.player_2)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mouse_position = pygame.mouse.get_pos()
                        self.ui.change_player_color(mouse_position)

                if self.available_positions:
                    self.ui.show_scores(self.player_1, self.player_2)

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()

