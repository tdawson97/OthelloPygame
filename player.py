import pygame
from settings import *

class Player:
    """
    Represents the players in the game

    Attributes:
        name
            the name of the player
        color
            the color the player was assigned or chose
        pieces
            a list of the current pieces for the player
        active
            boolean representing if it is the player's turn
    """
    def __init__(self, name, color, status=False):
        self.name = name
        self.color = color
        self.pieces = []
        self.active = status

    def set_color(self, color):
        self.color = color
        for tile in self.pieces:
            tile.set_color(color)

    def switch_turns(self):
        self.active = not self.active
