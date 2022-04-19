import Game_Time
import Main_Game_Variables
import Game_Files
from datetime import datetime


# global day_period, hunger_count, happiness_count, health_count

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
    hunger_decrease = int(status_countdown[0])
    happiness_decrease = int(status_countdown[1])
    health_decrease = int(status_countdown[2])

    print(Main_Game_Variables.hunger_action.penalty)
    print(Main_Game_Variables.health_action.penalty)
    print(Main_Game_Variables.happiness_action.penalty)

    # taking away the hunger countdowns and giving penalties
    Main_Game_Variables.hunger_action.stat -= hunger_decrease
    if Main_Game_Variables.hunger_action.stat < 0:
        print(Main_Game_Variables.hunger_action.penalty)
        # Here I am adding the penalties to the hunger_action penalty file. Because the stat is already negative, to add it to the penalties
        # the stat is taken away from the penalties ( -- = +)
        Main_Game_Variables.hunger_action.penalty = Main_Game_Variables.hunger_action.penalty - (
                    Main_Game_Variables.hunger_action.stat + 1)
        print(Main_Game_Variables.hunger_action.penalty)
        Main_Game_Variables.hunger_action.stat = 0
    # taking away the happiness countdowns and giving penalties
    Main_Game_Variables.happiness_action.stat -= happiness_decrease
    if Main_Game_Variables.happiness_action.stat < 0:
        print(Main_Game_Variables.health_action.penalty)
        Main_Game_Variables.happiness_action.penalty = Main_Game_Variables.happiness_action.penalty - (
                    Main_Game_Variables.happiness_action.stat + 1)
        print(Main_Game_Variables.health_action.penalty)
        Main_Game_Variables.happiness_action.stat = 0
    # taking away the health countdowns and giving penalties
    Main_Game_Variables.health_action.stat -= health_decrease
    if Main_Game_Variables.health_action.stat < 0:
        print(Main_Game_Variables.happiness_action.penalty)
        Main_Game_Variables.health_action.penalty = Main_Game_Variables.health_action.penalty - (
                    Main_Game_Variables.health_action.stat + 1)
        print(Main_Game_Variables.happiness_action.penalty)
        Main_Game_Variables.health_action.stat = 0

    Main_Game_Variables.save_all()
    print(Game_Files.hunger)
    print(Game_Files.happiness)
    print(Game_Files.health)


# ---- Subroutines for all the evolutions (so that they can be reused for different situations ----
def egg_to_baby():
    Main_Game_Variables.pet.collective_stage = "Baby"
    Main_Game_Variables.pet.stage = "Baby"
    Game_Files.evolution = "Baby"

    Main_Game_Variables.save_all()


def baby_to_child(next_evo):
    previous_time = (1 * day_period) - game_on_time
    after_time = next_evo - previous_time
    # print(previous_time, after_time)
    before_evolution, after_evolution = evolution_countdowns(previous_time, after_time)
    # print("The before evo and after evo are: ", before_evolution, after_evolution)
    # Giving new evolution
    Main_Game_Variables.pet.collective_stage = "Child"
    Main_Game_Variables.pet.stage = "Child"
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
    # print(Main_Game_Variables.pet.penalties)
    Main_Game_Variables.pet.collective_stage = "Teenager"
    # Giving new evolution
    if not off:
        Main_Game_Variables.pet.count_penalties()
        if 0 <= Main_Game_Variables.pet.penalties < 75:
            Main_Game_Variables.pet.stage = "TeenagerG"
            Game_Files.evolution = "TeenagerG"
        elif 75 <= Main_Game_Variables.pet.penalties or (
                (10 > Game_Files.feed) and (10 > Game_Files.play) and (10 > Game_Files.wash)):
            Main_Game_Variables.pet.stage = "TeenagerB"
            Game_Files.evolution = "TeenagerB"
    else:
        Main_Game_Variables.pet.stage = "TeenagerB"
        Game_Files.evolution = "TeenagerB"

    if not Main_Game_Variables.pet.immortal:
        Main_Game_Variables.pet.count_penalties()
        if Main_Game_Variables.pet.penalties > 80:
            Main_Game_Variables.pet.dead = True
            Main_Game_Variables.pet.dead_reason = "neglect"

    Main_Game_Variables.pet.penalty_reset = True
    Main_Game_Variables.pet_check()

    decrease_and_penalty(after_evolution)


def teen_to_adult(next_evo):
    # print("Entered the adult loop")
    previous_time = (6 * day_period) - game_on_time
    after_time = next_evo - previous_time
    before_evolution, after_evolution = evolution_countdowns(previous_time, after_time)
    # print("The before evo and after evo are: ", before_evolution, after_evolution)

    decrease_and_penalty(before_evolution)
    # Giving new evolution
    Main_Game_Variables.pet.collective_stage = "Adult"
    Main_Game_Variables.pet.count_penalties()
    Main_Game_Variables.pet.stage = Main_Game_Variables.pet.find_adult_evolution()
    Game_Files.evolution = Main_Game_Variables.pet.stage
    Main_Game_Variables.pet.penalty_reset = True
    Main_Game_Variables.pet_check()

    decrease_and_penalty(after_evolution)


