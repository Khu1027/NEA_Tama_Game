import pygame
import Variables

pygame.init()


class Button:
    # this Box class will include all 'box' type variables that will be displayed like buttons and a counter at the top
    def __init__(self, center):
        self.center = center
        self.area = None
        self.bar_surf = None
        self.bar_rect = None
        self.text = None
        self.text_surf = None
        self.text_rect = None

    def get_surf(self, area):
        self.area = area
        # Making the surface underneath the text
        self.bar_surf = pygame.Surface(self.area)
        self.bar_surf.fill(Variables.white)
        self.bar_rect = self.bar_surf.get_rect(center=self.center)
        # Displaying the surface
        return self.bar_surf, self.bar_rect

    def get_text(self, text):
        self.text = text
        # Writing the text on top
        self.text_surf = Variables.game_font.render(self.text, True, "Black")
        self.text_rect = self.text_surf.get_rect(center=self.center)
        # Displaying the text
        return self.text_surf, self.text_rect

    def get_whole_box(self):
        self.get_surf()
        self.get_text()

# # [This below is just testing the code]
# feed = Button((200,50), [320,50], "Feed", (320,50))
