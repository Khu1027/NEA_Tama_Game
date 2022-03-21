import json
#import Main_Game
import time
from datetime import date, datetime, timedelta

time_now = datetime.now()
new_game = False
FMT = "%d/%m/%Y %H:%M:%S"

# ----------------- subroutines -------------------------------------

def calculate_minutes(current, start):
    time_diff = current - start
    total_time = time_diff.total_seconds()
    minutes = total_time / 60
    return minutes

def calculate_seconds(current, start):
    time_diff = current - start
    total_time = time_diff.total_seconds()
    return total_time

def calculate_days(minutes):
    days = minutes // 1
    # this is div operation. It returns the whole number value
    # In this case we are making each day last 24 minutes for testing. If the game was to run in real time...
    # one day would last 1440 minutes, so you would divide by 1440
    return days

def current_day(current, start):
    minutes = calculate_minutes(current, start)
    day = calculate_days(minutes)
    return day

# --------------------------------------------------------------------
try:
    with open('start_time.txt') as start_file:
        start_time = json.load(start_file)
    # returning the script variable to a datetime variable
    start_time = datetime.strptime(start_time, FMT)
    new_game = False
except:
    # This will be what alerts a new_game screen to load
    # after the new game sequence, then the time file will be made
    # formatting to script is necessary as the json file doesn't allow datetime variables
    start_time = time_now
    start_time_save = time_now.strftime("%d/%m/%Y %H:%M:%S")
    with open("start_time.txt", "w") as start_file:
        json.dump(start_time_save, start_file)
    # start the new game process
    # to do this you can create a variable that checks if the game is new or not
    new_game = True

