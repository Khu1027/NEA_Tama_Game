import pygame
import sys
import os
import Variables
import New_Buttons
import Game_Files
import Game_Time

import Main_Game_Variables

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
buttons = New_Buttons
background = pygame.image.load("Pet Images/background_ds.png")

dead = False

if Main_Game_Variables.pet.dead:
    dead = True

try:
    open("end_file.txt", "r")
    continue_game = True
except:
    continue_game = False


text_sick = """Your pet has passed away from illness."""
text_ignored = """Your pet has passed away from neglect."""
text_age = """Your pet has passed away from old age."""

if Main_Game_Variables.pet.dead_reason == "sick":
    Message = buttons.Button(text_sick, 200, 75, (540, 350))
elif Main_Game_Variables.pet.dead_reason == "neglect":
    Message = buttons.Button(text_ignored, 200, 75, (540, 350))
elif Main_Game_Variables.pet.dead_reason == "old age":
    Message = buttons.Button(text_age, 200, 75, (540, 350))

New_Game_button = buttons.Button("New Game", 200, 75, (200, 500))
End_Game_button = buttons.Button("Quit Game", 200, 75, (900, 500))


def delete_all_files():
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


def display_screen(screen, clock):
    click = False
    running = True
    global choice
    choice = 0
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)
        screen.blit(background, (0,0))

        text_sick = """Your pet has passed away from illness."""
        text_ignored = """Your pet has passed away from neglect."""
        text_age = """Your pet has passed away from old age."""

        if Main_Game_Variables.pet.dead_reason == "sick":
            Message = buttons.Button(text_sick, 200, 75, (550, 250))
        elif Main_Game_Variables.pet.dead_reason == "neglect":
            Message = buttons.Button(text_ignored, 200, 75, (550, 250))
        elif Main_Game_Variables.pet.dead_reason == "old age":
            Message = buttons.Button(text_age, 200, 75, (550, 250))

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
