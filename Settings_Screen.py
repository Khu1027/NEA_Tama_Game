import pygame
import sys
import Main_Game_Variables
# python files
import New_Buttons
import Variables
import Game_Time
# import Game_Files
import game_continue
import Help_Screen

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
global music
buttons = New_Buttons
background = pygame.image.load("Pet Images/background_ss_hs.png")
Title = pygame.image.load("Pet Images/Settings Title.png")
music = "On"

# Rn the game just draws text saying start
# Message = buttons.Button("This is where the Settings Screen will be", 200, 80, (550, 70))
back_button = buttons.Button("Back", 120, 50, (1115, 635))

# ---------- Buttons --------------
save_and_quit = buttons.Button("Save and Quit", 200, 50, (575, 200))
help_screen = buttons.Button("Help", 200, 50, (575, 300))
music_button = buttons.Button(music, 200, 50, (575, 400))


music_text = buttons.Button("Music: ", 200, 50, (250, 400))
music_text.change_text_colour("#FFFFFF")
immortality_text = buttons.Button("Immortality: ", 250, 50, (200, 500))
immortality_text.change_text_colour("#FFFFFF")

reset_all = buttons.Button("Reset All", 200, 50, (575,600))
reset_all.change_colour("red")
# reset_all_warning_surf = buttons.Button("", 800, 500, (240, 110))
# reset_all_warning_1 = buttons.Button("Warning! This will reset all of your data and you will no longer have your pet.",600, 50, (40, 200))
# reset_all_warning_2 = buttons.Button("Do you still want to reset your data?", 600, 50, (40, 275))
# reset_yes = buttons.Button("YES", 200, 75, (200, 500))
# reset_no = buttons.Button("NO", 200, 75, (900, 500))

def display_screen(screen, clock):
    global music
    click = False
    running = True
    #main_game_running = Main_Game_Variables.running
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)
        screen.blit(background, (0,0))

        # Creating Immortality Button
        if not Main_Game_Variables.pet.immortal:
            immortality_button = buttons.Button("Off", 200, 50, (575, 500))
        else:
            immortality_button = buttons.Button("On", 200, 50, (575, 500))

        if music == "Off":
            music_button = buttons.Button("Off", 200, 50, (575, 400))
        else:
            music_button = buttons.Button("On", 200, 50, (575, 400))


        # Checking Collisions
        if back_button.surf_rect.collidepoint((mx, my)):
            if click:
                Game_Time.continue_game = True
                game_continue.continue_from_save()
                running = False
        if save_and_quit.surf_rect.collidepoint((mx, my)):
            if click:
                Main_Game_Variables.save_all()
                Main_Game_Variables.running = False
                running = False
        if help_screen.surf_rect.collidepoint((mx, my)):
            if click:
                Help_Screen.display_screen(screen, clock)
        if immortality_button.surf_rect.collidepoint((mx, my)):
            if click:
                print("This works")
                if not Main_Game_Variables.pet.immortal:
                    Main_Game_Variables.pet.immortal = True
                    print("Immortal is on")
                else:
                    Main_Game_Variables.pet.immortal = False
                    print("Immortal is off")
        if music_button.surf_rect.collidepoint((mx, my)):
            if click:
                print("This works")
                if music == "On":
                    music = "Off"
                elif music == "Off":
                    music = "On"
        if reset_all.surf_rect.collidepoint(((mx,my))):
            if click:
                # In future development, code for showing a pop up would be here
                Variables.delete_all_files()
                pygame.quit()
                sys.exit()

        Variables.screen.blit(Title, (325, 80))
        back_button.draw()
        save_and_quit.draw()
        help_screen.draw()
        music_text.draw_text()
        music_button.draw()
        immortality_text.draw_text()
        immortality_button.draw()
        reset_all.draw()
        #Message.draw_text()
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
