import time

import pygame
import sys
import random
import time

import Variables
import New_Buttons
import Game_Time
import Main_Game_Variables

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
buttons = New_Buttons

global game_happiness, shown_number, hidden_number
game_happiness = Main_Game_Variables.happiness_action.stat
shown_number = 0
hidden_number = 0

# Rn the game just draws text saying start
Message = buttons.Button("This is where the minigame Screen will be", 200, 80, (550, 250))
back_button = buttons.Button("Back", 120, 50, (1115, 635))
start_game = buttons.Button("Start_Game", 300, 50, (490, 335))
title = buttons.Button("Higher or Lower?", 500, 100, (390, 50))

# Checking answer
description = buttons.Button("Guess if the hidden card is higher or lower the one shown!", 1000, 50, (140, 200))
results_revealed_text = buttons.Button("And the answer is...", 300, 50, (540, 100))
results_higher = buttons.Button("Higher!", 200, 50, (540, 100))
results_lower = buttons.Button("Lower!", 200, 50, (540, 100))
correct_text = buttons.Button("Well done! You got it correct!", 600, 50, (540, 100))
incorrect_text = buttons.Button("Sorry! You got it incorrect!", 600, 50, (540, 100))
happiness_increased = buttons.Button("Your pet's happiness has increased!", 600, 50, (540, 575))

shown_card = buttons.Button("", 200, 400, (400, 200))
hidden_card = buttons.Button("", 200, 400, (820, 200))
higher = buttons.Button("Higher", 120, 50, (675, 180))
lower = buttons.Button("Lower", 120, 50, (675, 255))


def display_game_round(round_number):
    game_round = buttons.Button(f"Round: {round_number}/3", 200, 50, (320, 25))
    game_round.draw()


def display_status():
    happiness_status = buttons.Button(f"Happiness: {game_happiness}", 200, 50, (545, 25))
    happiness_status.draw()


def display_score(correct):
    score_box = buttons.Button(f"Score: {correct}", 200, 50, (770, 25))
    score_box.draw()


def update_status():
    global game_happiness
    if game_happiness < 4:
        game_happiness += 1
    happiness_status = buttons.Button(f"Happiness = {game_happiness}", 200, 50, (320, 25))
    happiness_status.draw()


def new_card_numbers():
    global shown_number, hidden_number
    shown_number = random.randint(1, 10)
    hidden_number = random.randint(1, 10)
    while shown_number == hidden_number:
        hidden_number = random.randint(1, 10)

def check_answer(correct_guess, answer, game_round):
    print("The check answer loop has been entered")
    if correct_guess:
        if answer == "Higher":
            results_revealed_text.draw_text()
            hidden_card.change_text(str(hidden_number))
            results_higher.draw_text()
        if answer == "Lower":
            results_revealed_text.draw_text()
            hidden_card.change_text(str(hidden_number))
            results_lower.draw_text()
        correct_text.draw_text()
        # Show pet happy (2 sec)
        new_card_numbers()
        game_round += 1
    elif not correct_guess:
        if answer == "Higher":
            results_revealed_text.draw_text()
            hidden_card.change_text(str(hidden_number))
            results_higher.draw_text()
        if answer == "Lower":
            results_revealed_text.draw_text()
            hidden_card.change_text(str(hidden_number))
            results_lower.draw_text()
        incorrect_text.draw_text()
        # Show pet sad (2 sec)
        new_card_numbers()
        game_round += 1

def event_loop(clock):
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


# -------------------- Minigame variables -------------------
def new_game(screen, clock):
    minigame_running = True
    # while game_running:
    game_click = False
    amount_correct = 0
    game_round = 0
    new_card_numbers()
    #
    # display_game_round(game_round)
    # display_status()
    # display_score(amount_correct)

    minigame_running = True
    while minigame_running:
        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)

        display_game_round(game_round)
        display_status()
        display_score(amount_correct)
        description.change_position((140,100))
        description.draw_text()

        if game_round != 4:

            # ---- Displaying the cards ---------
            shown_card.change_text(str(shown_number))
            shown_card.draw()
            # display back of hidden card
            hidden_card.draw()

            # ---- Displaying the buttons --------
            higher.draw()
            lower.draw()

            # correct_guess = None
            # answer = None

            # ------- Displaying the options ----------
            # if back_button.surf_rect.collidepoint((mx, my)):
            #     if game_click:
            #         back_click = True

            if higher.surf_rect.collidepoint((mx, my)):
                if game_click:
                    if hidden_number > shown_number:
                        correct_guess = True
                        amount_correct += 1
                    else:
                        correct_guess = False
                    answer = "Higher"
                    check_answer(correct_guess, answer, game_round)

            if lower.surf_rect.collidepoint((mx, my)):
                if game_click:
                    if hidden_number < shown_number:
                        correct_guess = True
                        amount_correct += 1
                    else:
                        correct_guess = False
                    answer = "Lower"
                    check_answer(correct_guess, answer, game_round)

            game_click = False
            event_loop(clock)

        if amount_correct >= 2:
            for i in amount_correct:
                update_status()
            Main_Game_Variables.happiness_action.stat = game_happiness
            happiness_increased.draw_text()
        game_running = False

        event_loop(clock)


def display_screen(screen, clock):
    click = False
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)

        title.draw()
        description.draw_text()
        back_button.draw()
        start_game.draw()

        # Checking Collisions
        if back_button.surf_rect.collidepoint((mx, my)):
            if click:
                Game_Time.continue_game = True
                running = False

        if start_game.surf_rect.collidepoint((mx, my)):
            if click:
                new_game(screen, clock)

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
