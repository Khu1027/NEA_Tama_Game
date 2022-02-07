# Displaying the output to Pet.py

import pygame
import sys
import Variables

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
pygame.display.set_caption("Tama")
screen = Variables.screen
clock = Variables.clock


# ------------ event loop -------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(Variables.matcha)
    pygame.display.flip()
    clock.tick(60)