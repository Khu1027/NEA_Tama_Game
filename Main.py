# ---------------- Import Variables -------------
import pygame
import sys
import time
import Variables
import Buttons
import Actions

# -------------- Initialising Variables -------------
pygame.init()
start_time = time.time()

# -------------- Setting the Environment -------------
pygame.display.set_caption("Tama")
screen = Variables.screen
clock = Variables.clock

# -------------- Main Code ----------------------------
# initialising the hunger statistics
hunger = 5
static_point = time.time()
feed_time = False

# initialising the center of the text that will be displayed
hunger_center = (640, 360)
hunger_text = Buttons.Button(hunger_center)
# initialising the hunger, static_point and feed_time
hunger_action = Actions.Action(hunger, static_point, feed_time)

# ------------ event loop -------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # increasing the hunger count by 1
                hunger_action.increase()

    # decreasing the hunger and displaying the hunger count
    hunger_action.decrease(1)
    text = f"Hunger: {hunger_action.stat}"

    screen.fill(Variables.matcha)
    hunger_text.get_text(text)
    pygame.display.flip()
    clock.tick(60)
