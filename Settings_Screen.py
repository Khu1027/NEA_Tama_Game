import pygame
import sys
# python files
import New_Buttons
import Variables
import Game_Time

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
pygame.display.set_caption("Tama")
screen = Variables.screen
clock = Variables.clock
buttons = New_Buttons

# Rn the game just draws text saying start
Message = buttons.Button("This is where the Settings Screen will be", 200, 80, (550, 250))
back_button = buttons.Button("Back", 120, 50, (1115, 635))


def display_screen():
    click = False
    running = True
    main_menu_running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)

        if back_button.surf_rect.collidepoint((mx, my)):
            if click:
                Game_Time.save_end_time()
                running = False

        back_button.draw()
        Message.draw_text()

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_Time.save_end_time()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Game_Time.save_end_time()
                    running = False

        pygame.display.flip()
        clock.tick(60)
