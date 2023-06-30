import pygame
from settings import *


class Tile:
    """
    A class to represent a tile on the game board.

    Attribtues
    ----------
    color : tuple
        color for the piece on the tile
    surface: Surface
        to draw circle piece on Tile object

    Methods
    ----------
    draw_piece():
        Draw the circular piece on the Tile object
    """
    def __init__(self, color):
        """
        Constructs all the necessary attributes for a Tile object
        """
        self.color = color
        self.surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT), pygame.SRCALPHA)

    def draw_piece(self):
        """
        Draws the piece onto the Tile object
        """
        pygame.draw.circle(self.surface, self.color, center, radius)
