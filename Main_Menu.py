#Main menu.py

import New_Buttons
import pygame
import sys
import Variables

# Screens
import Settings_Screen
import Help_Screen
import Death_Screen
import Main_Game
import game_continue

#import NewGame_Screen


# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
pygame.display.set_caption("Tama")
screen = Variables.screen
clock = Variables.clock
buttons = New_Buttons


Title = buttons.Button("Shrub Life!", 200, 80, (550, 200))
Start = buttons.Button("Start", 200, 60, (550, 350))
Settings = buttons.Button("Settings", 200, 60, (550, 450))
Help = buttons.Button("Help", 200, 60, (550, 550))


click = False

# ------------ event loop -------------------------
while True:
    mx, my = pygame.mouse.get_pos()
    screen.fill(Variables.matcha)

    if Start.surf_rect.collidepoint((mx,my)):
        if click:
            # The continue_game file checks if the game has a save file or not
            # then continues if it does and the pet is not dead,
            # but doesn't continue the game if the pet is dead and starts a new one
            if not Death_Screen.dead:
                if Death_Screen.continue_game:
                    game_continue.continue_from_save()
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

    if Death_Screen.choice == 2:
        pygame.quit()
        sys.exit()
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