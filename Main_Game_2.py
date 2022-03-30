import pygame
import sys
from datetime import datetime
import random
import time
# python files
import Variables
import New_Buttons
import Game_Files
import Game_Time
import Actions
import Evolution
# game screens
import Settings_Screen
import Death_Screen

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

hunger_action = Actions.Action(hunger, hunger_static, "hunger", Game_Files.hunger_penalty)
happiness_action = Actions.Action(happiness, happiness_static, "happiness", Game_Files.happiness_penalty)
health_action = Actions.Action(health, health_static, "health", Game_Files.health_penalty)

# ------------- MAIN Pet evolution class object ------------------------
pet = Evolution.Evolution()
pet.current_stage()

# ------------- Action Buttons -----------------------------
feed_button = buttons.Button("Feed", 200, 75, (25, 275))
wash_button = buttons.Button("Wash", 200, 75, (25, 450))
play_button = buttons.Button("Play", 200, 75, (1055, 275))
heal_button = buttons.Button("Heal", 200, 75, (1055, 450))

settings_button = buttons.Button("S", 75, 75, (1180, 50))
action_error_button = buttons.Button("You can't do that right now!", 500, 75, (550, 450))


# -------------- Status Meter ---------------------------------


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
    settings_button.draw()


def display_day():
    day = int(pet.display_day)
    day_display = buttons.Button(f"Day: {day}", 150, 50, (25, 100))
    day_display.draw()


def display_pet(pet):
    pet_display = buttons.Button(pet.stage, 200, 80, (550, 350))
    pet_display.draw_text()


def decrease_count():
    hunger_action.decrease(pet.hunger_countdown)
    happiness_action.decrease(pet.happiness_countdown)
    health_action.decrease(pet.health_countdown)


def save_all():
    # --- Saving the statistic counts ---
    status = [hunger_action.stat, happiness_action.stat, health_action.stat]
    Game_Files.save_count(status, "pet_status.txt")
    # --- Saving the action button counts ---
    user_actions_2 = [Game_Files.feed, Game_Files.wash, Game_Files.play]
    Game_Files.save_count(user_actions_2, "user_actions.txt")
    # --- Saving the penalty points ---
    # Saving the Game_Files penalties as the action penalties
    mirror_penalties()
    # Saving penalties to txt files
    penalties = [Game_Files.hunger_penalty, Game_Files.happiness_penalty, Game_Files.health_penalty]
    Game_Files.save_count(penalties, "penalties.txt")
    # --- Saving Evolution_2 stage ---
    Game_Files.save_count((Game_Files.evolution, Game_Files.collective_stage), "evolution.txt")
    # --- Saving the ending time ---
    Game_Time.save_end_time()
    # --- Saving sick variables ---
    Game_Files.save_count((pet.sick, pet.last_sick_day, pet.sick_day), "sick.txt")


def pet_check():
    # Whenever the pet changes stages the files will save all the files (and the penalty)
    if pet.change_stage:
        save_all()
        pet.change_stage = False

    if pet.penalty_reset:
        hunger_action.penalty = 0
        happiness_action.penalty = 0
        health_action.penalty = 0
        pet.penalty_reset = False

    sick_time_lapse = (pet.display_day - (pet.last_sick_day + 1))
    if not pet.sick and sick_time_lapse == pet.sick_day:
        pet.sick = True
        # the countdowns will decrease a little faster (health faster than the rest)
        pet.hunger_countdown = 3 / 4 * pet.hunger_countdown
        pet.happiness_countdown = 3 / 4 * pet.happiness_countdown
        pet.health_countdown = 2 / 3 * pet.health_countdown

    if pet.sick:
        # here the status bar will show the pet is sick
        print("Pet is sick!!")
        if pet.display_day - pet.sick_day >= 3:
            pet.dead = True
        if pet.heal == 0:
            pet.sick = False
            pet.last_sick_day = (pet.display_day - 1)
            pet.sick_day = random.randint(1, 3)
            print("Pet has been healed!")
            # returning countdowns to normal
            pet.hunger_countdown = pet.hunger_countdown / (3 / 4)
            pet.happiness_countdown = pet.happiness_countdown / (3 / 4)
            pet.health_countdown = pet.health_countdown / (2 / 3)


def mirror_penalties():
    # This saves the action penalties as the Game_Files penalties so that it can be used in
    # Evolution.py without any circular import errors
    Game_Files.hunger_penalty = hunger_action.penalty
    Game_Files.health_penalty = health_action.penalty
    Game_Files.happiness_penalty = happiness_action.penalty


# ---------------------- Main Game Loop ----------------------------------------------

def display_screen():
    # https://www.youtube.com/watch?v=YOCt8nsQqEo&t=90s
    click = False
    running = True
    while running:
        if not pet.dead:
            mx, my = pygame.mouse.get_pos()
            screen.fill(Variables.matcha)

            if settings_button.surf_rect.collidepoint((mx, my)):
                if click:
                    save_all()
                    Settings_Screen.display_screen()

            if pet.stage != "Egg":
                if feed_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        # increase hunger by 1
                        hunger_action.increase()
                        Game_Files.feed += 1

                if wash_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        # increase health by 1
                        health_action.increase()
                        Game_Files.wash += 1

                if play_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        # increase happiness by 1
                        happiness_action.increase()
                        Game_Files.play += 1

                if heal_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        pet.heal -= 1
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

            mirror_penalties()
            pet.current_stage()
            pet_check()
            decrease_count()
            display_pet(pet)
            digital_clock()
            display_day()
            display_stats()
            display_buttons()

            click = False
        else:
            save_all()
            Death_Screen.display_screen()
            if Death_Screen.display_screen().choice == 1:
                pass
            elif Death_Screen.display_screen().choice == 1:
                running = False

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
