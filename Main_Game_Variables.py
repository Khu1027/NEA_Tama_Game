import pygame
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

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
buttons = New_Buttons
status_cords = (1000, 40)
pet_cords = (0, 0)
running = False

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

print(hunger_action.penalty)
print(health_action.penalty)
print(happiness_action.penalty)

# ------------- MAIN Pet evolution class object ------------------------
pet = Evolution.Evolution()
#print(pet.stage,pet.hunger_countdown)

# ------------- Action Buttons -----------------------------
feed_button = buttons.Button("Feed", 200, 75, (25, 275))
wash_button = buttons.Button("Wash", 200, 75, (25, 450))
play_button = buttons.Button("Play", 200, 75, (1055, 275))
heal_button = buttons.Button("Heal", 200, 75, (1055, 450))

# These are now unneeded as the images have replaced them
# settings_button = buttons.Button("S", 75, 75, (1180, 100))
# action_error_button = buttons.Button("You can't do that right now!", 500, 75, (550, 450))
settings_image = pygame.image.load("Pet Images/settings.png").convert()
s_img_height = settings_image.get_height()
s_img_width = settings_image.get_width()
settings_button = buttons.Button("S", s_img_width, s_img_height, (1180, 100))


# -------------- Status Meter / Pet Display ----------------------
def status_meter():
    if happiness_action.stat == 0:
        status = pygame.image.load("Pet Images/bored.png")
        Variables.screen.blit(status, status_cords)
    if hunger_action.stat == 0:
        status = pygame.image.load("Pet Images/hungry.png")
        Variables.screen.blit(status, status_cords)
    if health_action.stat == 0:
        status = pygame.image.load("Pet Images/dirty.png")
        Variables.screen.blit(status, status_cords)

        Variables.screen.blit(status, status_cords)
    if hunger_action.stat == 0 and happiness_action.stat == 0 and health_action.stat == 0:
        status = pygame.image.load("Pet Images/sad.png")
        Variables.screen.blit(status, status_cords)
    if hunger_action.stat > 0 and happiness_action.stat > 0 and health_action.stat > 0:
        status = pygame.image.load("Pet Images/neutral.png")
        Variables.screen.blit(status, status_cords)
    if hunger_action.stat == 5 and happiness_action.stat == 5 and health_action.stat == 5:
        status = pygame.image.load("Pet Images/happy.png")
        Variables.screen.blit(status, status_cords)

    if pet.sick:
        status = pygame.image.load("Pet Images/sick.png")
        Variables.screen.blit(status, status_cords)
    if pet.stage == "Egg":
        status = pygame.image.load("Pet Images/invalid.png")
        Variables.screen.blit(status, status_cords)


