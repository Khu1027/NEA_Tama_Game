import Game_Time
import Main_Game
import Game_Files
from datetime import datetime

continue_game = Game_Time.continue_game
global day_period, hunger_count, happiness_count, health_count


def evolution_countdowns(previous_time, after_time):
    hunger_b4_evo = previous_time // hunger_count
    happiness_b4_evo = previous_time // happiness_count
    health_b4_evo = previous_time // health_count
    hunger_after_evo = after_time // hunger_count
    happiness_after_evo = after_time // happiness_count
    health_after_evo = after_time // health_count

    before_evolution = [hunger_b4_evo, happiness_b4_evo, health_b4_evo]
    after_evolution = [hunger_after_evo, happiness_after_evo, health_after_evo]

    return before_evolution, after_evolution


def decrease_and_penalty(status_countdown):
    hunger = status_countdown[0]
    happiness = status_countdown[1]
    health = status_countdown[2]
    hunger_stat = Main_Game.hunger_action.stat
    happiness_stat = Main_Game.happiness_action.stat
    health_stat = Main_Game.health_action.stat
    hunger_penalty = Main_Game.hunger_action.penalty
    happiness_penalty = Main_Game.happiness_action.penalty
    health_penalty = Main_Game.health_action.penalty

    while hunger_stat != 0 or hunger != 0:
        hunger_stat -= 1
        hunger -= 1
    while happiness_stat != 0 or happiness != 0:
        happiness_stat -= 1
        happiness -= 1
    while health_stat != 0 or health != 0:
        health_stat -= 1
        health -= 1

    Main_Game.hunger_action.stat = hunger_stat
    Main_Game.happiness_action.stat = happiness_stat
    Main_Game.health_action.stat = health_stat

    while hunger != 0:
        hunger_penalty += 1
        hunger -= 1
    while happiness != 0:
        happiness_penalty += 1
        happiness -= 1
    while health != 0:
        health_penalty += 1
        health -= 1

    Main_Game.hunger_action.penalty = hunger_penalty
    Main_Game.happiness_action.penalty = hunger_penalty
    Main_Game.health_action.penalty = hunger_penalty
    Main_Game.save_all()


if continue_game:
    day_period = 60  # currently, one day is 60 seconds

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

    if current_day >= 6:
        if Main_Game.pet.collective_stage != "Adult":
            previous_time = (current_day * day_period) - game_on_time
            after_time = game_off_time - previous_time
            before_evolution, after_evolution = evolution_countdowns(previous_time, after_time)

            Main_Game.pet.penalty_reset = True
            Main_Game.pet_check()
            # Giving new evolution
            Main_Game.pet.collective_stage = "Adult"
            Main_Game.pet.count_penalties()
            Main_Game.pet.stage = Main_Game.pet.find_adult_evolution()
            Game_Files.evolution = Main_Game.pet.stage
            Main_Game.pet.penalty_reset = True

            decrease_and_penalty(after_evolution)
        else:
            decrease_and_penalty(stats_count_decrease)
    elif 6 > current_day >= 4:
        if Main_Game.pet.collective_stage != "Teenager":
            previous_time = (current_day * day_period) - game_on_time
            after_time = game_off_time - previous_time
            before_evolution, after_evolution = evolution_countdowns(previous_time, after_time)

            decrease_and_penalty(before_evolution)
            # Giving new evolution
            if 0 <= Main_Game.pet.penalties < 75:
                Main_Game.pet.stage = "TeenagerG"
                Game_Files.evolution = "TeenagerG"
            elif 75 <= Main_Game.pet.penalties:
                Main_Game.pet.stage = "TeenagerB"
                Game_Files.evolution = "TeenagerB"
            Main_Game.pet.penalty_reset = True
            Main_Game.pet_check()

            decrease_and_penalty(after_evolution)
        else:
            decrease_and_penalty(stats_count_decrease)
    elif 4 > current_day >= 1:
        if Main_Game.pet.collective_stage != "Child":
            previous_time = (current_day * day_period) - game_on_time
            after_time = game_off_time - previous_time
            before_evolution, after_evolution = evolution_countdowns(previous_time, after_time)
            # Giving new evolution
            Main_Game.pet.collective_stage = "Baby"
            Main_Game.pet.stage = "Baby"
            Game_Files.evolution = "Baby"

            decrease_and_penalty(after_evolution)
        else:
            decrease_and_penalty(stats_count_decrease)
    elif 1 > current_day >= 0:
        if Main_Game.pet.collective_stage != "Baby":
            Main_Game.pet.collective_stage = "Baby"
            Main_Game.pet.stage = "Baby"
            Game_Files.evolution = "Baby"
        else:
            decrease_and_penalty(stats_count_decrease)
