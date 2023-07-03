import pygame
from settings import *

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pieces = []

    def set_name(self, name):
        self.name = name

    def set_color(self, color):
        self.color = color