def pet_display():
    # Egg display
    if pet.stage == "Egg":
        pet_graphic = pygame.image.load("Pet Images/Egg.png")
        Variables.screen.blit(pet_graphic, pet_cords)
    # Baby display
    if pet.stage == "Baby":
        if hunger_action.stat > 0 or health_action.stat > 0 or happiness_action.stat > 0:
            pet_graphic = pygame.image.load("Pet Images/Baby_Normal.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if hunger_action.stat == 5 and happiness_action.stat == 5 and health_action.stat == 5:
            pet_graphic = pygame.image.load("Pet Images/Baby_Happy.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if (hunger_action.stat == 0 and happiness_action.stat == 0 and health_action.stat == 0) or pet.sick:
            pet_graphic = pygame.image.load("Pet Images/Baby_Sad.png")
            Variables.screen.blit(pet_graphic, pet_cords)

    # Child Display
    if pet.stage == "Child":

        if hunger_action.stat > 0 or health_action.stat > 0 or happiness_action.stat > 0:
            pet_graphic = pygame.image.load("Pet Images/Child_Normal.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if hunger_action.stat == 5 and happiness_action.stat == 5 and health_action.stat == 5:
            pet_graphic = pygame.image.load("Pet Images/Child_Happy.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if (hunger_action.stat == 0 and happiness_action.stat == 0 and health_action.stat == 0) or pet.sick:
            pet_graphic = pygame.image.load("Pet Images/Child_Sad.png")
            Variables.screen.blit(pet_graphic, pet_cords)
    # Teenager Display
    if pet.stage == "TeenagerG":
        if hunger_action.stat > 0 or health_action.stat > 0 or happiness_action.stat > 0:
            pet_graphic = pygame.image.load("Pet Images/TeenG_Normal.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if hunger_action.stat == 5 and happiness_action.stat == 5 and health_action.stat == 5:
            pet_graphic = pygame.image.load("Pet Images/TeenG_Happy.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if (hunger_action.stat == 0 and happiness_action.stat == 0 and health_action.stat == 0) or pet.sick:
            pet_graphic = pygame.image.load("Pet Images/TeenG_Sad.png")
            Variables.screen.blit(pet_graphic, pet_cords)
    if pet.stage == "TeenagerB":
        if hunger_action.stat > 0 or health_action.stat > 0 or happiness_action.stat > 0:
            pet_graphic = pygame.image.load("Pet Images/TeenB_Normal.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if hunger_action.stat == 5 and happiness_action.stat == 5 and health_action.stat == 5:
            pet_graphic = pygame.image.load("Pet Images/TeenB_Happy.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if (hunger_action.stat == 0 and happiness_action.stat == 0 and health_action.stat == 0) or pet.sick:
            pet_graphic = pygame.image.load("Pet Images/TeenB_Sad.png")
            Variables.screen.blit(pet_graphic, pet_cords)
    # Adult Display
    if pet.stage == "AdultA":
        if hunger_action.stat > 0 or health_action.stat > 0 or happiness_action.stat > 0:
            pet_graphic = pygame.image.load("Pet Images/A_A_Normal.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if hunger_action.stat == 5 and happiness_action.stat == 5 and health_action.stat == 5:
            pet_graphic = pygame.image.load("Pet Images/A_A_Happy.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if (hunger_action.stat == 0 and happiness_action.stat == 0 and health_action.stat == 0) or pet.sick:
            pet_graphic = pygame.image.load("Pet Images/A_A_Sad.png")
            Variables.screen.blit(pet_graphic, pet_cords)
    if pet.stage == "AdultB":
        if hunger_action.stat > 0 or health_action.stat > 0 or happiness_action.stat > 0:
            pet_graphic = pygame.image.load("Pet Images/A_B_Normal.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if hunger_action.stat == 5 and happiness_action.stat == 5 and health_action.stat == 5:
            pet_graphic = pygame.image.load("Pet Images/A_B_Happy.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if (hunger_action.stat == 0 and happiness_action.stat == 0 and health_action.stat == 0) or pet.sick:
            pet_graphic = pygame.image.load("Pet Images/A_B_Sad.png")
            Variables.screen.blit(pet_graphic, pet_cords)
    if pet.stage == "AdultC":
        if hunger_action.stat > 0 or health_action.stat > 0 or happiness_action.stat > 0:
            pet_graphic = pygame.image.load("Pet Images/A_C_Normal.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if hunger_action.stat == 5 and happiness_action.stat == 5 and health_action.stat == 5:
            pet_graphic = pygame.image.load("Pet Images/A_C_Happy.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if (hunger_action.stat == 0 and happiness_action.stat == 0 and health_action.stat == 0) or pet.sick:
            pet_graphic = pygame.image.load("Pet Images/A_C_Sad.png")
            Variables.screen.blit(pet_graphic, pet_cords)
    if pet.stage == "AdultD":
        if hunger_action.stat > 0 or health_action.stat > 0 or happiness_action.stat > 0:
            pet_graphic = pygame.image.load("Pet Images/A_D_Normal.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if hunger_action.stat == 5 and happiness_action.stat == 5 and health_action.stat == 5:
            pet_graphic = pygame.image.load("Pet Images/A_D_Happy.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if (hunger_action.stat == 0 and happiness_action.stat == 0 and health_action.stat == 0) or pet.sick:
            pet_graphic = pygame.image.load("Pet Images/A_D_Sad.png")
            Variables.screen.blit(pet_graphic, pet_cords)
    if pet.stage == "AdultE":
        if hunger_action.stat > 0 or health_action.stat > 0 or happiness_action.stat > 0:
            pet_graphic = pygame.image.load("Pet Images/A_E_Normal.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if hunger_action.stat == 5 and happiness_action.stat == 5 and health_action.stat == 5:
            pet_graphic = pygame.image.load("Pet Images/A_E_Happy.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if (hunger_action.stat == 0 and happiness_action.stat == 0 and health_action.stat == 0) or pet.sick:
            pet_graphic = pygame.image.load("Pet Images/A_E_Sad.png")
            Variables.screen.blit(pet_graphic, pet_cords)
    if pet.stage == "AdultF":
        if hunger_action.stat > 0 or health_action.stat > 0 or happiness_action.stat > 0:
            pet_graphic = pygame.image.load("Pet Images/A_F_Normal.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if hunger_action.stat == 5 and happiness_action.stat == 5 and health_action.stat == 5:
            pet_graphic = pygame.image.load("Pet Images/A_F_Happy.png")
            Variables.screen.blit(pet_graphic, pet_cords)
        if (hunger_action.stat == 0 and happiness_action.stat == 0 and health_action.stat == 0) or pet.sick:
            pet_graphic = pygame.image.load("Pet Images/A_F_Sad.png")
            Variables.screen.blit(pet_graphic, pet_cords)


# ------------ Subroutines ---------------------------------------
def digital_clock():
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M")
    d_clock = buttons.Button(current_time, 150, 50, (25, 25))
    d_clock.draw()


def display_stats():
    hunger_bar = buttons.Button(f"Hunger = {hunger_action.stat}", 200, 50, (320, 25))
    happiness_bar = buttons.Button(f"Happiness = {happiness_action.stat}", 200, 50, (770, 25))
    health_bar = buttons.Button(f"Health = {health_action.stat}", 200, 50, (545, 25))
    hunger_bar.draw()
    happiness_bar.draw()
    health_bar.draw()


def display_buttons():
    feed_button.draw()
    wash_button.draw()
    play_button.draw()
    heal_button.draw()
    settings_button.draw_image(settings_image)


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
    Game_Files.save_count((pet.sick, pet.sick_day), "sick.txt")
    # --- Saving immortality ----
    Game_Files.save_count(pet.immortal, "immortal.txt")


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

    pet.count_penalties()
    # print("hunger countdown = ", pet.hunger_countdown)
    # Sickness check

    if pet.stage != "Egg" and pet.stage != "Baby":
        # sick_time_lapse = (pet.display_day - (pet.last_sick_day + 1))
        # print(sick_time_lapse)
        if not pet.sick and pet.display_day >= pet.sick_day:
            #print("This process is working")
            pet.sick = True
            # the countdowns will decrease a little faster (health faster than the rest)
            pet.hunger_countdown = (3 / 4) * pet.hunger_countdown
            pet.happiness_countdown = (3 / 4) * pet.happiness_countdown
            pet.health_countdown = (2 / 3) * pet.health_countdown
            save_all()

            # This if statement is to check if 2 days have passed since the pet's assigned sick day,
            # this is so that if the game is continued from closing, then the game will check if the
            # pet died from illness or not
            if pet.display_day >= (pet.sick_day + 2):
                pet.dead = True
                pet.dead_reason = "sick"

        if pet.sick:
            # here the status bar will show the pet is sick
            print("Pet is sick!!")
            # If the pet has been sick for 2 days then it will be assigned as dead
            if pet.display_day >= (pet.sick_day + 2):
                if not pet.immortal:
                    pet.dead = True
                    pet.dead_reason = "sick"
            if pet.heal == 0:
                pet.sick = False
                # this will choose a day after the current day that the pet will become sick again.
                pet.sick_day = pet.display_day + random.randint(2, 4)
                print("Pet has been healed!")
                # returning countdowns to normal
                pet.hunger_countdown = pet.hunger_countdown / (3 / 4)
                pet.happiness_countdown = pet.happiness_countdown / (3 / 4)
                pet.health_countdown = pet.health_countdown / (2 / 3)
                pet.heal = random.randint(1, 3)
                save_all()


def mirror_penalties():
    print(hunger_action.penalty)
    print(health_action.penalty)
    print(happiness_action.penalty)
    # This saves the action penalties as the Game_Files penalties so that it can be used in
    # Evolution.py without any circular import errors
    Game_Files.hunger_penalty = hunger_action.penalty
    Game_Files.health_penalty = health_action.penalty
    Game_Files.happiness_penalty = happiness_action.penalty
