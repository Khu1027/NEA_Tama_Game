#Main menu.py

import New_Buttons
import pygame
import sys
import Variables
import Main_Game
import Settings_Screen
import Help_Screen
#import NewGame_Screen


# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
pygame.display.set_caption("Tama")
screen = Variables.screen
clock = Variables.clock
buttons = New_Buttons

Title = buttons.Button("Tamagotchi!", 200, 80, (550, 100))
Start = buttons.Button("Start", 200, 80, (550, 250))
Settings = buttons.Button("Settings", 200, 80, (550, 400))
Help = buttons.Button("Help", 200, 80, (550, 550))


click = False

# ------------ event loop -------------------------
while True:
    mx, my = pygame.mouse.get_pos()
    screen.fill(Variables.matcha)

    if Start.surf_rect.collidepoint((mx,my)):
        if click:
            # if Game_Time.new_game:
            #     NewGame_Screen.display_screen()
            # if not Game_Time.new_game:
            #     Main_Game.display_screen()
            Main_Game.display_screen()
    if Settings.surf_rect.collidepoint((mx,my)):
        if click:
            Settings_Screen.display_screen()
    if Help.surf_rect.collidepoint((mx,my)):
        if click:
            Help_Screen.display_screen()

    Title.draw_text()
    Start.draw()
    Settings.draw()
    Help.draw()

    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    pygame.display.flip()
    clock.tick(60)