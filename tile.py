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

    Methods
    ----------
    set_color():
        Set color of the piece

    draw_piece():
        Draw the circular piece on the Tile object

    draw_outline():
        Draw an outline over a piece on the board
    """
    def __init__(self, color, coord_pos, pixel_pos):
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

