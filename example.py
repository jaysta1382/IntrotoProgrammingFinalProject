# RJ PROFETA'S VIDEOGAME: JAYSTA JUMP


##  SOURCES ##
# Microsoft Paint
# Mr. Cozort
# Scotty Francis
# Charile Premo 
# for inspo: https://www.youtube.com/watch?v=5FMPAt0n3Nc&list=LL&index=1&t=554s
# for outline: https://github.com/russs123/Jumpy
# for easy/understandable content:  http://kidscancode.org/blog/
# for inserting image: https://web.microsoftstream.com/video/b1bdbe8e-edc6-47a8-a2f9-c1aaf1b7930f
# for creating a high score: https://stackoverflow.com/questions/64696573/highscore-in-pygame-game

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
HEIGHT = 750

#set frame rate
clock = pg.time.Clock
FPS = 30

# global variablves
SCROLL_THRESH = 200
PLAYER_GRAV = 1.0
SCORE = 0
HIGHSCORE = 0
MAX_PLATFORMS = 10
scroll = 0
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
        self.image = pg.image.load(os.path.join(img_folder, 'link2.png')).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.inbounds = True
        self.flip = False
    # deines the controls of the players (only left and right)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x -= 5
            self.flip = False
        if keys[pg.K_d]:
            self.acc.x += 5
            self.flip = True
    def draw(self):
        screen.blit(self.image, self.rect)
        pg.draw.rect(screen, WHITE, self.rect, 2)
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
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
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
        self.image = pg.image.load(os.path.join(img_folder, 'platform2.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

















#instantiates the mob class
class Mob1(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image = pg.image.load(os.path.join(img_folder, 'rupee.png')).convert()
        self.image.set_colorkey(WHITE)
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 3*random.choice([-1,1])
        self.speedy = 3*random.choice([-1,1])
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
background = pg.image.load(os.path.join(img_folder, 'background2.png')).convert()
background_rect = background.get_rect() 

# creates groups to write code easier later
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()

# instantiates classes
player = Player()

# create randomly generated platforms
for p in range(MAX_PLATFORMS):
    p_w = random.randint(40,60)
    p_x = random.randint(0, WIDTH - p_w)
    p_y = p * random.randint(80,120)
    p_h = random.randint(0, 200)
    platform = Platform(p_x, p_y, p_w, p_h)
    all_plats.add(platform)

#defines the amount of mob classes displayed
for i in range(30):
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
all_plats.add()

# adds things to their respective groups
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

def show_go_screen():
    draw_text(screen, str(HIGHSCORE), 20, WIDTH / 2, 10)

# general game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)
    
    #PLAYER DRAW
    player.draw()
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
        
    # drawing a temprorary scroll threshold
    pg.draw.line(screen, BLACK, (0, SCROLL_THRESH), (WIDTH, SCROLL_THRESH))
    # update all sprites
    all_sprites.update()

    # draws the screen's bakcground 
    screen.fill(WHITE)
    screen.blit(background, (0,0))
    # draws the scoreboard (all the mobs hit)
    draw_text("JAYSTA JUMP",  70, BLACK, WIDTH/2, 15 )    
    draw_text("OBJECTIVE: SCORE 20 POINTS", 20, BLACK, 108, 65)
    draw_text("POINTS: " + str(SCORE), 20, BLACK, 41, 80)

    # draws all sprites
    all_sprites.draw(screen)
    all_plats.draw(screen)
    #if the scoreboard reaches 60, the game will quit and display that you wo
    if SCORE > HIGHSCORE:
            HIGHSCORE = SCORE
    if SCORE >= 20:
        draw_text("YOU'VE WON!!!!", 80, BLACK, WIDTH/2, HEIGHT/3)

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()