import pygame
import os
import Game_Files

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 32)
white = (255,255,255)
matcha = (116, 141, 46)

def delete_all_files():
    try:
        os.remove("end_time.txt")
    except OSError as e:  # name the Exception `e`
        # failsafe if the files cannot be deleted
        Game_Files.save_count("delete", "end_time.txt")
    try:
        os.remove("evolution.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "evolution.txt")
    try:
        os.remove("immortal.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "immortal.txt")
    try:
        os.remove("penalties.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "penalties.txt")
    try:
        os.remove("pet_status.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "pet_status.txt")
    try:
        os.remove("sick.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "sick.txt")
    try:
        os.remove("start_time.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "start_time.txt")
    try:
        os.remove("user_actions.txt")
    except OSError as e:  # name the Exception `e`
        Game_Files.save_count("delete", "user_actions.txt")