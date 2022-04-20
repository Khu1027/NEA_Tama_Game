import time
import New_Buttons
#import Game_Files
import Main_Game_Variables

buttons = New_Buttons

class Action:
    def __init__(self, stat, static_point, stat_name, penalty): # act_time
        self.stat = stat
        self.static_point = static_point
        self.penalty_static_point = static_point
        self.stat_name = stat_name
        self.warning = None
        self.penalty = penalty
        # penalty is being used as the exact Game_Files value


    def penalty_check(self):
            if 0 < self.stat <= 5:
                self.warning = False

            if self.stat == 0:
                if not self.warning:
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
