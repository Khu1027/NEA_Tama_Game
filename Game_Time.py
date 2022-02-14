import json
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


def calculate_days(minutes):
    days = minutes // 24
    # this is div operation. It returns the whole number value
    # In this case we are making each day last 24 minutes for testing. If the game was to run in real time...
    # one day would last 1440 minutes, so you would divide by 1440
    return minutes

# --------------------------------------------------------------------

try:
    with open('start_time.txt') as start_file:
        start_time = json.load(start_file)
    # returning the script variable to a datetime variable
    start_time = datetime.strptime(start_time, FMT)
except:
    # formatting to script is necessary as the json file doesn't allow datetime variables
    start_time = time_now.strftime("%d/%m/%Y %H:%M:%S")
    with open("start_time.txt", "w") as start_file:
        json.dump(start_time, start_file)
    # start the new game process
    # to do this you can create a variable that checks if the game is new or not
    new_game = True

# Checks if the game is a new file or continued. it is checked if it's new by the main_pet file
# If the new_game = false then the time is calculated between the current time and the start time to give the days
if new_game == False:
    minutes_passed = calculate_minutes(time_now, start_time)
    days = calculate_days(minutes_passed)
