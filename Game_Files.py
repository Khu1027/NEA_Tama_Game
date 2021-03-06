import json
import random
import New_Buttons

buttons = New_Buttons

def save_count(count, file_name):
    with open(file_name, "w") as count_file:
        json.dump(count, count_file)

def load_count(count):
    with open(count) as count_file:
        new_count = json.load(count_file)
    return new_count

# All of these try, except statements checks if the file exists.
# If the file does exist it reassigns the variable the value that is in the file
# If the file does not exist it assigns it a value, then makes a new file and saves the data
# It is put into an array of similar variables and then saved into a txt file
# ------------- Pet_Status -----------------
try:
    with open("pet_status.txt") as status_file:
        status = json.load(status_file)
        if status == "delete":
            print("Entered delete txt file")
            hunger = 0
            happiness = 0
            health = 0
            status = [hunger, happiness, health]
            with open("pet_status.txt", "w") as status_file:
                json.dump(status, status_file)
        else:
            hunger = status[0]
            happiness = status[1]
            health = status[2]
except:
    hunger = 0
    happiness = 0
    health = 0
    status = [hunger, happiness, health]
    with open("pet_status.txt", "w") as status_file:
        json.dump(status, status_file)

# ------------- User_Actions -----------------
try:
    with open("user_actions.txt") as user_actions_file:
        user_actions = json.load(user_actions_file)
        if user_actions == "delete":
            print("Entered delete txt file")
            play = 0
            wash = 0
            feed = 0
            user_actions = [play, wash, feed]
            with open("user_actions.txt", "w") as user_actions_file:
                json.dump(user_actions, user_actions_file)
        else:
            play = user_actions[0]
            wash = user_actions[1]
            feed = user_actions[2]
except:
    play = 0
    wash = 0
    feed = 0
    user_actions = [play, wash, feed]
    with open("user_actions.txt", "w") as user_actions_file:
        json.dump(user_actions, user_actions_file)

# ------------- Penalties -----------------
try:
    with open("penalties.txt") as penalty_file:
        penalties = json.load(penalty_file)
        if penalties == "delete":
            print("Entered delete txt file")
            hunger_penalty = 0
            happiness_penalty = 0
            health_penalty = 0
            penalties = [hunger_penalty, happiness_penalty, health_penalty]
            with open("penalties.txt", "w") as penalty_file:
                json.dump(penalties, penalty_file)
        else:
            hunger_penalty = penalties[0]
            happiness_penalty = penalties[1]
            health_penalty = penalties[2]

except:
    hunger_penalty = 0
    happiness_penalty = 0
    health_penalty = 0
    penalties = [hunger_penalty, happiness_penalty, health_penalty]
    with open("penalties.txt", "w") as penalty_file:
        json.dump(penalties, penalty_file)

# --------- Evolution Stage ---------------
try:
    with open("evolution.txt") as evolution_file:
        try:
            evolution, collective_stage = json.load(evolution_file)
        except:
            evolution = json.load(evolution_file)
        if evolution == "delete":
            print("Entered delete txt file")
            evolution = "Egg"
            collective_stage = "Egg"
            with open("evolution.txt", "w") as evolution_file:
                json.dump((evolution, collective_stage), evolution_file)
except:
    evolution = "Egg"
    collective_stage = "Egg"
    with open("evolution.txt", "w") as evolution_file:
        json.dump((evolution, collective_stage), evolution_file)

# --------- sick Stage ---------------
try:
    with open("sick.txt") as sick_file:
        try:
            sick, sick_day = json.load(sick_file)
        except:
            sick = json.load(sick_file)
        if sick == "delete":
            print("Entered delete txt file")
            sick = False
            sick_day = random.randint(1, 4)
            with open("sick.txt", "w") as sick_file:
                json.dump((sick, sick_day), sick_file)
except:
    sick = False
    last_sick_day = 0
    sick_day = random.randint(1, 4)
    with open("sick.txt", "w") as sick_file:
        json.dump((sick, last_sick_day, sick_day), sick_file)

# --------- immortal Stage ---------------
try:
    with open("immortal.txt") as immortal_file:
        immortal = json.load(immortal_file)
        if immortal == "delete":
            immortal = False
            with open("immortal.txt", "w") as immortal_file:
                json.dump(immortal, immortal_file)
except:
    immortal = False
    with open("immortal.txt", "w") as immortal_file:
        json.dump(immortal, immortal_file)
