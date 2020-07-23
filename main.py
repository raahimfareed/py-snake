import pygame
import random
import math

pygame.init()

window_size = (1280, 720)
window_bg_color = (20, 20, 20)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Test Game")

# Player
player_x = 50
player_y = 50
player_width = 20
player_height = 20
player_vel = 20
player_direction = "r"
player_color = (255, 0, 0)

# Food
food_x = random.randint(0, window_size[0])
food_y = random.randint(0, window_size[1])
# food_x = 60
# food_y = 60
# food_eaten = False
food_width = 20
food_height = 20
food_color = (255, 205, 86)


# Functions
def is_collision(x_1, y_1, x_2, y_2):
    print(x_1, x_2, y_1, y_2)
    print(math.pow(x_2 - x_1, 2))
    print(math.pow(y_2 - y_1, 2))
    print(math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2)))
    distance = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    print(distance)
    if distance < 20:
        return True
    else:
        return False


run = True

while run:
    print(f"Player X = {player_x}")
    print(f"Player Y = {player_y}")
    print(f"Food X = {food_x}")
    print(f"Food Y = {food_y}")
    eat_food = is_collision(player_x, food_x, player_y, food_y)
    # Slows down the loop
    pygame.time.delay(100)
    window.fill(window_bg_color)
    if eat_food:
        food_x = random.randint(0, window_size[0])
        food_y = random.randint(0, window_size[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    if keys[pygame.K_LEFT] and player_direction != "r":
        player_direction = "l"
    if keys[pygame.K_RIGHT] and player_direction != "l":
        player_direction = "r"
    if keys[pygame.K_UP] and player_direction != "d":
        player_direction = "u"
    if keys[pygame.K_DOWN] and player_direction != "u":
        player_direction = "d"

    if player_direction == "l":
        player_x -= player_vel
    if player_direction == "r":
        player_x += player_vel
    if player_direction == "u":
        player_y -= player_vel
    if player_direction == "d":
        player_y += player_vel

    if player_x < (0 - player_width):
        player_x = window_size[0] + player_width
    elif player_x > (window_size[0] + player_width):
        player_x = 0 - player_width

    if player_y < (0 - player_height):
        player_y = window_size[1] + player_height
    elif player_y > (window_size[1] + player_height):
        player_y = 0 - player_height

    pygame.draw.rect(window, food_color, (food_x, food_y, food_width, food_height))
    pygame.draw.rect(window, player_color, (player_x, player_y, player_width, player_height))

    pygame.display.update()

pygame.quit()
