
# importing libraries and modules
import pygame as pg
pg.init()
from pygame.sprite import Sprite
import random
import os
from random import randint

vec = pg.math.Vector2

# sets the game window
WIDTH = 500
HEIGHT = 700
FPS = 30


# #load images
# character = pg.image.load('game_folder/yunobo.png')
# bg_image = pg.image.load('game_folder/background.png').convert_alpha()


# #draw background
# screen.blit(character, (0,0))

# player settings
PLAYER_GRAV = 1.0
SCORE = 0

# defines colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 200, 255)
