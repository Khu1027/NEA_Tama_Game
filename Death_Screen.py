import pygame
import sys
import Variables
import New_Buttons

import Main_Game_Variables

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
buttons = New_Buttons
background = pygame.image.load("Pet Images/background_ds.png")
Title = pygame.image.load("Pet Images/Death Title.png")

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
    Message = buttons.Button(text_sick, 200, 75, (550, 550))
elif Main_Game_Variables.pet.dead_reason == "neglect":
    Message = buttons.Button(text_ignored, 200, 75, (550, 550))
elif Main_Game_Variables.pet.dead_reason == "old age":
    Message = buttons.Button(text_age, 200, 75, (550, 550))

New_Game_button = buttons.Button("New Game", 200, 75, (200, 500))
End_Game_button = buttons.Button("Quit Game", 200, 75, (900, 500))

choice = 0


def display_screen(screen, clock):
    click = False
    running = True
    global choice
    choice = 0
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)
        screen.blit(background, (0, 0))

        text_sick = """Your pet has passed away from illness."""
        text_ignored = """Your pet has passed away from neglect."""
        text_age = """Your pet has passed away from old age."""

        if Main_Game_Variables.pet.dead_reason == "sick":
            Message = buttons.Button(text_sick, 200, 75, (550, 300))
        elif Main_Game_Variables.pet.dead_reason == "neglect":
            Message = buttons.Button(text_ignored, 200, 75, (550, 300))
        elif Main_Game_Variables.pet.dead_reason == "old age":
            Message = buttons.Button(text_age, 200, 75, (550, 300))

        # The main game button doesn't work. write in evaluation
        # if New_Game_button.surf_rect.collidepoint((mx, my)):
        #     if click:
        #         choice = 1
        #         delete_all_files()
        #         running = False

        if End_Game_button.surf_rect.collidepoint((mx, my)):
            if click:
                choice = 2
                Variables.delete_all_files()
                pygame.quit()
                sys.exit()

        Variables.screen.blit(Title, (450,200))
        Message.draw_text()
        New_Game_button.draw()
        End_Game_button.draw()

        click = False

        for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            # The game will not let you quit unless you pick an option
            # pygame.quit()
            # sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()
        clock.tick(60)
