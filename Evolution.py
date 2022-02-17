# Calculates the days that have passed and the evolution of the pet
import Game_Time
from datetime import datetime
FMT = "%d/%m/%Y %H:%M:%S"

# start_time = Game_Time.start_time
# current_time = datetime.now().strptime("%d/%m/%Y %H:%M:%S")

class Evolution:
    def __init__(self):
        self.stage = None
        self.death = None
        self.penalties = None
        self.countdown = None
        self.display_day = None
        # Stage = the stage that the pet is at
        # Death = If the pet can die at this stage or not
        # Penalties = If penalties are to be calculated at this stage
        # Countdown = what length should the countdown be
        # Display_day = the day that will be displayed

    def current_stage(self):
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
        elif day == 1 or day == 2:
            if self.stage == "Baby":
                # Code for playing the evolution animation
                pass
            self.stage = "Child"
        elif day == 3:
            self.stage = "Child"
            self.death = True
        elif day == 4 or day == 5:
            if self.stage == "Child":
                # Code for playing the evolution animation
                pass
            self.stage = "Teenager"
        elif day >= 6:
            if self.stage == "Teenager":
                # Code for playing the evolution animation
                pass
            self.stage = "Adult"

        # Giving each of the stages of the pet different attributes
        if self.stage == "Egg":
            self.death = False
            self.penalties = False
            self.countdown = 1
            # the self.countdown should be 0 as in the user should be unable to feed the pet
            # however the subroutines do not work with float or NoneType so as a replacement
            # the countdown length is 1
        elif self.stage == "Baby":
            self.death = False
            self.penalties = False
            self.countdown = 2
        elif self.stage == "Child":
            self.death = False
            self.penalties = True
            self.countdown = 3
        elif self.stage == "Teenager":
            self.death = True
            self.penalties = True
            self.countdown = 4
        elif self.stage == "Adult":
            self.death = True
            self.penalties = True
            self.countdown = 5
