import Variables
import pygame
import sys
import New_Buttons
import Game_Time
import game_continue
import Main_Game_Variables

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
buttons = New_Buttons

# Rn the game just draws text saying start
Message = buttons.Button("This is where the minigame Screen will be", 200, 80, (550, 250))
back_button = buttons.Button("Back", 120, 50, (1115, 635))

def display_screen(screen, clock):
    click = False
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)

        # Checking Collisions
        if back_button.surf_rect.collidepoint((mx, my)):
            if click:
                Game_Time.continue_game = True
                game_continue.continue_from_save()
                running = False

        back_button.draw()
        Message.draw_text()

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Main_Game_Variables.save_all()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Main_Game_Variables.save_all()
                    running = False

        pygame.display.flip()
        clock.tick(60)