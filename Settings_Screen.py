import pygame
import sys
import Main_Game_Variables
# python files
import New_Buttons
import Variables
import Game_Time
# import Game_Files
import game_continue

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
# pygame.display.set_caption("Tama")
# screen = Variables.screen
# clock = Variables.clock
buttons = New_Buttons

# Rn the game just draws text saying start
Message = buttons.Button("This is where the Settings Screen will be", 200, 80, (550, 70))
back_button = buttons.Button("Back", 120, 50, (1115, 635))


# warning_immortal =

def display_screen(screen, clock):
    click = False
    running = True
    main_menu_running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)

        # Creating Immortality Button
        if not Main_Game_Variables.pet.immortal:
            immortality_button = buttons.Button("Off", 200, 50, (575, 150))
        else:
            immortality_button = buttons.Button("On", 200, 50, (575, 150))

        # Checking Collisions
        if back_button.surf_rect.collidepoint((mx, my)):
            if click:
                Game_Time.continue_game = True
                game_continue.continue_from_save()
                running = False
        if immortality_button.surf_rect.collidepoint((mx, my)):
            if click:
                print("This works")
                if not Main_Game_Variables.pet.immortal:
                    Main_Game_Variables.pet.immortal = True
                    print("Immortal is on")
                else:
                    Main_Game_Variables.pet.immortal = False
                    print("Immortal is off")

        back_button.draw()
        immortality_button.draw()
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
