import Variables
import pygame
import sys
import New_Buttons
import Statistics
from datetime import datetime
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

# Rn the game just draws text saying start
Message = buttons.Button("This is where the main game will be", 200, 80, (550, 250))

def digital_clock():
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    d_clock = buttons.Button(current_time, 150, 50, (25, 25))
    d_clock.draw()

def display_stats():
    hunger_bar = buttons.Button(f"Hunger = {hunger}", 200, 50, (350, 25))
    happiness_bar = buttons.Button(f"Happiness = {happiness}", 200, 50, (575, 25))
    health_bar = buttons.Button(f"Health = {health}", 200, 50, (800, 25))
    hunger_bar.draw()
    happiness_bar.draw()
    health_bar.draw()

def display_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(Variables.matcha)

        Message.draw_text()
        digital_clock()
        display_stats()
        pygame.display.flip()
        clock.tick(60)