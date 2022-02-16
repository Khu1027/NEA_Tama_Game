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
feed = Statistics.feed
wash = Statistics.wash
play = Statistics.play

# Rn the game just draws text saying start
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
    hunger_bar = buttons.Button(f"Hunger = {hunger}", 200, 50, (350, 25))
    happiness_bar = buttons.Button(f"Happiness = {happiness}", 200, 50, (575, 25))
    health_bar = buttons.Button(f"Health = {health}", 200, 50, (800, 25))
    hunger_bar.draw()
    happiness_bar.draw()
    health_bar.draw()

def display_buttons():
    feed_button.draw()
    wash_button.draw()
    play_button.draw()
    heal_button.draw()

def save_all():
    Statistics.save_count(hunger)
    Statistics.save_count(health)
    Statistics.save_count(happiness)
    Statistics.save_count(feed)
    Statistics.save_count(play)
    Statistics.save_count(wash)

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
                pass
        if wash_button.surf_rect.collidepoint((mx, my)):
            if click:
                # increase health by 1
                pass
        if play_button.surf_rect.collidepoint((mx, my)):
            if click:
                # increase happiness by 1
                pass
        if heal_button.surf_rect.collidepoint((mx, my)):
            if click:
                # check to see if the pet is infected
                # if the pet is sick (random out of 3 to heal the pet)
                # otherwise the pet is unable to be healed (error message is shown)
                pass

        Message.draw_text()
        digital_clock()
        display_stats()
        display_buttons()

        click = False
        # -------------- event loop --------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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