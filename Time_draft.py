# Evolution of the tamagotchi
# https://www.youtube.com/watch?v=k34KT-Z9ONM&list=PLmr34YByUWUf2wo5f0g1damQ86PfzH8XC&index=5
# https://www.geeksforgeeks.org/python-datetime-timedelta-function/
# https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings


import json
import time
from datetime import date, datetime, timedelta

time_now = datetime.now()
time_future = time_now + timedelta(days= 5)
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
minutes = total_time/60
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
