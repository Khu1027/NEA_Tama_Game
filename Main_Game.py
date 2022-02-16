import pygame
import sys
from datetime import datetime
import time
import Variables
import New_Buttons
import Statistics
import Actions
import json

# -------------- Initialising Variables -------------
pygame.init()

# -------------- Setting the Environment -------------
pygame.display.set_caption("Tama")
screen = Variables.screen
clock = Variables.clock
buttons = New_Buttons

# -------------- Statistic counters --------------------

hunger = Statistics.hunger
happiness = Statistics.happiness
health = Statistics.health
feed = Statistics.feed
wash = Statistics.wash
play = Statistics.play

# ------------ Setting up Actions ------------------------
hunger_static = time.time()
happiness_static = time.time()
health_static = time.time()

hunger_action = Actions.Action(hunger, hunger_static)
happiness_action = Actions.Action(happiness, happiness_static)
health_action = Actions.Action(health, health_static)


# --------------- Rn the game just draws text saying start -------------
Message = buttons.Button("This is where the pet will be", 200, 80, (550, 350))

# ------------- Action Buttons -----------------------------
feed_button = buttons.Button("Feed", 200, 75, (25, 275))
wash_button = buttons.Button("Wash", 200, 75, (25, 450))
play_button = buttons.Button("Play", 200, 75, (1055, 275))
heal_button = buttons.Button("Heal", 200, 75, (1055, 450))


# ------------ Subroutines ---------------------------------------
def digital_clock():
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    d_clock = buttons.Button(current_time, 150, 50, (25, 25))
    d_clock.draw()

def display_stats():
    hunger_bar = buttons.Button(f"Hunger = {hunger_action.stat}", 200, 50, (350, 25))
    happiness_bar = buttons.Button(f"Happiness = {happiness_action.stat}", 200, 50, (575, 25))
    health_bar = buttons.Button(f"Health = {health_action.stat}", 200, 50, (800, 25))
    hunger_bar.draw()
    happiness_bar.draw()
    health_bar.draw()

def display_buttons():
    feed_button.draw()
    wash_button.draw()
    play_button.draw()
    heal_button.draw()

def decrease_count():
    hunger_action.decrease(2)
    happiness_action.decrease(2)
    health_action.decrease(2)

def save_all():
    Statistics.save_count(hunger_action.stat, "hunger.txt")
    Statistics.save_count(health_action.stat, "health.txt")
    Statistics.save_count(happiness_action.stat, "happiness.txt")
    Statistics.save_count(feed, "feed.txt")
    Statistics.save_count(play, "play.txt")
    Statistics.save_count(wash, "wash.txt")

# ---------------------- Main Game Loop ----------------------------------------------

def display_screen():
    click = False
    running = True
    while running:

        mx, my = pygame.mouse.get_pos()
        screen.fill(Variables.matcha)

        if feed_button.surf_rect.collidepoint((mx, my)):
            if click:
                # increase hunger by 1
                hunger_action.increase()

        if wash_button.surf_rect.collidepoint((mx, my)):
            if click:
                # increase health by 1
                health_action.increase()

        if play_button.surf_rect.collidepoint((mx, my)):
            if click:
                # increase happiness by 1
                happiness_action.increase()

        if heal_button.surf_rect.collidepoint((mx, my)):
            if click:
                # check to see if the pet is infected
                # if the pet is sick (random out of 3 to heal the pet)
                # otherwise the pet is unable to be healed (error message is shown)
                pass

        decrease_count()
        Message.draw_text()
        digital_clock()
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