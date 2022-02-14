#Main menu.py

import New_Buttons
import pygame
import sys
import Variables

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
pygame.display.set_caption("Tama")
screen = Variables.screen
clock = Variables.clock
buttons = New_Buttons

Title = buttons.Button("Tamagotchi!", 200, 80, (550, 100))
Start = buttons.Button("Start", 200, 80, (550, 250))
Options = buttons.Button("Options", 200, 80, (550, 400))
Help = buttons.Button("Help", 200, 80, (550, 550))

# ------------ event loop -------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(Variables.matcha)
    Title.draw()
    Start.draw()
    Options.draw()
    Help.draw()

    pygame.display.flip()
    clock.tick(60)