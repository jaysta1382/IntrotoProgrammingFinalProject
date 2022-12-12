import pygame
pygame.init()
from PIL import Image

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
jaysta_character = pygame.image.load('Kratos-Transparent-Image.png').convert_alpha()