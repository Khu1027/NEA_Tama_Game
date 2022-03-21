
# creating a hunger bar that
# <3 is able to start a new game with a new hunger bar
# - minus hunger in regular increments (30 seconds)
# - save the hunger bar progress into a text file
# - load the hunger bar from the text file
# - have a button that feeds the pet + increases the hunger
# - if the hunger is zero for a period of time, 1 minute
#   - the pet signals for food up to 2 times if hunger is zero
#   - bad points are given if the hunger is still 0 after signals
# - if the hunger is full for a period of time, 1 minute, good points are given
# - if the hunger is full and the user feeds the pet 3 times in a row
#   - signal sickness, + feed cooldown.

import pygame, sys
import json

pygame.init()
# best screen size rn is 1280, 720
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
global game_font
game_font = pygame.font.Font(None, 32)


#colours
white = (255,255,255)
matcha = (116, 141, 46)

# creating hunger bar
hunger_bar_surf = pygame.Surface([640, 50])
hunger_bar_surf.fill(white)
hunger_bar_rect = hunger_bar_surf.get_rect(center = (640, 50))

#creating feed button
feed_surf = pygame.Surface([200,200])
feed_surf.fill(white)
feed_rect = feed_surf.get_rect(center = (320, 360))

#data = hunger points
hunger_count = 0

# loading the hunger_count data
# tries to open the file, if the file is found, the new count is loaded, else ignored
try:
    with open('hunger_bar.txt') as hunger_file:
        hunger_count = json.load(hunger_file)
except:
    print("No file created yet")

#creating text on hunger bar
hunger_text_surf = game_font.render(f" hunger: {hunger_count}", True, 'Black')
hunger_text_rect = hunger_text_surf.get_rect(center = (640,50))

#creating text on the feed button
feed_text_surf = game_font.render(f"Feed", True, 'Black')
feed_text_rect = hunger_text_surf.get_rect(center = (340, 360))

# feed subroutine
def feed(surf, rect, count):
    if rect.collidepoint(event.pos):
        if count >= 0 and count <=4:
            count = count + 1
        elif count == 5:
            count = count
            print("The hunger is already full")
        surf = game_font.render(f" hunger: {count}", True, 'Black')
        rect = surf.get_rect(center = (640,50))
    return [surf, rect, count]



#event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("hunger_bar.txt", "w") as hunger_file:
                json.dump(hunger_count, hunger_file)
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            new = feed(feed_surf, feed_rect, hunger_count)
            hunger_text_surf, hunger_text_rect = new[0], new[1]
            hunger_count = new[2]

    screen.fill(matcha)
    #creating top hunger bar counter
    screen.blit(hunger_bar_surf, hunger_bar_rect)
    screen.blit(hunger_text_surf, hunger_text_rect)
    #creating the feed button
    screen.blit(feed_surf, feed_rect)
    screen.blit(feed_text_surf, feed_text_rect)
    #updating the display and frame rate
    pygame.display.update()
    clock.tick(60)
