import pygame
from settings import*
import math
#player class
class Player:
    #attributes
    def __init__(self):
        self.x = player_x
        self.y = player_y
        self.angle = player_angle
    #player movement method
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_d]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_w]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.03
        if keys[pygame.K_RIGHT]:
            self.angle += 0.03
