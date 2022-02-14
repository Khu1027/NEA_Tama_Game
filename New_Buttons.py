# https://www.youtube.com/watch?v=8SzTzvrWaAA&t=1120s
# New_buttons.py

import pygame
import Variables

pygame.init()

class Button:
    # this Box class will include all 'box' type variables that will be displayed like buttons and a counter at the top
    def __init__(self, text, width, height, pos):
        self.surf_rect = pygame.Rect(pos, (width, height))
        self.surf_rect_colour = Variables.white

        self.text_surf = Variables.game_font.render(text, True, "Black")
        self.text_rect = self.text_surf.get_rect(center = self.surf_rect.center)

    def draw(self):
        pygame.draw.rect(Variables.screen, self.surf_rect_colour, self.surf_rect)
        Variables.screen.blit(self.text_surf, self.text_rect)

# # [This below is just testing the code]
# feed = Button((200,50), [320,50], "Feed", (320,50))
