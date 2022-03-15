import pygame
import sys
from datetime import datetime
import time
import Variables
import New_Buttons
import Game_Files
import Actions
import Evolution

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
pygame.display.set_caption("Tama")
screen = Variables.screen
clock = Variables.clock
buttons = New_Buttons

# -------------- Statistic counters --------------------
hunger = Game_Files.hunger
happiness = Game_Files.happiness
health = Game_Files.health

# ------------ Setting up Actions ------------------------
hunger_static = time.time()
happiness_static = time.time()
health_static = time.time()

hunger_action = Actions.Action(hunger, hunger_static, "hunger", "hunger_penalty.txt")
happiness_action = Actions.Action(happiness, happiness_static, "happiness", "happiness_penalty.txt")
health_action = Actions.Action(health, health_static, "health", "health_penalty.txt")

# ------------- MAIN Pet evolution class object ------------------------
pet = Evolution.Evolution()
pet.current_stage()

# ------------- Action Buttons -----------------------------
feed_button = buttons.Button("Feed", 200, 75, (25, 275))
wash_button = buttons.Button("Wash", 200, 75, (25, 450))
play_button = buttons.Button("Play", 200, 75, (1055, 275))
heal_button = buttons.Button("Heal", 200, 75, (1055, 450))

action_error_button = buttons.Button("You can't do that right now!", 500, 75, (550, 450))

# ------------ Subroutines ---------------------------------------
def digital_clock():
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    d_clock = buttons.Button(current_time, 150, 50, (25, 25))
    d_clock.draw()

def display_stats():
    hunger_bar = buttons.Button(f"Hunger = {hunger_action.stat}", 200, 50, (350, 25))
    happiness_bar = buttons.Button(f"Happiness = {happiness_action.stat}", 200, 50, (800, 25))
    health_bar = buttons.Button(f"Health = {health_action.stat}", 200, 50, (575, 25))
    hunger_bar.draw()
    happiness_bar.draw()
    health_bar.draw()

def display_buttons():
    feed_button.draw()
    wash_button.draw()
    play_button.draw()
    heal_button.draw()

def display_day():
    day = int(pet.display_day)
    day_display = buttons.Button(f"Day: {day}", 150, 50, (25, 100))
    day_display.draw()

def display_pet(pet):
    pet_display = buttons.Button(pet.stage, 200, 80, (550, 350))
    pet_display.draw_text()

def decrease_count():
    hunger_action.decrease(pet.countdown)
    happiness_action.decrease(pet.countdown)
    health_action.decrease(pet.countdown)

def save_all():
    # Saving the statistic counts
    Game_Files.save_count(hunger_action.stat, "hunger.txt")
    Game_Files.save_count(health_action.stat, "health.txt")
    Game_Files.save_count(happiness_action.stat, "happiness.txt")
    # Saving the action button counts
    Game_Files.save_count(Game_Files.feed, "feed.txt")
    Game_Files.save_count(Game_Files.wash, "wash.txt")
    Game_Files.save_count(Game_Files.play, "play.txt")
    # Saving the penalty points
    Game_Files.save_count(hunger_action.penalty, "hunger_penalty.txt")
    Game_Files.save_count(health_action.penalty, "health_penalty.txt")
    Game_Files.save_count(happiness_action.penalty, "happiness_penalty.txt")
    # Saving Evolution stage
    Game_Files.save_count(Game_Files.evolution, "evolution.txt")

def pet_check():
    # Whenever the pet changes stages the files will save all the files (and the penalty)
    if pet.change_stage:
        save_all()
        pet.change_stage_completed = True
        pet.change_stage = False

    if pet.penalty_reset:
        hunger_action.penalty = 0
        happiness_action.penalty = 0
        health_action.penalty = 0
        Game_Files.health_penalty = 0
        Game_Files.hunger_penalty = 0
        Game_Files.health_penalty = 0
        pet.penalty_reset = False

# ---------------------- Main Game Loop ----------------------------------------------

def display_screen():
    # https://www.youtube.com/watch?v=YOCt8nsQqEo&t=90s
    click = False
    running = True
    while running:

        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)

        if pet.stage != "Egg":
            if feed_button.surf_rect.collidepoint((mx, my)):
                if click:
                    # increase hunger by 1
                    hunger_action.increase()
                    Game_Files.feed +=1

            if wash_button.surf_rect.collidepoint((mx, my)):
                if click:
                    # increase health by 1
                    health_action.increase()
                    Game_Files.wash +=1

            if play_button.surf_rect.collidepoint((mx, my)):
                if click:
                    # increase happiness by 1
                    happiness_action.increase()
                    Game_Files.play +=1

            if heal_button.surf_rect.collidepoint((mx, my)):
                if click:
                    # check to see if the pet is infected
                    # if the pet is sick (random out of 3 to heal the pet)
                    # otherwise the pet is unable to be healed (error message is shown)
                    pass
        else:
            if feed_button.surf_rect.collidepoint((mx, my)):
                if click:
                    action_error_button.draw()
            if wash_button.surf_rect.collidepoint((mx, my)):
                if click:
                    action_error_button.draw()
            if play_button.surf_rect.collidepoint((mx, my)):
                if click:
                    action_error_button.draw()
            if heal_button.surf_rect.collidepoint((mx, my)):
                if click:
                    action_error_button.draw()

        pet.current_stage()
        #pet.count_penalties()
        decrease_count()
        pet_check()
        display_pet(pet)
        digital_clock()
        display_day()
        display_stats()
        display_buttons()


        click = False
        # -------------- event loop --------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_all()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_all()
                    running = False

        pygame.display.flip()
        clock.tick(60)