# ------------------------------- Main game_continue function ----------------------------------------------
def continue_from_save():
    continue_game = Game_Time.continue_game
    Main_Game_Variables.pet.current_stage()
    if continue_game:
        Main_Game_Variables.pet.count_penalties()
        global day_period, hunger_count, happiness_count, health_count, game_on_time, game_off_time, end_day
        print("This process has been initiated BOOM")
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
        print(Main_Game_Variables.pet.stage, Main_Game_Variables.pet.hunger_countdown)
        hunger_count = game_off_time // Main_Game_Variables.pet.hunger_countdown
        happiness_count = game_off_time // Main_Game_Variables.pet.happiness_countdown
        health_count = game_off_time // Main_Game_Variables.pet.health_countdown

        stats_count_decrease = [hunger_count, happiness_count, health_count]
        # print("The variable counts are: ",stats_count_decrease)

        # --------- Adult Evolution -------------------
        if current_day >= 6:
            # print("Entered day loop")
            # print(Main_Game_Variables.pet.collective_stage)
            if Main_Game_Variables.pet.collective_stage != "Adult" and Main_Game_Variables.pet.collective_stage == "Teenager":
                teen_to_adult(game_off_time)
            elif Main_Game_Variables.pet.collective_stage != "Adult" and Main_Game_Variables.pet.collective_stage == "Child":
                # at this stage the pet would be dead (if mortality was on)
                next_evo = (6 * day_period) - game_on_time
                # checks if the time passed is less than 3 (so the pet wont be set to dead)
                if end_day >= 3 and current_day == 6:
                    off = False
                else:
                    off = True
                child_to_teen(next_evo, off)
                teen_to_adult(game_off_time)
            elif Main_Game_Variables.pet.collective_stage != "Adult" and Main_Game_Variables.pet.collective_stage == "Baby":
                # at this stage the pet would be dead (if mortality was on)
                next_evo = (4 * day_period) - game_on_time
                baby_to_child(next_evo)
                next_evo = (6 * day_period) - game_on_time
                off = True
                child_to_teen(next_evo, off)
                teen_to_adult(game_off_time)
                if not Main_Game_Variables.pet.immortal:
                    Main_Game_Variables.pet.dead = True
                    Main_Game_Variables.pet.dead_reason = "neglect"

            elif Main_Game_Variables.pet.collective_stage != "Adult" and Main_Game_Variables.pet.collective_stage == "Egg":
                # at this stage the pet would be dead (if mortality was on)
                egg_to_baby()
                next_evo = (4 * day_period) - game_on_time
                baby_to_child(next_evo)
                next_evo = (6 * day_period) - game_on_time
                off = True
                child_to_teen(next_evo, off)
                teen_to_adult(game_off_time)
                if not Main_Game_Variables.pet.immortal:
                    Main_Game_Variables.pet.dead = True
                    Main_Game_Variables.pet.dead_reason = "neglect"
            else:
                decrease_and_penalty(stats_count_decrease)
                # checking for death
                adult_death_period = current_day - end_day
                if adult_death_period > 3 or Main_Game_Variables.pet.penalties >= 100:
                    if not Main_Game_Variables.pet.immortal:
                        Main_Game_Variables.pet.dead = True
                        Main_Game_Variables.pet.dead_reason = "old age"

        # --------- Teenager Evolution -------------------
        elif 6 > current_day >= 4:
            if Main_Game_Variables.pet.collective_stage != "Teenager" and Main_Game_Variables.pet.collective_stage == "Child":
                off = False
                child_to_teen(game_off_time, off)
            elif Main_Game_Variables.pet.collective_stage != "Teenager" and Main_Game_Variables.pet.collective_stage == "Baby":
                # at this stage the pet would be dead (if mortality was on)
                next_evo = (4 * day_period) - game_on_time
                baby_to_child(next_evo)
                off = True
                child_to_teen(game_off_time, off)
                if not Main_Game_Variables.pet.immortal:
                    Main_Game_Variables.pet.dead = True
                    Main_Game_Variables.pet.dead_reason = "neglect"
            elif Main_Game_Variables.pet.collective_stage != "Teenager" and Main_Game_Variables.pet.collective_stage == "Egg":
                # at this stage the pet would be dead (if mortality was on)
                # teenager B is picked because as an egg/child there are no penalties given so no
                # real way of measuring the teenager type.
                egg_to_baby()
                next_evo = (4 * day_period) - game_on_time
                baby_to_child(next_evo)
                off = True
                child_to_teen(game_off_time, off)
                if not Main_Game_Variables.pet.immortal:
                    Main_Game_Variables.pet.dead = True
                    Main_Game_Variables.pet.dead_reason = "neglect"
            else:
                decrease_and_penalty(stats_count_decrease)

        # --------- Child Evolution -------------------
        elif 4 > current_day >= 1:
            if Main_Game_Variables.pet.collective_stage != "Child" and Main_Game_Variables.pet.collective_stage == "Baby":
                if 4 > current_day >= 3:
                    if not Main_Game_Variables.pet.immortal:
                        Main_Game_Variables.pet.dead = True
                        Main_Game_Variables.pet.dead_reason = "neglect"
                baby_to_child(game_off_time)
            elif Main_Game_Variables.pet.collective_stage != "Child" and Main_Game_Variables.pet.collective_stage == "Egg":
                # Egg already had all the status at 0 and no penalties so all that needs to happen is to change the
                # stage. This is done in steps so that the correct penalties are given hence next_evo_time is required
                # so that the correct 'after_evolution' is calculated
                if 4 > current_day >= 3:
                    if not Main_Game_Variables.pet.immortal:
                        Main_Game_Variables.pet.dead = True
                        Main_Game_Variables.pet.dead_reason = "neglect"
                egg_to_baby()
                off = True
                baby_to_child(game_off_time)
            else:
                # print("Stage = Child, decrease_and_penalty is at fault")
                decrease_and_penalty(stats_count_decrease)

        # --------- Baby Evolution -------------------
        elif 60 > total_seconds >= 30:
            if Main_Game_Variables.pet.collective_stage != "Baby":
                egg_to_baby()
            else:
                decrease_and_penalty(stats_count_decrease)
