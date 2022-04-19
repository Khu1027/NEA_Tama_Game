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
background = pygame.image.load("Pet Images/help background.png")
# Rn the game just draws text saying start
back_button = buttons.Button("Back", 120, 50, (1115, 635))

def display_screen(screen, clock):
    click = False
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)
        screen.blit(background, (0,0))

        # Checking Collisions
        if back_button.surf_rect.collidepoint((mx, my)):
            if click:
                # This checks if the end file has been made to then continue from
                # save file or to just end the event loop
                try:
                    with open("end_time.txt") as end_file:
                        Game_Time.continue_game = True
                        game_continue.continue_from_save()
                        running = False
                except:
                    running = False



        back_button.draw()

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
