import time
import Buttons

# Notes:
# The act_time variable caused issues with the method running smoothly so it was removed.
# It may be added / changed later on if needed

class Action:
    def __init__(self, stat, static_point): # act_time
        self.stat = stat
        # act_time will tell us if the user has interacted with action
        # if they did then the corresponding action will be taken
        # self.act_time = act_time
        self.static_point = static_point

    def increase(self):
        # When the user interacts with a button and increases the statistic
        # For example the user clicks 'feed' and the 'hunger' increases by 1
        if 0 <= self.stat < 5:
            self.stat += 1
        # self.act_time = True

    def decrease(self, countdown_length):
        # countdown_length is the period in which the statistic should decrease by
        if 0 < self.stat <= 5:
            current_time = time.time()
            if current_time - self.static_point >= countdown_length:
                self.stat -=1
                self.static_point = current_time
            # if current_time - self.static_point >= countdown_length and not self.act_time:
            #     self.stat -= 1
            #     self.static_point = current_time
            # elif current_time - self.static_point >= countdown_length and self.act_time:
            #     self.stat -= 1
            #     self.static_point = current_time
