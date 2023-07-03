import pygame
from settings import *
from player import Player

class UI:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(font, 50)

        self.options_screen = pygame.Surface((800, 800))
        self.options_screen.fill(BROWN)
        self.options_font = pygame.font.Font(font, 30)
        self.options_screen_rect = self.options_screen.get_rect(topleft=(100, 100))

        self.color_rects = []
        self.players = []






    def show_scores(self, player_1, player_2):
        text_surf = self.font.render(f'Player 1: {len(player_1.pieces)}', False, player_1.color)
        text_rect = text_surf.get_rect(topleft=(100, 0))
        self.display_surface.blit(text_surf, text_rect)

        text_surf = self.font.render(f'Player 2: {len(player_2.pieces)}', False, player_2.color)
        text_rect = text_surf.get_rect(topleft=(650, 0))
        self.display_surface.blit(text_surf, text_rect)

        text_surf = self.options_font.render(f'Press q to view options', False, BLACK)
        text_rect = text_surf.get_rect(topleft=(345, 925))
        self.display_surface.blit(text_surf, text_rect)

    def show_winner_text(self, winner=None):
        if winner:
            text_surf = self.font.render(f'{winner.name} wins!!', False, winner.color)
        else:
            text_surf = self.font.render(f"It's a tie.", False, BLACK)

        text_rect = text_surf.get_rect(topleft=(450, 0))
        self.display_surface.blit(text_surf, text_rect)

    def display_options_screen(self, player_1, player_2):
        if not self.players:
            self.players.append(player_1)
            self.players.append(player_2)
        self.display_surface.blit(self.options_screen, self.options_screen_rect)

        text_surf = self.options_font.render(f'Click to change player 1 name: {player_1.name}',
                                             False, player_1.color)
        text_rect = text_surf.get_rect(topleft=(150, 150))
        self.display_surface.blit(text_surf, text_rect)

        text_surf = self.options_font.render(f'Click to change player 2 name: {player_2.name}',
                                             False, player_2.color)
        text_rect = text_surf.get_rect(topleft=(150, 300))
        self.display_surface.blit(text_surf, text_rect)

        text_surf = self.options_font.render(f'Click to change player 1 color',
                                             False, player_1.color)
        text_rect = text_surf.get_rect(topleft=(150, 450))
        self.display_surface.blit(text_surf, text_rect)
        self.color_display((50, 400), player_1)

        text_surf = self.options_font.render(f'Click to change player 2 color',
                                             False, player_2.color)
        text_rect = text_surf.get_rect(topleft=(150, 600))
        self.display_surface.blit(text_surf, text_rect)
        self.color_display((50, 550), player_2)

    def color_display(self, pos, player):
        for color, rgb_value in player_colors.items():
            color_rect = pygame.Rect(pos[0], pos[1], 50, 50)
            if color_rect not in self.color_rects:
                self.color_rects.append(color_rect)
            pygame.draw.rect(self.options_screen, rgb_value, color_rect)
            if rgb_value == player.color:
                pygame.draw.rect(self.options_screen, GREEN, pygame.Rect(pos[0], pos[1], 50, 50), 5)
            pos = (pos[0]+100, pos[1])

    def change_player_color(self, pos):
        pos_x = pos[0] - 100
        pos_y = pos[1] - 100
        for index, rect in enumerate(self.color_rects):
            if rect.collidepoint((pos_x, pos_y)):
                pygame.draw.rect(self.options_screen, GREEN, pygame.Rect(rect.x, rect.y, 50, 50), 5)
                if index < len(player_colors):
                    self.players[0].set_color(list(player_colors.values())[index])
                else:
                    self.players[1].set_color(list(player_colors.values())[index-len(player_colors)])












