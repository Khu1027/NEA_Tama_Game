#
# - minus hunger in regular increments (30 seconds)
#       - A Countdown will need to be made.
# - Create Classes so that the different Boxs can be made, buttons can be made, etc.

import json
import pygame
import sys

#----------------- previous code in GAME Hunger.py -----------------------

pygame.init()
# best screen size rn is 1280, 720
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
global game_font, white, matcha
game_font = pygame.font.Font(None, 32)
white = (255,255,255)
matcha = (116, 141, 46)

#-------------------------------------------------------------------------
# https://youtu.be/Mp6YMt8MSAU?list=PLmr34YByUWUf2wo5f0g1damQ86PfzH8XC
#creating a Box class so that all the variables can be reused: Hunger, Health, Happiness, Box etc.
class Box:
    def __init__(self, area, surf_center, text, text_center):
        self.area = area
        self.surf_center = surf_center
        self.text = text
        self.text_center = text_center

    def make_bar(self):
        self.bar_surf = pygame.Surface(self.area)
        self.bar_surf.fill(white)
        self.bar_rect = self.bar_surf.get_rect(center = self.surf_center)
        return self.bar_surf, self.bar_rect

    def make_text(self):
        self.text_surf = game_font.render(self.text, True, "Black")
        self.text_rect = self.text_surf.get_rect(center = self.text_center)
        return self.text_surf, self.text_rect

# ~~~~~~~~~~~~~~~~~~~~~~~ Hunger ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hunger_count = 0
# loading the hunger_count data
# tries to open the file, if the file is found, the new count is loaded, else ignored
try:
    with open('hunger_bar.txt') as hunger_file:
        hunger_count = json.load(hunger_file)
except:
    print("No file created yet")

hunger_text = f"Hunger: {hunger_count}/5"
hunger = Box([200,50], (640,50), hunger_text, (640,50))
hunger_bar = hunger.make_bar()
hunger_bar_surf, hunger_bar_rect = hunger_bar[0], hunger_bar[1]
hunger_text = hunger.make_text()
hunger_text_surf, hunger_text_rect = hunger_text[0], hunger_text[1]

# ~~~~~~~~~~~~~~~~~~~ Health ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
health_count = 0
# loading the health_count data
# tries to open the file, if the file is found, the new count is loaded, else ignored
try:
    with open('health_bar.txt') as health_file:
        health_count = json.load(health_file)
except:
    print("No file created yet")

health_text = f"Health: {health_count}/5"
health = Box([200,50], (320,50), health_text, (320,50))
health_bar = health.make_bar()
health_bar_surf, health_bar_rect = health_bar[0], health_bar[1]
health_text = health.make_text()
health_text_surf, health_text_rect = health_text[0], health_text[1]

# ~~~~~~~~~~~~~~~~~~~~~~ Happiness ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
happy_count = 0
# loading the happy_count data
# tries to open the file, if the file is found, the new count is loaded, else ignored
try:
    with open('happy_bar.txt') as happy_file:
        happy_count = json.load(happy_file)
except:
    print("No file created yet")

happy_text = f"Happy: {happy_count}/5"
happy = Box([200,50], (960,50), happy_text, (960,50))
happy_bar = happy.make_bar()
happy_bar_surf, happy_bar_rect = happy_bar[0], happy_bar[1]
happy_text = happy.make_text()
happy_text_surf, happy_text_rect = happy_text[0], happy_text[1]

#--------------- Saving and loading variables -------------------------
global txt_files, stat_count
txt_files = ["hunger_bar", "health_bar", "happy_bar"]
stat_count = [hunger_count, health_count, happy_count]

def save_all():
    for i in txt_files:
        json.dump(stat_count[i], (open(f"{txt_files[i]}.txt", "w")))


# ------------------------- event loop ---------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_all()
            pygame.quit()
            sys.exit()

    screen.fill(matcha)
    #hunger
    screen.blit(hunger_bar_surf, hunger_bar_rect)
    screen.blit(hunger_text_surf, hunger_text_rect)
    #health
    screen.blit(health_bar_surf, health_bar_rect)
    screen.blit(health_text_surf, health_text_rect)
    #happiness
    screen.blit(happy_bar_surf, happy_bar_rect)
    screen.blit(happy_text_surf, happy_text_rect)
    #display and frame rate
    pygame.display.update()
    clock.tick(60)
