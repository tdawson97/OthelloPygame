import pygame
from settings import *

class UI:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(font, 50)

        self.options_screen = pygame.Surface((800, 800))
        self.options_screen_rect = self.options_screen.get_rect(topleft=(100, 100))



    def show_scores(self, player_1_score, player_2_score):
        text_surf = self.font.render(f'Player 1: {player_1_score}', False, WHITE)
        text_rect = text_surf.get_rect(topleft=(100, 0))
        self.display_surface.blit(text_surf, text_rect)

        text_surf = self.font.render(f'Player 2: {player_2_score}', False, BLACK)
        text_rect = text_surf.get_rect(topleft=(650, 0))
        self.display_surface.blit(text_surf, text_rect)

    def show_winner_text(self, winner=None):
        if winner:
            text_surf = self.font.render(f'{winner.name} wins!!', False, winner.color)
        else:
            text_surf = self.font.render(f"It's a tie.", False, BLACK)

        text_rect = text_surf.get_rect(topleft=(350, 0))
        self.display_surface.blit(text_surf, text_rect)

    def display_options_screen(self):
        self.display_surface.blit(self.options_screen, self.options_screen_rect)
        self.display_surface.blit(self.options_screen, self.options_screen_rect)

