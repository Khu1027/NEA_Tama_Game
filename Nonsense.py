# nonsense / random code that might be useful later

# ~~~~~~~~~~~~~~~~~~~~ From GAME Classes.py ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#random button things


if event.type == pygame.MOUSEBUTTONDOWN:
    new = collision_update()
#------ Checking Collisions and updating counter ------------------------------
# def count_update(self, stat, count, surf, rect, text)
# feed_new = feed.count_update("Hunger", hunger_count, hunger_text_surf, hunger_text_rect, hunger_text)

def collision_update():
    colli_stat = ["Hunger", "Health", "Happiness"]
    colli_center = [(640,50), (320,50), (960, 50)]
    colli_count = [hunger_count, health_count, happy_count]
    colli_surf = [hunger_text_surf, health_text_surf, happy_text_surf]
    colli_rect = [hunger_text_rect, health_text_rect, happy_text_rect]
    colli_text = [hunger_text, health_text, happy_text]

    for i in colli_rect:
        if colli_rect[i].collidepoint(event.pos):
            count = colli_count[i]
            surf = colli_surf[i]
            rect = colli_rect[i]
            center = colli_center[i]
            if count >= 0 and count <= 4:
                count = count + 1
            elif count == 5:
                print(f"The {colli_stat[i]} is already full")
            surf = game_font.render(colli_text[i], True, "Black")
            rect = surf.get_rect(center = center)
    return surf, rect, count

# --------------------- Feed Button ----------------------------
feed = Box([200,100], (640, 150), "Feed", (640, 150))
feed_button = feed.make_bar()
feed_button_surf, feed_button_rect = feed_button[0], feed_button[1]
feed_text = feed.make_text()
feed_text_surf, feed_text_rect = feed_text[0], feed_text[1]

def count_update(self, stat, count, surf, rect, text):
        if count >= 0 and count <= 4:
            count = count + 1
        elif count == 5:
            print(f"The {stat} is already full")
        surf = game_font.render(text, True, "Black")
        rect = surf.get_rect(center = self.text_center)
        return surf, text, count

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ From countdown timer.py ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#https://www.youtube.com/watch?v=E4Ih9mpn5tk
# creating a timer in pygame

#stats
hunger = 5
happiness = 5
health = 5
sick = False
dead = False
full = False

# keeps a measure of the time when the game starts
global start_time
global countdown_length
global hunger_static_point
global happiness_static_point
global health_static_point

start_time = time.time()
countdown_length = 30
hunger_static_point = time.time()
happiness_static_point = time.time()
health_static_point = time.time()

# class countdown:
#     def __init__(self, stat, static_point):
#         self.stat = stat
#         self.static_point = static_point
#         current_time = time.time()
#     def countdown(self):
#         if current_time - self.static_point >= countdown_length:
#             self.stat =-1
#             self.static_point = current_time

def countdown(stat, static_point):
    current_time = time.time()
    if current_time - static_point >= countdown_length:
        while stat >=0 and stat=< 5:
            stat = stat-1
            static_point = current_time
            return stat, static_point

def background_countdown():


# ----------------------------------- From Game_Time.py -------------------------------------------------------------------
# Evolution of the tamagotchi
# https://www.youtube.com/watch?v=k34KT-Z9ONM&list=PLmr34YByUWUf2wo5f0g1damQ86PfzH8XC&index=5
# https://www.geeksforgeeks.org/python-datetime-timedelta-function/
# https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings


import json
import time
from datetime import date, datetime, timedelta

time_now = datetime.now()
time_future = time_now + timedelta(days=5)
time_now_string = time_now.strftime("%d/%m/%Y %H:%M:%S")
time_future_string = time_future.strftime("%d/%m/%Y %H:%M:%S")

print(time_now_string)
print(time_future_string)

FMT = "%d/%m/%Y %H:%M:%S"

time_now = datetime.strptime(time_now_string, FMT)
time_future = datetime.strptime(time_future_string, FMT)
print(time_now)
print(time_future)
tdelta = time_future - time_now
total_time = tdelta.total_seconds()
minutes = total_time / 60
print(minutes)

# try:
#     with open('start_time.txt') as start_time_file:
#         start_time = json.load(start_time_file)
# except:
#     new_game = True
#     start_time = time_now
#     with open("start_time.txt", "wb") as start_time_file:
#         json.dump(start_time, start_time_file)


# #https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings
# s1 = '10:33:26'
# s2 = '11:15:49' # for example
# FMT = '%H:%M:%S'
# # this calculates it in terms of minutes
# tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
# print(tdelta)
# # ----------------------------------------------------------------