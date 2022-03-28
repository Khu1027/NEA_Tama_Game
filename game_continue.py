import Game_Time
import Main_Game
import Game_Files
from datetime import datetime

continue_game = Game_Time.continue_game
global day_period, hunger_count, happiness_count, health_count


# ---- subroutines for calculating the decrease in status levels before and after evolution -----
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
    hunger = int(status_countdown[0])
    happiness = int(status_countdown[1])
    health = int(status_countdown[2])

    # taking away the hunger countdowns and giving penalties
    Main_Game.hunger_action.stat -= hunger
    if Main_Game.hunger_action.stat < 0:
        Main_Game.hunger_action.penalty = Main_Game.hunger_action.penalty - (Main_Game.hunger_action.stat + 1)
        Main_Game.hunger_action.stat = 0
    # taking away the happiness countdowns and giving penalties
    Main_Game.happiness_action.stat -= happiness
    if Main_Game.happiness_action.stat < 0:
        Main_Game.happiness_action.penalty = Main_Game.happiness_action.penalty - (Main_Game.happiness_action.stat + 1)
        Main_Game.happiness_action.stat = 0
    # taking away the health countdowns and giving penalties
    Main_Game.health_action.stat -= health
    if Main_Game.health_action.stat < 0:
        Main_Game.health_action.penalty = Main_Game.health_action.penalty - (Main_Game.health_action.stat + 1)
        Main_Game.health_action.stat = 0

    Main_Game.save_all()


# ---- Subroutines for all the evolutions (so that they can be reused for different situations ----
def egg_to_baby():
    Main_Game.pet.collective_stage = "Baby"
    Main_Game.pet.stage = "Baby"
    Game_Files.evolution = "Baby"

    Main_Game.save_all()


def baby_to_child(next_evo):
    previous_time = (1 * day_period) - game_on_time
    after_time = next_evo - previous_time
    # print(previous_time, after_time)
    before_evolution, after_evolution = evolution_countdowns(previous_time, after_time)
    # print("The before evo and after evo are: ", before_evolution, after_evolution)
    # Giving new evolution
    Main_Game.pet.collective_stage = "Child"
    Main_Game.pet.stage = "Child"
    Game_Files.evolution = "Child"

    decrease_and_penalty(after_evolution)


def child_to_teen(next_evo, off):
    # off is a variable that tells if the game was off for this period or not -> determine the teenager stage
    previous_time = (4 * day_period) - game_on_time
    after_time = next_evo - previous_time
    # print(previous_time, after_time)
    before_evolution, after_evolution = evolution_countdowns(previous_time, after_time)
    # print("The before evo and after evo are: ", before_evolution, after_evolution)

    decrease_and_penalty(before_evolution)
    # print(Main_Game.pet.penalties)
    Main_Game.pet.collective_stage = "Teenager"
    # Giving new evolution
    if not off:
        if 0 <= Main_Game.pet.penalties < 75:
            Main_Game.pet.stage = "TeenagerG"
            Game_Files.evolution = "TeenagerG"
        elif 75 <= Main_Game.pet.penalties:
            Main_Game.pet.stage = "TeenagerB"
            Game_Files.evolution = "TeenagerB"
    else:
        Main_Game.pet.stage = "TeenagerB"
        Game_Files.evolution = "TeenagerB"
    Main_Game.pet.penalty_reset = True
    Main_Game.pet_check()

    decrease_and_penalty(after_evolution)


def teen_to_adult(next_evo):
    # print("Entered the adult loop")
    previous_time = (6 * day_period) - game_on_time
    after_time = next_evo - previous_time
    before_evolution, after_evolution = evolution_countdowns(previous_time, after_time)
    # print("The before evo and after evo are: ", before_evolution, after_evolution)

    decrease_and_penalty(before_evolution)
    # Giving new evolution
    Main_Game.pet.collective_stage = "Adult"
    Main_Game.pet.count_penalties()
    Main_Game.pet.stage = Main_Game.pet.find_adult_evolution()
    Game_Files.evolution = Main_Game.pet.stage
    Main_Game.pet.penalty_reset = True
    Main_Game.pet_check()

    decrease_and_penalty(after_evolution)


# ------------------------------- Main game_continue function ----------------------------------------------
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
    # print("The variable counts are: ",stats_count_decrease)

    if current_day >= 6:
        # print("Entered day loop")
        # print(Main_Game.pet.collective_stage)
        if Main_Game.pet.collective_stage != "Adult" and Main_Game.pet.collective_stage == "Teenager":
            teen_to_adult(game_off_time)
        elif Main_Game.pet.collective_stage != "Adult" and Main_Game.pet.collective_stage == "Child":
            # at this stage the pet would be dead (if mortality was on)
            next_evo = (6 * day_period) - game_on_time
            off = False
            child_to_teen(next_evo, off)
            teen_to_adult(game_off_time)
        elif Main_Game.pet.collective_stage != "Adult" and Main_Game.pet.collective_stage == "Baby":
            # at this stage the pet would be dead (if mortality was on)
            next_evo = (4 * day_period) - game_on_time
            baby_to_child(next_evo)
            next_evo = (6 * day_period) - game_on_time
            off = True
            child_to_teen(next_evo, off)
            teen_to_adult(game_off_time)
        elif Main_Game.pet.collective_stage != "Adult" and Main_Game.pet.collective_stage == "Egg":
            # at this stage the pet would be dead (if mortality was on)
            egg_to_baby()
            next_evo = (4 * day_period) - game_on_time
            baby_to_child(next_evo)
            next_evo = (6 * day_period) - game_on_time
            off = True
            child_to_teen(next_evo, off)
            teen_to_adult(game_off_time)
        else:
            decrease_and_penalty(stats_count_decrease)
    # Teenager evolution
    elif 6 > current_day >= 4:
        if Main_Game.pet.collective_stage != "Teenager" and Main_Game.pet.collective_stage == "Child":
            off = False
            child_to_teen(game_off_time, off)
        elif Main_Game.pet.collective_stage != "Teenager" and Main_Game.pet.collective_stage == "Baby":
            # at this stage the pet would be dead (if mortality was on)
            next_evo = (4 * day_period) - game_on_time
            baby_to_child(next_evo)
            off = True
            child_to_teen(game_off_time, off)
        elif Main_Game.pet.collective_stage != "Teenager" and Main_Game.pet.collective_stage == "Egg":
            # at this stage the pet would be dead (if mortality was on)
            # teenager B is picked because as an egg/child there are no penalties given so no
            # real way of measuring the teenager type.
            egg_to_baby()
            next_evo = (4 * day_period) - game_on_time
            baby_to_child(next_evo)
            off = True
            child_to_teen(game_off_time, off)
        else:
            decrease_and_penalty(stats_count_decrease)
    # Child evolution
    elif 4 > current_day >= 1:
        if Main_Game.pet.collective_stage != "Child" and Main_Game.pet.collective_stage == "Baby":
            baby_to_child(game_off_time)
        elif Main_Game.pet.collective_stage != "Child" and Main_Game.pet.collective_stage == "Egg":
            # Egg already had all the status at 0 and no penalties so all that needs to happen is to change the stage
            # This is done in steps so that the correct penalties are given
            # hence next_evo_time is required so that the correct 'after_evolution' is calculated
            egg_to_baby()
            off = True
            baby_to_child(game_off_time, off)
        else:
            decrease_and_penalty(stats_count_decrease)
    # Baby evolution
    elif 60 > total_seconds >= 30:
        if Main_Game.pet.collective_stage != "Baby":
            egg_to_baby()
        else:
            decrease_and_penalty(stats_count_decrease)
