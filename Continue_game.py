import Game_Time
import Main_Game
import Game_Files
from datetime import datetime

FMT = "%d/%m/%Y %H:%M:%S"

global day_period
day_period = 60  # currently, one day is 60 seconds

continue_game = Game_Time.continue_game


# This subroutine checks how many countdowns occur before and after the evolution day
def evolution_countdowns(evolution_day, total_seconds, game_on_time, hunger_count, happiness_count, health_count):
    seconds_b4_evo = ((evolution_day * day_period) - game_on_time)
    seconds_after_evo = (total_seconds - (evolution_day * day_period))
    hunger_b4_evo = seconds_b4_evo // hunger_count
    happiness_b4_evo = seconds_b4_evo // happiness_count
    health_b4_evo = seconds_after_evo // health_count
    hunger_after_evo = seconds_after_evo // hunger_count
    happiness_after_evo = seconds_after_evo // happiness_count
    health_after_evo = seconds_after_evo // health_count

    return [hunger_b4_evo, happiness_b4_evo, health_b4_evo, hunger_after_evo, happiness_after_evo, health_after_evo]


# this subroutine decreases the status bars by the countdown periods and gives penalties when the status is 0
def decrease_and_penalty(status_countdown):
    hunger = status_countdown[0]
    happiness = status_countdown[1]
    health = status_countdown[2]
    # decreasing status'
    while Main_Game.hunger_action.stat != 0 or hunger != 0:
        Main_Game.hunger_action.stat -= 1
        hunger -= 1
    while Main_Game.happiness_action.stat != 0 or happiness != 0:
        Main_Game.happiness_action.stat -= 1
        happiness -= 1
    while Main_Game.health.stat != 0 or health != 0:
        Main_Game.health_action.stat -= 1
        health -= 1
    # giving penalties
    while hunger != 0:
        Main_Game.hunger_action.penalty += 1
        hunger -= 1
    while happiness != 0:
        Main_Game.happiness_action.penalty += 1
        happiness -= 1
    while health != 0:
        Main_Game.health_action.penalty += 1
        health -= 1

    Main_Game.mirror_penalties()


if continue_game:
    current_time = datetime.now()
    end_time = Game_Time.load_end_time()
    # Game_off_time = the seconds passed between closing the game and now reopening it
    game_off_time = Game_Time.calculate_seconds(current_time, end_time)
    # Game_on_time = the seconds passed between the start of a new file and the last closing of the game
    game_on_time = Game_Time.calculate_seconds(end_time, Game_Time.start_time)
    # End day = the day at which the game was closed
    end_day = Game_Time.current_day(end_time, Game_Time.start_time)
    # The current day in the game when it was reopened
    current_day = Game_Time.current_day(current_time, Game_Time.start_time)
    # Total seconds = the number of seconds since start of the game and the reopening
    total_seconds = Game_Time.calculate_seconds(current_time, Game_Time.start_time)

    # calculating how many times a 'countdown' occurred whilst the game was off
    hunger_count = game_off_time // Main_Game.pet.hunger_countdown
    happiness_count = game_off_time // Main_Game.pet.happiness_countdown
    health_count = game_off_time // Main_Game.pet.health_countdown

    stats_count_decrease = [hunger_count, happiness_count, health_count]

    # Calculating penalties given and any evolutions that occurred
    if 1 > current_day:
        if Main_Game.pet.collective_stage != "Baby":
            countdowns = evolution_countdowns(1, total_seconds, game_on_time, hunger_count, happiness_count, health_count)
            before_evo = [countdowns[0], countdowns[1], countdowns[2]]
            after_evo = [countdowns[3], countdowns[4], countdowns[5]]

            decrease_and_penalty(before_evo)
            # Giving new evolution 
            Main_Game.pet.collective_stage = "Baby"
            Main_Game.pet.stage = "Baby"
            # Changing the evolution stage to the updated one
            Game_Files.evolution = "Baby"

            decrease_and_penalty(after_evo)
        else:
            decrease_and_penalty(stats_count_decrease)

    elif 4 > current_day:
        if Main_Game.pet.collective_stage != "Child":
            countdowns = evolution_countdowns(1, total_seconds, game_on_time, hunger_count, happiness_count, health_count)
            before_evo = [countdowns[0], countdowns[1], countdowns[2]]
            after_evo = [countdowns[3], countdowns[4], countdowns[5]]
            
            decrease_and_penalty(before_evo)
            # Giving new evolution
            Main_Game.pet.collective_stage = "Child"
            Main_Game.pet.change_stage = True
            # Code for playing the evolution animation
            Main_Game.pet.stage = "Child"
            Game_Files.evolution = "Child"
            if current_day == 3:
                Main_Game.pet.mortal = True
            else:
                Main_Game.pet.mortal = False
                
            decrease_and_penalty(after_evo)
        else:
            decrease_and_penalty(stats_count_decrease)
            
    elif 6 > current_day:
        if Main_Game.pet.collective_stage != "Teenager":
            countdowns = evolution_countdowns(4, total_seconds, game_on_time, hunger_count, happiness_count, health_count)
            before_evo = [countdowns[0], countdowns[1], countdowns[2]]
            after_evo = [countdowns[3], countdowns[4], countdowns[5]]

            decrease_and_penalty(before_evo)
            # Giving new evolution
            Main_Game.pet.collective_stage = "Teenager"
            Main_Game.pet.count_penalties()
            # Code for playing the evolution animation
            # Changing the type of teenager with the amount of penalties gained
            if 0 <= Main_Game.pet.penalties < 75:
                print(Main_Game.pet.penalties)
                Main_Game.pet.stage = "TeenagerG"
                Game_Files.evolution = "TeenagerG"
            elif 75 <= Main_Game.pet.penalties:
                print(Main_Game.pet.penalties)
                Main_Game.pet.stage = "TeenagerB"
                Game_Files.evolution = "TeenagerB"
            # resetting the penalties
            Main_Game.pet.penalty_reset = True
            
            decrease_and_penalty(after_evo)
        else:
            decrease_and_penalty(stats_count_decrease)
            
    elif current_day >= 6:
        if Main_Game.pet.collective_stage != "Adult":
            countdowns = evolution_countdowns(6, total_seconds, game_on_time, hunger_count, happiness_count, health_count)
            before_evo = [countdowns[0], countdowns[1], countdowns[2]]
            after_evo = [countdowns[3], countdowns[4], countdowns[5]]

            decrease_and_penalty(before_evo)
            # Giving new evolution
            Main_Game.pet.collective_stage = "Adult"
            Main_Game.pet.count_penalties()
            Main_Game.pet.stage = Main_Game.pet.find_adult_evolution()
            Game_Files.evolution = Main_Game.pet.stage
            Main_Game.pet.penalty_reset = True
            
            decrease_and_penalty(after_evo)
        else:
            decrease_and_penalty(stats_count_decrease)
