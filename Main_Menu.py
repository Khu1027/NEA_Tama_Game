# Main menu.py
import datetime

import New_Buttons
import pygame
import sys
import json
import Variables

# Screens
import Settings_Screen
import Help_Screen
import Death_Screen
import game_continue
import Main_Game

# import NewGame_Screen

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
pygame.display.set_caption("Shrub Life")
screen = Variables.screen
clock = Variables.clock
background = pygame.image.load("Pet Images/background.jpg")
buttons = New_Buttons

Title = pygame.image.load("Pet Images/Shrub Life Title.png")
# Title = buttons.Button("Shrub Life!", 200, 80, (550, 200))
Start = buttons.Button("Start", 200, 60, (550, 350))
Settings = buttons.Button("Settings", 200, 60, (550, 450))
Help = buttons.Button("Help", 200, 60, (550, 550))

click = False

# ------------ event loop -------------------------
while True:
    mx, my = pygame.mouse.get_pos()
    screen.fill(Variables.matcha)
    screen.blit(background, (0, 0))

    if Start.surf_rect.collidepoint((mx, my)):
        if click:
            # The continue_game file checks if the game has a save file or not
            # then continues if it does and the pet is not dead,
            # but doesn't continue the game if the pet is dead and starts a new one
            if not Death_Screen.dead:
                game_continue.continue_from_save()

            Main_Game.display_screen(screen, clock)
    if Settings.surf_rect.collidepoint((mx, my)):
        if click:
            Settings_Screen.display_screen(screen, clock)
    if Help.surf_rect.collidepoint((mx, my)):
        if click:
            Help_Screen.display_screen(screen, clock)

    # Title.draw_text()
    Variables.screen.blit(Title, (400, 200))
    Start.draw()
    Settings.draw()
    Help.draw()

    if Death_Screen.choice == 2:
        pygame.quit()
        sys.exit()
    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # ------------- Saving end_time if the user closed the game without starting it ---------------
            try:
                with open("end_time.txt") as end_file:
                    print("End file exists")
            except:
                end_time = datetime.datetime.now()
                end_time_save = end_time.strftime("%d/%m/%Y %H:%M:%S")
                with open("end_time.txt", "w") as end_file:
                    json.dump(end_time_save, end_file)
            # -------------------------------------------------------------------------
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    pygame.display.flip()
    clock.tick(60)
