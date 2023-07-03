import pygame
from settings import *

class Player:
    def __init__(self, name, color, status=False):
        self.name = name
        self.color = color
        self.pieces = []
        self.active = status

    def set_name(self, name):
        self.name = name

    def set_color(self, color):
        self.color = color
        for tile in self.pieces:
            tile.set_color(color)

    def switch_turns(self):
        self.active = not self.active
