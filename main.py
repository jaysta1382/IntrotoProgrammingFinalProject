##SOURCES##
#RJ PROFETA
# Microsoft Paint
# Scotty Francis
# Mr. Cozort
# for inspo: https://www.youtube.com/watch?v=5FMPAt0n3Nc&list=LL&index=1&t=554s
# for help with python: https://www.youtube.com/watch?v=5FMPAt0n3Nc&list=LL&index=1&t=554s
# for easy/understandable content:  http://kidscancode.org/blog/
# for inserting image: https://www.sololearn.com/discuss/2499517/how-to-insert-image-in-python
#Import Settings file

# importing necessary libraries and modules
import pygame as pg
pg.init()
from pygame.sprite import Sprite
import random
from random import randint
import os

vec = pg.math.Vector2

# creates asset folders here
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')


# sets boundaries of the game window
WIDTH = 500
HEIGHT = 700
FPS = 30

# player settings
PLAYER_GRAV = 1.0
SCORE = 0

# defines colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 200, 255)

# sets the prerequisites for the text displayed on the window such as position etc
def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('underline')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)




# instantiates the player class
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        # creates the main character(link) by pulling file from an outside source and adding it to player sprite
        self.image = pg.image.load(os.path.join(img_folder, 'link.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    # keeps player from going off the screen 
    def boundscheck(self):
        if not self.rect.x > 0 or not self.rect.x < WIDTH:
            self.speedx *=-1
        if not self.rect.y > 0 or not self.rect.y < HEIGHT:
            self.speedy *= -1
    # deines the controls of the players (only left and right)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x -= 10
        if keys[pg.K_d]:
            self.acc.x += 10
    #allows the player class the ability to jump
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, all_plats, False)
        self.rect.x += -1
        if hits:
            self.vel.y = -20
    #constantly updates the player class
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # friction
        self.acc.x += self.vel.x * -0.1
        # self.acc.y += self.vel.y * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.rect.midbottom = self.pos
    # defines the player clss and platform interactions
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, all_plats, False)
            if hits:
                self.colliding = True
                self.hitx = hits[0].rect.centerx
                self.hity = hits[0].rect.centery
                xdiff = abs(self.rect.centerx - hits[0].rect.centerx)
                ydiff = abs(self.rect.centery - hits[0].rect.centery)
                # print("xdif " + str(xdiff))
                # print("ydif " + str(ydiff))
                if hits[0].rect.centerx > self.rect.centerx and xdiff > ydiff:
                    self.pos.x = hits[0].rect.left - self.rect.width/2
                if hits[0].rect.centerx < self.rect.centerx and xdiff > ydiff:
                    self.pos.x = hits[0].rect.right + self.rect.width/2
                self.vel.x = 0
                self.centerx = self.pos.x
                self.hitx = hits[0].rect.centerx
                self.hity = hits[0].rect.centery
            else:
                self.colliding = False
    
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, all_plats, False)
            if hits:
                self.colliding = True
                xdiff = abs(self.rect.centerx - hits[0].rect.centerx)
                ydiff = abs(self.rect.centery - hits[0].rect.centery)
                # print("xdif " + str(xdiff))
                # print("ydif " + str(ydiff))

                if hits[0].rect.centery > self.rect.centery and xdiff < ydiff:
                    self.pos.y = hits[0].rect.top - self.rect.height/2
                if hits[0].rect.centery < self.rect.centery and xdiff < ydiff:
                    self.pos.y = hits[0].rect.bottom + self.rect.height/2
                self.vel.y = 0
                self.centery = self.pos.y
                self.hitx = hits[0].rect.centerx
                self.hity = hits[0].rect.centery
            else:
                self.colliding = False

# instantiates the platform class
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


#instantiates the mob class
class Mob1(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.color = color
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 5*random.choice([-1,1])
        self.speedy = 5*random.choice([-1,1])
        self.inbounds = True
    #defines the mob class collision with walls
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, all_plats, False)
            if hits:
                xdiff = abs(self.rect.centerx - hits[0].rect.centerx)
                ydiff = abs(self.rect.centery - hits[0].rect.centery)
                if hits[0].rect.centerx > self.rect.centerx and xdiff > ydiff:
                    self.speedx *= -1
                if hits[0].rect.centerx < self.rect.centerx and xdiff > ydiff:
                    self.speedx *= -1
                self.hitx = hits[0].rect.centerx
                self.hity = hits[0].rect.centery

        if dir == 'y':
            hits = pg.sprite.spritecollide(self, all_plats, False)
            if hits:
                xdiff = abs(self.rect.centerx - hits[0].rect.centerx)
                ydiff = abs(self.rect.centery - hits[0].rect.centery)
                if hits[0].rect.centery > self.rect.centery and xdiff < ydiff:
                    self.speedy *= -1
                if hits[0].rect.centery < self.rect.centery and xdiff < ydiff:
                    self.speedy *= -1
                self.hitx = hits[0].rect.centerx
                self.hity = hits[0].rect.centery

    def boundscheck(self):
        if not self.rect.x > 0 or not self.rect.x < WIDTH:
            self.speedx *=-1
        if not self.rect.y > 0 or not self.rect.y < HEIGHT:
            self.speedy *= -1
    # constantly updates the mob class 
    def update(self):
        self.boundscheck()
        self.collide_with_walls('x')
        self.collide_with_walls('y')
        self.rect.x += self.speedx
        self.rect.y += self.speedy







# initiates pygame and creates the window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Jaysta Jump")
clock = pg.time.Clock()

# pulls the wanted background image rfom assets folder
background = pg.image.load(os.path.join(img_folder, 'background.png')).convert()
background_rect = background.get_rect() 


# creates groups to write code easier later
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()

# instantiates classes
player = Player()
#leve 1
plat2 = Platform(0, 690, 800, 30)
plat3 = Platform(400, 760, 200, 30)
plat4 = Platform(770, 760, 200, 30)


#defines the amount of mob classes displayed
for i in range(15):
    # instantiate mob class repeatedly
    m = Mob1(randint(0, WIDTH), randint(0,HEIGHT), 35, 35, (randint(0,255), randint(0,255) , randint(0,255)))
    all_sprites.add(m)
    mobs.add(m)
running = True 
while running:
    dt = clock.tick(FPS)

    for event in pg.event.get():
        if event.type ==pg.QUIT:
            running = False

        
# adds player to all sprites group
all_sprites.add(player)
all_plats.add(plat2, plat3, plat4)

# adds all platforms to the sprites group
all_sprites.add(plat2)
all_sprites.add(plat3)
all_sprites.add(plat4)


# adds things to their respective groups
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


# general game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)
    
    #defines the interactions between player class and mob class
    hits = pg.sprite.spritecollide(player, all_plats, False)
    if hits:
        player.pos.y = hits[0].rect.top
        player.vel.y = 0
    mobhits = pg.sprite.spritecollide(player, mobs, True)
    if mobhits:
        SCORE += 1

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()
    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
        # check for mouse
        
    # update all sprites
    all_sprites.update()

    screen.fill(WHITE)
    # draws the scoreboard (all the mobs hit)
    draw_text("JAYSTA JUMP",  80, BLACK, WIDTH / 2, HEIGHT / 38 )    
    draw_text("objective: score 60 points", 25, BLACK, WIDTH / 2, HEIGHT / 10)
    # draws all sprites
    all_sprites.draw(screen)
    #if the scoreboard reaches 60, the game will quit and display that you wo
    if SCORE >= 5:
        draw_text("you win bro!!!!", 100, RED, WIDTH/2, HEIGHT/4)

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()