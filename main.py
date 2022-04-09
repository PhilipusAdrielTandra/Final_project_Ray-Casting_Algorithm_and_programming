import pygame
import sys
import math
from player import Player
from settings import*
from pygame import mixer
#map
map = (
    "########"
    "#    # #"
    "#      #"
    "###    #"
    "# #    #"
    "#      #"
    "#  #   #"
    "########"
)
#initialize pygame
pygame.init()
pygame.display.set_caption("RayCasting")
#relaxing music
mixer.music.load("music.mp3")
mixer.music.play(-1)
#player class from player.py
player = Player()
#function to draw on the screen, this has most of the things such as the player, their fov, the map and the ray shading
def draw_window():
    #calling class method
    player.movement()
    pygame.display.update()
    #update 2D background
    pygame.draw.rect(win, black, (0, 0, height, width))
    #3D floor
    pygame.draw.rect(win, grey, (480, height / 2, height, height))
    #3D ceiling
    pygame.draw.rect(win, light_grey, (480, -height / 2, height, height))
    draw_map()
    #player model
    pygame.draw.circle(win, blue, (int(player.x), int(player.y)), 8)
    #player direction
    pygame.draw.line(win, green, (player.x, player.y), (player.x - math.sin(player.angle) * 50, player.y + math.cos(player.angle) * 50), 3)
    #left eye visual limit
    pygame.draw.line(win, green, (player.x, player.y), (player.x - math.sin(player.angle - half_fov) * 50, player.y + math.cos(player.angle - half_fov) * 50), 3)
    #right eye visual limit
    pygame.draw.line(win, green, (player.x, player.y), (player.x - math.sin(player.angle + half_fov) * 50, player.y + math.cos(player.angle + half_fov) * 50), 3)
    cast_rays()

#ray casting algorithm
def cast_rays():
    start_angle = player.angle - half_fov
    #loop over rays
    for ray in range(casted_rays):
        #loop over depth
        for depth in range(max_depth):
            target_x = player.x - math.sin(start_angle) * depth
            target_y = player.y + math.cos(start_angle) * depth
            col = int(target_x / tile_size)
            row = int(target_y / tile_size)
            #calculate square index
            square = row * map_size + col
            if map[square] == "#":
                #highlight wall hit by ray
                pygame.draw.rect(win, green, (col * tile_size, row * tile_size, tile_size - 2, tile_size - 2))
                #draw casted rays
                pygame.draw.line(win, yellow, (player.x, player.y), (target_x, target_y))
                #calculate wall height
                wall_height = 21000 / (depth + 0.0001)
                #draw the 3d projection
                # Calculate brightness
                br = depth/max_depth
                brightness = (br*200, br*200, br*200)
                pygame.draw.rect(win, brightness, (height + ray * scale, (height / 2) - wall_height / 2, scale, wall_height))

                break
        #incremental rays
        start_angle += step_angle
#map function
def draw_map():
    #rows
    for row in range(8):
        #columns
        for col in range(8):
            #map square index
            square = row * map_size + col
            #drawing the map, if there is no #, the color changes to grey instead of white
            pygame.draw.rect(win, white if map[square] == "#" else dark_grey, (col * tile_size, row * tile_size, tile_size - 2, tile_size - 2))

#main game loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.flip()
    #calls draw_window function
    draw_window()
