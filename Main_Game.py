import pygame
import sys
# variables
import Main_Game_Variables
import Game_Files
import Game_Time
import Variables
import New_Buttons
# game screens
import Settings_Screen
import Death_Screen

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
# pygame.display.set_caption("Tama")
# screen = Variables.screen
# clock = Variables.clock
buttons = New_Buttons

# ---------------------- Main Game Loop ----------------------------------------------

def display_screen(screen, clock):
    # https://www.youtube.com/watch?v=YOCt8nsQqEo&t=90s
    click = False
    running = True
    while running:
        if not Main_Game_Variables.pet.dead:
            mx, my = pygame.mouse.get_pos()
            screen.fill(Variables.matcha)

            if Main_Game_Variables.settings_button.surf_rect.collidepoint((mx, my)):
                if click:
                    Main_Game_Variables.save_all()
                    Settings_Screen.display_screen(screen, clock)

            if Main_Game_Variables.pet.stage != "Egg":
                if Main_Game_Variables.feed_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        # increase hunger by 1
                        Main_Game_Variables.hunger_action.increase()
                        Game_Files.feed += 1

                if Main_Game_Variables.wash_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        # increase health by 1
                        Main_Game_Variables.health_action.increase()
                        Game_Files.wash += 1

                if Main_Game_Variables.play_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        # increase happiness by 1
                        Main_Game_Variables.happiness_action.increase()
                        Game_Files.play += 1

                if Main_Game_Variables.heal_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        Main_Game_Variables.pet.heal -= 1
                        # check to see if the pet is infected
                        # if the pet is sick (random out of 3 to heal the pet)
                        # otherwise the pet is unable to be healed (error message is shown)

            else:
                if Main_Game_Variables.feed_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        Main_Game_Variables.action_error_button.draw()
                if Main_Game_Variables.wash_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        Main_Game_Variables.action_error_button.draw()
                if Main_Game_Variables.play_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        Main_Game_Variables.action_error_button.draw()
                if Main_Game_Variables.heal_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        Main_Game_Variables.action_error_button.draw()

            Main_Game_Variables.mirror_penalties()
            Main_Game_Variables.pet.current_stage()
            Main_Game_Variables.pet_check()
            Main_Game_Variables.decrease_count()
            Main_Game_Variables.display_pet(Main_Game_Variables.pet)
            Main_Game_Variables.digital_clock()
            Main_Game_Variables.display_day()
            Main_Game_Variables.display_stats()
            Main_Game_Variables.display_buttons()

            click = False

        else:
            Main_Game_Variables.save_all()
            Death_Screen.display_screen(screen, clock)
            # if Death_Screen.choice == 1:
            #     running = False
            if Death_Screen.choice == 2:
                running = False

        # -------------- event loop --------------------
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
