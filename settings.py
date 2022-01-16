import pygame
import math
#variables for the screen
height = 480
width = height * 2
win = pygame.display.set_mode((width, height))
map_size = 8
tile_size = int((width / 2) / map_size)
#ray casting variables
max_depth = 480
FOV = math.pi / 3
half_fov = FOV / 2
casted_rays = 120
step_angle = FOV / casted_rays
scale = (width / 2) / casted_rays
#pygame variables for fps and such
FPS = 60
clock = pygame.time.Clock()
#player variables
player_x = (width / 2) / 2
player_y = (width / 2) / 2
player_angle = math.pi
player_speed = 2
#colors
black = (0, 0, 0)
red = (220, 0 , 0)
blue = (0, 0, 220)
white = (255, 255, 255)
green = (0, 220, 0)
yellow = (255, 255, 0)
#bunch of greys
dark_grey = (169, 169, 169)
grey = (100, 100, 100)
light_grey = (200, 200, 200)
