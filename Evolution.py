# Calculates the days that have passed and the evolution of the pet
import Game_Time
import Game_Files
from datetime import datetime

FMT = "%d/%m/%Y %H:%M:%S"


# start_time = Game_Time.start_time
# current_time = datetime.now().strptime("%d/%m/%Y %H:%M:%S")

class Evolution:
    def __init__(self):
        self.stage = Game_Files.evolution
        self.mortal = None
        self.penalties = None
        self.countdown = None
        self.display_day = None
        self.dead = None
        self.penalty_reset = False
        self.change_stage = False
        #self.change_stage_completed = False

        # Stage = the stage that the pet is at
        # Mortal = If the pet can die at this stage or not
        # Penalties = If penalties are to be calculated at this stage
        # Countdown = what length should the countdown be
        # Display_day = the day that will be displayed
        # Dead = If the pet is dead or not
        # Penalty Reset = To signify to the main code if the penalties should be reset or not
        # Change_Stage = A signifier that the pet has changed stage = saves penalty files so
        # that the evolution can be determined
        # Change_stage_completed = current solution for the files being saved being detected

    # First version of the count_penalties
    # def count_penalties(self):
    #     # This subroutine will first load all the new penalties and then add them to get the total penalties
    #     # The self.penalties will add up all the penalties that have accumulated so far
    #     hunger_penalty = Game_Files.load_count("hunger_penalty.txt")
    #     happiness_penalty = Game_Files.load_count("happiness_penalty.txt")
    #     health_penalty = Game_Files.load_count("health_penalty.txt")
    #     #print(happiness_penalty, hunger_penalty, health_penalty)
    #     self.penalties = (happiness_penalty + hunger_penalty + health_penalty)
    #     #print(self.penalties)

    def count_penalties(self):
        self.penalties = Game_Files.hunger_penalty + Game_Files.health_penalty + Game_Files.happiness_penalty
        print(self.penalties)


    def current_stage(self):
        # evolution over time calculating variables
        current = datetime.now()
        start = Game_Time.start_time
        day = Game_Time.current_day(current, start)
        minutes = Game_Time.calculate_minutes(current, start)
        seconds = Game_Time.calculate_seconds(current, start)
        self.display_day = day + 1

        if day == 0:
            if seconds < 30:
                self.stage = "Egg"
            else:
                self.stage = "Baby"
                # Changing the evolution stage to the updated one
                Game_Files.evolution = "Baby"

        elif day == 1:
            if self.stage == "Baby":
                self.change_stage = True
                # Code for playing the evolution animation
                self.stage = "Child"
                Game_Files.evolution = "Child"
                self.mortal = False
                #self.change_stage_completed = False

        elif day == 3:
            # self.stage = "Child"
            self.mortal = True

        elif day == 4:
            if self.stage == "Child":
                self.change_stage = True
                self.count_penalties()
                # Code for playing the evolution animation
                # Changing the type of teenager with the amount of penalties gained
                if 0 <= self.penalties < 75:
                    print(self.penalties)
                    self.stage = "TeenagerG"
                    Game_Files.evolution = "TeenagerG"
                elif 75 <= self.penalties:
                    print(self.penalties)
                    self.stage = "TeenagerB"
                    Game_Files.evolution = "TeenagerB"
                # resetting the penalties
                self.penalty_reset = True

        elif day >= 6:
            if self.stage == "TeenagerG" or self.stage == "TeenagerB":
                self.change_stage = True
                self.count_penalties()
                # Code for playing the evolution animation
                self.stage = "Adult"
                Game_Files.evolution = "Adult"
                # resetting the penalties
                self.penalty_reset = True


# ------------------------------ Attributes of Stages ---------------------------------------------
        # Giving each of the stages of the pet different attributes
        if self.stage == "Egg":
            self.mortal = False
            # self.penalties = False
            self.countdown = 1
            # the self.countdown should be 0 as in the user should be unable to feed the pet
            # however the subroutines do not work with float or NoneType so as a replacement
            # the countdown length is 1
        elif self.stage == "Baby":
            self.mortal = False
            # self.penalties = False
            self.countdown = 2
        elif self.stage == "Child":
            # self.penalties = True
            self.countdown = 3
        elif self.stage == "TeenagerG" or self.stage == "TeenagerB":
            self.mortal = True
            # self.penalties = True
            self.countdown = 4
        elif self.stage == "Adult":
            self.mortal = True
            # self.penalties = True
            self.countdown = 5
