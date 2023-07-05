import pygame
from settings import *


class Tile:
    """
    A class to represent a tile on the game board.

    Attributes
    ----------
    color : tuple
        color for the piece on the tile
    surface: Surface
        to draw circle piece on Tile object
    coord_pos: tuple
        to represent the coordinate position of the tile on the board
    pixel_pos: tuple
        to represent the position of the tile on the screen
    """
    def __init__(self, color=None, coord_pos=None, pixel_pos=None):
        """
        Constructs all the necessary attributes for a Tile object
        """
        self.color = color
        self.surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT), pygame.SRCALPHA)
        self.coord_pos = coord_pos
        self.pixel_pos = pixel_pos

    def set_color(self, color):
        self.color = color

    def draw_piece(self):
        """
        Draws the piece onto the Tile object
        """
        pygame.draw.circle(self.surface, self.color, center, radius)

    def draw_outline(self, color=RED, width=5):
        pygame.draw.circle(self.surface, color, center, radius, width)

