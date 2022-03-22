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


class Main_Game:
    def __init__(self):

        # -------------- Statistic counters --------------------
        self.hunger = Game_Files.hunger
        self.happiness = Game_Files.happiness
        self.health = Game_Files.health

        # ------------ Setting up Actions ------------------------
        self.hunger_static = time.time()
        self.happiness_static = time.time()
        self.health_static = time.time()

        self.hunger_action = Actions.Action(self.hunger, self.hunger_static, "hunger", Game_Files.hunger_penalty)
        self.happiness_action = Actions.Action(self.happiness, self.happiness_static, "happiness", Game_Files.happiness_penalty)
        self.health_action = Actions.Action(self.health, self.health_static, "health", Game_Files.health_penalty)

        # ------------- MAIN Pet evolution class object ------------------------
        self.pet = Evolution.Evolution()
        self.pet.current_stage()

        # ------------- Action Buttons -----------------------------
        self.feed_button = buttons.Button("Feed", 200, 75, (25, 275))
        self.wash_button = buttons.Button("Wash", 200, 75, (25, 450))
        self.play_button = buttons.Button("Play", 200, 75, (1055, 275))
        self.heal_button = buttons.Button("Heal", 200, 75, (1055, 450))

        self.action_error_button = buttons.Button("You can't do that right now!", 500, 75, (550, 450))

    # ------------ Subroutines ---------------------------------------
    def digital_clock(self):
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        d_clock = buttons.Button(current_time, 150, 50, (25, 25))
        d_clock.draw()

    def display_stats(self):
        hunger_bar = buttons.Button(f"Hunger = {self.hunger_action.stat}", 200, 50, (350, 25))
        happiness_bar = buttons.Button(f"Happiness = {self.happiness_action.stat}", 200, 50, (800, 25))
        health_bar = buttons.Button(f"Health = {self.health_action.stat}", 200, 50, (575, 25))
        hunger_bar.draw()
        happiness_bar.draw()
        health_bar.draw()

    def display_buttons(self):
        self.feed_button.draw()
        self.wash_button.draw()
        self.play_button.draw()
        self.heal_button.draw()

    def display_day(self):
        day = int(self.pet.display_day)
        day_display = buttons.Button(f"Day: {day}", 150, 50, (25, 100))
        day_display.draw()

    def display_pet(self, pet):
        pet_display = buttons.Button(pet.stage, 200, 80, (550, 350))
        pet_display.draw_text()

    def decrease_count(self):
        self.hunger_action.decrease(self.pet.countdown)
        self.happiness_action.decrease(self.pet.countdown)
        self.health_action.decrease(self.pet.countdown)

    def save_all(self):
        # --- Saving the statistic counts ---
        status = [self.hunger_action.stat, self.happiness_action.stat, self.health_action.stat]
        Game_Files.save_count(status, "pet_status.txt")
        # --- Saving the action button counts ---
        user_Actions_2 = [Game_Files.feed, Game_Files.wash, Game_Files.play]
        Game_Files.save_count(user_Actions_2, "user_actions.txt")
        # --- Saving the penalty points ---
        # Saving the Game_Files penalties as the action penalties
        self.mirror_penalties()
        # Saving penalties to txt files
        penalties = [Game_Files.hunger_penalty, Game_Files.happiness_penalty, Game_Files.health_penalty]
        Game_Files.save_count(penalties, "penalties.txt")
        # --- Saving Evolution_2 stage ---
        Game_Files.save_count(Game_Files.evolution, "evolution.txt")

    def pet_check(self):
        # Whenever the pet changes stages the files will save all the files (and the penalty)
        if self.pet.change_stage:
            self.save_all()
            self.pet.change_stage = False

        if self.pet.penalty_reset:
            self.hunger_action.penalty = 0
            self.happiness_action.penalty = 0
            self.health_action.penalty = 0
            self.pet.penalty_reset = False

    def mirror_penalties(self):
        # This saves the action penalties as the Game_Files penalties so that it can be used in
        # Evolution.py without any circular import errors
        Game_Files.hunger_penalty = self.hunger_action.penalty
        Game_Files.health_penalty = self.health_action.penalty
        Game_Files.happiness_penalty = self.happiness_action.penalty

    # ---------------------- Main Game Loop ----------------------------------------------

    def display_screen(self):
        # https://www.youtube.com/watch?v=YOCt8nsQqEo&t=90s
        click = False
        running = True
        while running:

            mx, my = pygame.mouse.get_pos()
            screen.fill(Variables.matcha)

            if self.pet.stage != "Egg":
                if self.feed_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        # increase hunger by 1
                        self.hunger_action.increase()
                        Game_Files.feed += 1

                if self.wash_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        # increase health by 1
                        self.health_action.increase()
                        Game_Files.wash += 1

                if self.play_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        # increase happiness by 1
                        self.happiness_action.increase()
                        Game_Files.play += 1

                if self.heal_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        # check to see if the pet is infected
                        # if the pet is sick (random out of 3 to heal the pet)
                        # otherwise the pet is unable to be healed (error message is shown)
                        pass
            else:
                if self.feed_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        self.action_error_button.draw()
                if self.wash_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        self.action_error_button.draw()
                if self.play_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        self.action_error_button.draw()
                if self.heal_button.surf_rect.collidepoint((mx, my)):
                    if click:
                        self.action_error_button.draw()

            self.mirror_penalties()
            self.pet.current_stage()
            self.pet_check()
            self.decrease_count()
            self.display_pet(self.pet)
            self.digital_clock()
            self.display_day()
            self.display_stats()
            self.display_buttons()

            click = False
            # -------------- event loop --------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_all()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.save_all()
                        running = False

            pygame.display.flip()
            clock.tick(60)
