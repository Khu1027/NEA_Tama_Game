# https://www.youtube.com/watch?v=8SzTzvrWaAA&t=1120s
# New_buttons.py

import pygame
import Variables

pygame.init()


class Button:
    # this Box class will include all 'box' type variables that will be displayed like buttons and a counter at the top
    def __init__(self, text, width, height, pos):
        self.text = text
        self.width = width
        self.height = height
        self.pos = pos

        self.surf_rect = pygame.Rect(self.pos, (self.width, self.height))
        self.surf_rect_colour = Variables.white

        self.text_surf = Variables.game_font.render(self.text, True, "Black")
        self.text_rect = self.text_surf.get_rect(center=self.surf_rect.center)

    def draw(self):
        pygame.draw.rect(Variables.screen, self.surf_rect_colour, self.surf_rect)
        Variables.screen.blit(self.text_surf, self.text_rect)

    def draw_text(self):
        # for getting text only
        Variables.screen.blit(self.text_surf, self.text_rect)

    def change_text(self, text):
        self.text_surf = Variables.game_font.render(text, True, "Black")

    def change_colour(self, colour):
        self.surf_rect_colour = colour

    def change_position(self, pos):
        self.surf_rect = pygame.Rect(pos, (self.width, self.height))
        self.surf_rect_colour = Variables.white
