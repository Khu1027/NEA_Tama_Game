import json
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
# ------------- hunger -----------------
try:
    with open("hunger.txt") as hunger_file:
        hunger = json.load(hunger_file)

except:
    hunger = 0
    with open("hunger.txt", "w") as hunger_file:
        json.dump(hunger, hunger_file)

# ------------- happiness -----------------
try:
    with open("happiness.txt") as happiness_file:
        happiness = json.load(happiness_file)
except:
    happiness = 0
    with open("happiness.txt", "w") as happiness_file:
        json.dump(happiness, happiness_file)

# ------------- health -----------------
try:
    with open("health.txt") as health_file:
        health = json.load(health_file)
except:
    health = 0
    with open("health.txt", "w") as health_file:
        json.dump(health, health_file)

# ------------- play -----------------
try:
    with open("play.txt") as play_file:
        play = json.load(play_file)
except:
    play = 0
    with open("play.txt", "w") as play_file:
        json.dump(play, play_file)

# ------------- wash -----------------
try:
    with open("wash.txt") as wash_file:
        wash = json.load(wash_file)
except:
    wash = 0
    with open("wash.txt", "w") as wash_file:
        json.dump(wash, wash_file)

# ------------- feed -----------------
try:
    with open("feed.txt") as feed_file:
        feed = json.load(feed_file)
except:
    feed = 0
    with open("feed.txt", "w") as feed_file:
        json.dump(feed, feed_file)


# ------------- hunger_penalty -----------------
try:
    with open("hunger_penalty.txt") as hunger_penalty_file:
        hunger_penalty = json.load(hunger_penalty_file)
except:
    hunger_penalty = 0
    with open("hunger_penalty.txt", "w") as hunger_penalty_file:
        json.dump(hunger_penalty, hunger_penalty_file)


# ------------- happiness_penalty -----------------
try:
    with open("happiness_penalty.txt") as happiness_penalty_file:
        happiness_penalty = json.load(happiness_penalty_file)
except:
    happiness_penalty = 0
    with open("happiness_penalty.txt", "w") as happiness_penalty_file:
        json.dump(happiness_penalty, happiness_penalty_file)


# ------------- health_penalty -----------------
try:
    with open("health_penalty.txt") as health_penalty_file:
        health_penalty = json.load(health_penalty_file)
except:
    health_penalty = 0
    with open("health_penalty.txt", "w") as health_penalty_file:
        json.dump(health_penalty, health_penalty_file)

# --------- Evolution Stage ---------------
try:
    with open("evolution.txt") as evolution_file:
        evolution = json.load(evolution_file)
except:
    evolution = "Egg"
    with open("evolution.txt", "w") as evolution_file:
        json.dump(evolution, evolution_file)
