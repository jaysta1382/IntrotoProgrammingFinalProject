#import libraries

import pygame
from PIL import Image
#intiliaize pygame
pygame.init()

#game window
WIDTH = 500
HEIGHT = 700

#create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JaystaJump')

# #open the image files
background = Image.open('background.png')

# #Display the image
# background.show()
# background = background.rotate(45)
# background.show()

#game loop
run = True
while run:
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
# initiates pygame and creates the window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jaysta Jump")
clock = pygame.time.Clock()