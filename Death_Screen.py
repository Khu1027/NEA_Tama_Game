import pygame
import sys
import random
import os
import Variables
import New_Buttons
import Game_Files
import Game_Time

import Main_Game_Variables

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
pygame.display.set_caption("Tama")
screen = Variables.screen
clock = Variables.clock
buttons = New_Buttons

dead = False

if Main_Game_Variables.pet.dead:
    dead = True

try:
    open("end_file.txt", "r")
    continue_game = True
except:
    continue_game = False


option = random.randint(1, 3)
text_sick = """Your pet has passed away from illness.
Please choose from the options below:"""
text_ignored = """Your pet has passed away from neglect.
Please choose from the options below:"""
text_age = """Your pet has passed away from old age.
Please choose from the options below: """

if option == 1:
    Message = buttons.Button(text_sick, 200, 75, (550, 250))
elif option == 2:
    Message = buttons.Button(text_ignored, 200, 75, (550, 250))
elif option == 3:
    Message = buttons.Button(text_age, 200, 75, (550, 250))

New_Game_button = buttons.Button("New Game", 200, 75, (100, 500))
End_Game_button = buttons.Button("Quit Game", 200, 75, (700, 500))

# def delete_all_files():
#     # os.remove(file)
#     # os.remove("end_time.txt")
#     # os.remove("evolution.txt")
#     # os.remove("immortal.txt")
#     # os.remove("penalties.txt")
#     # os.remove("\Users\User\Documents\Computer Science\NEA (Real)\NEA - comp version\python files\Game Mechanics\16.01.22 Code\Version 2\penalties.txt")
#     # os.remove("\Users\User\Documents\Computer Science\NEA (Real)\NEA - comp version\python files\Game Mechanics\16.01.22 Code\Version 2\pet_status.txt")
#     # os.remove("\Users\User\Documents\Computer Science\NEA (Real)\NEA - comp version\python files\Game Mechanics\16.01.22 Code\Version 2\sick.txt")
#     # os.remove("\Users\User\Documents\Computer Science\NEA (Real)\NEA - comp version\python files\Game Mechanics\16.01.22 Code\Version 2\start_time.txt")
#     # os.remove("\Users\User\Documents\Computer Science\NEA (Real)\NEA - comp version\python files\Game Mechanics\16.01.22 Code\Version 2\user_actions.txt")

def delete_all_files():
    # # need to close all files first to delete them
    # Main_Game_Variables.save_all()
    # Game_Time.start_file.close()
    # #Game_Time.end_file.close()
    # Game_Files.evolution_file.close()
    # Game_Files.immortal_file.close()
    # Game_Files.penalty_file.close()
    # Game_Files.status_file.close()
    # Game_Files.sick_file.close()
    # Game_Files.user_actions_file.close()

    try:
        os.remove("end_time.txt")
    except OSError as e:  # name the Exception `e`
        # failsafe if the files cannot be deleted
        Game_Files.save_count("delete", "end_time.txt")
    try:
        os.remove("evolution.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "evolution.txt")
    try:
        os.remove("immortal.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "immortal.txt")
    try:
        os.remove("penalties.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "penalties.txt")
    try:
        os.remove("pet_status.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "pet_status.txt")
    try:
        os.remove("sick.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "sick.txt")
    try:
        os.remove("start_time.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "start_time.txt")
    try:
        os.remove("user_actions.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "user_actions.txt")

choice = 0

def display_screen():
    click = False
    running = True
    global choice
    choice = 0
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)

        # The main game button doesn't work. write in evaluation

        # if New_Game_button.surf_rect.collidepoint((mx, my)):
        #     if click:
        #         choice = 1
        #         delete_all_files()
        #         running = False

        if End_Game_button.surf_rect.collidepoint((mx, my)):
            if click:
                choice = 2
                delete_all_files()
                running = False

        Message.draw_text()
        New_Game_button.draw()
        End_Game_button.draw()

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()
        clock.tick(60)
