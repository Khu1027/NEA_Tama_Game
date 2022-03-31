import Variables
import pygame
import sys
import New_Buttons

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
# pygame.display.set_caption("Tama")
# screen = Variables.screen
# clock = Variables.clock
buttons = New_Buttons

# Rn the game just draws text saying start
Message = buttons.Button("This is where the Help Screen will be", 200, 80, (550, 250))


def display_screen(screen, clock):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(Variables.matcha)
        Message.draw_text()
        pygame.display.flip()
        clock.tick(60)
