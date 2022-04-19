# Calculates the days that have passed and the evolution of the pet
import Game_Time
import Game_Files
from datetime import datetime
import random

FMT = "%d/%m/%Y %H:%M:%S"


# start_time = Game_Time.start_time
# current_time = datetime.now().strptime("%d/%m/%Y %H:%M:%S")

class Evolution:
    def __init__(self):
        self.stage = Game_Files.evolution
        self.collective_stage = Game_Files.collective_stage
        self.mortal = None
        self.penalties = None
        # countdowns
        self.hunger_countdown = None
        self.happiness_countdown = None
        self.health_countdown = None
        # other variables
        self.display_day = None
        self.immortal = Game_Files.immortal
        self.dead = None
        self.dead_reason = None
        # dead_reason = to personalise the death screen
        self.penalty_reset = False
        self.change_stage = False
        # sick variables
        self.sick = Game_Files.sick
        self.sick_day = Game_Files.sick_day
        self.heal = random.randint(1, 3)

        # Stage = the stage that the pet is at
        # Collective_stage = a variable which makes it easier to determine what stage the pet is at
        #   E.g. If i want to check if the pet is an adult, i can check the collective_stage "adult" and
        #   I do not need to check through every adult type
        # Mortal = If the pet can die at this stage or not
        # Penalties = If penalties are to be calculated at this stage
        # Countdown = what length should the countdown be
        # Display_day = the day that will be displayed
        # Dead = If the pet is dead or not
        # Penalty Reset = To signify to the main code if the penalties should be reset or not
        # Change_Stage = A signifier that the pet has changed stage = saves files
        # sick = tells whether the pet is sick or not
        # sick_day = calculates what day the pet will next be sick.
        # heal = chooses a random number of times the user needs to click heal

    def count_penalties(self):
        self.penalties = Game_Files.hunger_penalty + Game_Files.health_penalty + Game_Files.happiness_penalty
        #print(self.penalties)

    def find_adult_evolution(self):
        # This subroutine compares the different action buttons and then calculates which adult is the result
        play = Game_Files.play
        wash = Game_Files.wash
        feed = Game_Files.feed
        adult = 0
        new_evolution = ""

        if play > wash and play > feed:
            adult = 1
        elif play > wash and play == feed:
            adult = 1
        elif play > feed and play == wash:
            adult = 1

        elif wash > play and wash > feed:
            adult = 2
        elif wash > play and wash == feed:
            adult = 2
        elif wash > feed and wash == play:
            adult = 2

        elif feed > wash and feed > play:
            adult = 3
        elif feed > wash and feed == play:
            adult = 3
        elif feed > play and feed == wash:
            adult = 3
        elif feed == play == wash:
            adult = random.randint(1, 3)

        # This part then calculates which adult is chosen for each teenager type
        if self.stage == "TeenagerG":
            if adult == 1:
                new_evolution = "AdultA"
            elif adult == 2:
                new_evolution = "AdultB"
            else:
                new_evolution = "AdultC"
        elif self.stage == "TeenagerB":
            if adult == 1:
                new_evolution = "AdultD"
            elif adult == 2:
                new_evolution = "AdultE"
            elif adult == 3:
                new_evolution = "AdultF"
        return new_evolution

    def current_stage(self):
        #print("entered current stage loop")
        # evolution over time calculating variables
        current = datetime.now()
        start = Game_Time.start_time
        day = Game_Time.current_day(current, start)
        minutes = Game_Time.calculate_minutes(current, start)
        seconds = Game_Time.calculate_seconds(current, start)
        self.display_day = day + 1

        if day == 0:
            if seconds < 30:
                self.collective_stage = "Egg"
                self.stage = "Egg"
            else:
                self.collective_stage = "Baby"
                self.stage = "Baby"
                # Changing the evolution stage to the updated one
                Game_Files.evolution = "Baby"
                Game_Files.collective_stage = "Baby"

        elif day == 1:
            if self.stage == "Baby":
                self.collective_stage = "Child"
                self.change_stage = True
                # Code for playing the evolution animation
                self.stage = "Child"
                Game_Files.evolution = "Child"
                Game_Files.collective_stage = "Child"
                self.mortal = False


        elif day == 3:
            # self.stage = "Child"
            self.mortal = True
            self.count_penalties()

        elif day == 4:
            if self.stage == "Child":
                self.collective_stage = "Teenager"
                self.change_stage = True
                self.count_penalties()
                # Code for playing the evolution animation
                # Changing the type of teenager with the amount of penalties gained
                if 0 <= self.penalties < 75:
                    #print(self.penalties)
                    self.stage = "TeenagerG"
                    Game_Files.evolution = "TeenagerG"
                elif 75 <= self.penalties < 150:
                    #print(self.penalties)
                    self.stage = "TeenagerB"
                    Game_Files.evolution = "TeenagerB"
                elif 150 <= self.penalties:
                    if not self.immortal:
                        self.dead = True
                        self.dead_reason = "neglect"
                    else:
                        #print(self.penalties)
                        self.stage = "TeenagerB"
                        Game_Files.evolution = "TeenagerB"
                # resetting the penalties
                Game_Files.collective_stage = "Teenager"
                self.penalty_reset = True

        elif day >= 6:
            if self.collective_stage == "Teenager":
                self.collective_stage = "Adult"
                self.change_stage = True
                self.count_penalties()
                if not self.immortal:
                    if 0 <= self.penalties < 45:

                        self.stage = self.find_adult_evolution()
                        Game_Files.evolution = self.stage
                        Game_Files.collective_stage = "Adult"
                    else:
                        self.dead = True
                        self.dead_reason = "neglect"
                else:
                    self.collective_stage = "Adult"
                    self.change_stage = True
                    self.count_penalties()
                    self.stage = self.find_adult_evolution()
                    Game_Files.evolution = self.stage
                    Game_Files.collective_stage = "Adult"
                if self.collective_stage == "Adult":
                    if day / 3 == 0 and day != 6:
                        if self.penalties >= 100:
                            self.dead = True
                            self.dead_reason = "old age"
                            # resetting the penalties
                self.penalty_reset = True

        # ------------------------------ Attributes of Stages ---------------------------------------------
        # Giving each of the stages of the pet different attributes

        # Egg Stage
        if self.stage == "Egg":
            self.mortal = False
            # self.penalties = False
            self.hunger_countdown = 1
            self.happiness_countdown = 1
            self.health_countdown = 1
            # the self.countdown should be 0 as in the user should be unable to feed the pet
            # however the subroutines do not work with float or NoneType so as a replacement
            # the countdown length is 1

        #print("entered the current stage loop")
        #print(self.stage)
        #print(self.collective_stage)

        # Baby Stage
        if self.stage == "Baby":
            self.mortal = False
            # self.penalties = False
            self.hunger_countdown = 2
            self.health_countdown = 2
            self.happiness_countdown = 2
            self.penalties = 0

        # Child Stage
        if self.stage == "Child":
            # self.penalties = True
            self.hunger_countdown = 3
            self.happiness_countdown = 3
            self.health_countdown = 3
            self.count_penalties()

        # Teenager Stage
        if self.stage == "TeenagerG" or self.stage == "TeenagerB":
            self.count_penalties()
            self.mortal = True
            # self.penalties = True
            self.hunger_countdown = 4
            self.happiness_countdown = 4
            self.health_countdown = 4
            # Teenager G gets bored more quickly
            if self.stage == "TeenagerG":
                self.happiness_countdown = 3
            # Teenager B gets dirty and hunger more quickly
            elif self.stage == "TeenagerB":
                self.hunger_countdown = 3
                self.health_countdown = 3

        # Adult stage
        # Teenager G = all the stats decrease a little quicker
        if self.collective_stage == "Adult":
            self.count_penalties()
            if self.stage == "AdultA":
                self.mortal = True
                # Adult A gets bored more quickly
                self.hunger_countdown = 5
                self.happiness_countdown = 3
                self.health_countdown = 5
            elif self.stage == "AdultB":
                self.mortal = True
                # Adult B gets dirty more quickly
                self.hunger_countdown = 5
                self.happiness_countdown = 5
                self.health_countdown = 3
            elif self.stage == "AdultC":
                self.mortal = True
                # Adult C gets hungry more quickly
                self.hunger_countdown = 3
                self.happiness_countdown = 5
                self.health_countdown = 5

            # Teenager B = all the stats decrease a little slower
            elif self.stage == "AdultD":
                self.mortal = True
                # Adult D gets bored more quickly
                self.hunger_countdown = 6
                self.happiness_countdown = 5
                self.health_countdown = 6
            elif self.stage == "AdultE":
                self.mortal = True
                # Adult E gets dirty more quickly
                self.hunger_countdown = 6
                self.happiness_countdown = 6
                self.health_countdown = 5
            elif self.stage == "AdultF":
                print("entered this loop")
                self.mortal = True
                # Adult F gets hungry more quickly
                self.hunger_countdown = 5
                self.happiness_countdown = 6
                self.health_countdown = 6

            elif self.dead:
                self.mortal = True
                self.penalties = 0
                # countdowns
                self.hunger_countdown = 1
                self.happiness_countdown = 1
                self.health_countdown = 1
                # other variables
                self.immortal = Game_Files.immortal
                # dead_reason = to personalise the death screen
                self.penalty_reset = False
                self.change_stage = False