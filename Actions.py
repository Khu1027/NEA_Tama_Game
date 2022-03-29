import time
import New_Buttons
#import Game_Files
import Main_Game_Variables

apples = 2

# Notes:
# The act_time variable caused issues with the method running smoothly so it was removed.
# It may be added / changed later on if needed
buttons = New_Buttons

class Action:
    def __init__(self, stat, static_point, stat_name, penalty): # act_time
        self.stat = stat
        # act_time will tell us if the user has interacted with action
        # if they did then the corresponding action will be taken
        # self.act_time = act_time
        self.static_point = static_point
        self.penalty_static_point = static_point
        self.stat_name = stat_name
        # Count = to ensure the penalty is not given for a count of 2
        self.warning = None
        self.penalty = penalty
        # penalty is being used as the exact Game_Files value


    def penalty_check(self):
            if 0 < self.stat <= 5:
                self.warning = False

            if self.stat == 0:
                if not self.warning:
                    warning = buttons.Button(f"Your pet's {self.stat_name} is low!", 500, 80, (550, 450))
                    warning.draw_text()
                    self.warning = True
                if self.warning:
                    self.penalty +=1
                #print(self.penalty)

    def increase(self):
        # When the user interacts with a button and increases the statistic
        # For example the user clicks 'feed' and the 'hunger' increases by 1
        if 0 <= self.stat < 5:
            self.stat += 1
        # self.act_time = True

    def decrease(self, countdown_length):
        # countdown_length is the period of time (in seconds) in which the statistic should decrease by

        current_time = time.time()
        penalty_time = time.time()
        if current_time - self.static_point >= countdown_length:
            if 0 < self.stat <= 5:
                self.stat -=1
                self.static_point = current_time

        if penalty_time - self.penalty_static_point >= countdown_length:
            # as the decrease function is working, it will check for any penalties that are given out
            if (Main_Game_Variables.pet.stage != "Egg") and (Main_Game_Variables.pet.stage != "Baby"):
                self.penalty_check()
                self.penalty_static_point = penalty_time
