import pygame
import random
import math
from ship import Ship
from projectile import Projectile
from asteroid import Asteroid
from pygame import image as img


# declare constants
ASTEROID_RADIUS = 80
ASTEROID_SIZE = (2*ASTEROID_RADIUS, 2*ASTEROID_RADIUS)
WIN_HEIGHT = 800
WIN_WIDTH = 1200
WIN_CENTER = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
WHITE = (255,255,255)
#initialize pygame and window surface
pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Asteroids')

#text
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('SCORE:  ' + str(score), True, WHITE)
textRect = text.get_rect()
textRect.center = (80, 20)

#load images
spaceshipimglist = [img.load('sprites/spaceship0.png'), img.load('sprites/spaceship1.png'), img.load('sprites/spaceshipl.png'), img.load('sprites/spaceshipr.png')]
# asteroidimageList = [img.load('rock1.png'), img.load('rock2.png'), img.load('rock2.png'), img.load('rock2.png'), img.load('rock2.png')]
asteroidImage = img.load('sprites/pngguru.com.png')
asteroidImage = pygame.transform.scale(asteroidImage, ASTEROID_SIZE)

# create spaceship object and load sprites
spaceShip = Ship(win, 0, 0.1, 6, WIN_WIDTH/2 - 25, WIN_HEIGHT/2 - 25, False, False, False, WIN_WIDTH, WIN_HEIGHT, spaceshipimglist)
spaceShip.loadimg()

run = True
game_over = False
projectileTiming = 0
gameTime = 0

### rotation function ====================================
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
### ======================================================

### projectile creation and update =======================
projectiles = []
def projectileInit(object):
    projectiles.append(Projectile(win, WIN_WIDTH, WIN_HEIGHT, object.xpos + 25, object.ypos + 25, object.heading, object.velocity))

def projectileUpdate(asteroids):
    i = 0
    while ((i <len(projectiles)) & (len(projectiles) > 0)):
        projectiles[i].updateImg()

        if (not projectiles[i].inBound):
            projectiles.pop(i)
            if i > 1:
                i -= 1
        i += 1
### ======================================================


### collision detection

def collisionDetection():
    global projectiles, asteroids, score, run, game_over
    indexesi = []
    indexesj = []
    for i in range(len(asteroids)):
        for j in range(len(projectiles)):
            if (abs(projectiles[j].x - asteroids[i].center()[0]) < asteroids[i].radius) and (abs(projectiles[j].y - asteroids[i].center()[1]) < asteroids[i].radius):
                indexesi.append(i)
                indexesj.append(j)
                score += 1
    for ind in indexesj:
        projectiles.remove(projectiles[ind])
    for ind in indexesi:
        asteroids.remove(asteroids[ind])
    for i in range(len(asteroids)):
        if (abs(spaceShip.xpos + 36 - asteroids[i].center()[0]) < asteroids[i].radius + 20) and (abs(spaceShip.ypos + 36 - asteroids[i].center()[1]) < asteroids[i].radius + 20):
            game_over = True


### asteroids creation and update ========================
asteroids = []
def asteroidInit(surface, WIN_WIDTH, WIN_HEIGHT):
    asteroidRadius = random.randint(30, 80)
    asteroidSize = (2*asteroidRadius, 2*asteroidRadius)
    asteroidImageScaled = pygame.transform.scale(asteroidImage, asteroidSize)
    asteroidX = random.randint(0, WIN_WIDTH)
    asteroidY = random.randint(0, WIN_HEIGHT)
    if (abs((spaceShip.xpos + 36) - asteroidX) < 100):
        asteroidX += 100
    if (abs((spaceShip.ypos + 36) - asteroidY) < 100):
        asteroidY += 100

    asteroids.append(Asteroid(surface, WIN_WIDTH, WIN_HEIGHT, random.randint(0, 360), asteroidX, asteroidY, 2*random.random(), asteroidRadius, asteroidImageScaled))

def asteroidUpdate():
    i = 0
    while ((i < len(asteroids)) & (len(asteroids) > 0)):
        asteroids[i].updateImg()

        if (not asteroids[i].inBound):
            asteroids.pop(i)
            if i > 1:
                i -= 1
        i += 1

### ======================================================

### background ===========================================
### initialize x,y,r for background
bgx = []
bgy = []
bgr = []
for i in range(1000):
    bgx.append(random.randrange(5, WIN_WIDTH - 5, 1))
    bgy.append(random.randrange(5, WIN_HEIGHT - 5, 1))
    bgr.append(random.randrange(0, 3))

def drawBg():

    for i in range(1000):
        pygame.draw.circle(win, WHITE, (bgx[i], bgy[i]), bgr[i])
        partVel = 1
        bgy[i] += partVel
        if bgx[i] >= WIN_WIDTH:
            bgx[i] = 0
        if bgy[i] >= WIN_HEIGHT:
            bgy[i] = 0
        if bgx[i] < 0:
            bgx[i] = WIN_WIDTH
        if bgy[i] < 0:
            bgy[i] = WIN_HEIGHT

### ======================================================

### draw function=========================================
def drawScreen(shipimg, heading, posx, posy):
    global  text, textRect, game_over
    if not game_over:
        win.fill((0,0,0))
        drawBg()
        text = font.render('SCORE:  ' + str(score), True, WHITE)
        win.blit(text, textRect)
        shipimg = rot_center(shipimg, heading)
        win.blit(shipimg, (posx, posy))
        #pygame.draw.line(win, WHITE, WIN_CENTER, (WIN_WIDTH/2 + 100*math.cos(math.radians(heading)), WIN_HEIGHT/2 - 100*math.sin(math.radians(heading))))
        pygame.draw.circle(win, WHITE, (round(spaceShip.xpos) + 36, round(spaceShip.ypos) + 36), 4)
        spaceShip.move()
        asteroidUpdate()
        for i in range(len(asteroids)):
            asteroids[i].draw()
            pygame.draw.circle(win, WHITE, (round(asteroids[i].xpos + asteroids[i].radius), round(asteroids[i].ypos + asteroids[i].radius)), 5)
        if spaceShip.fire:
            projectileUpdate(asteroids)
    else:
        win.fill((0, 0, 0))
        text = font.render('GAME OVER, YOUR SCORE IS :  ' + str(score), True, WHITE)
        textRect = text.get_rect()
        textRect.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
        win.blit(text, textRect)
        esctoquit = font.render("PRESS ESCAPE TO EXIT", True, WHITE)
        escRect = esctoquit.get_rect()
        escRect.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 32)
        win.blit(esctoquit, escRect)


    pygame.display.update()
### ======================================================

### main function ========================================
while run:
    spaceShip.forward = False
    spaceShip.right = False
    spaceShip.left = False

    pygame.time.delay(10)
    projectileTiming = projectileTiming % 30
    if gameTime % 200 == 0:
        gameTime = 0
        asteroidInit(win, WIN_WIDTH, WIN_HEIGHT)

    #if (len(projectiles) > 0) and (len(asteroids) > 0):
    collisionDetection()

    # keypress handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys =  pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        spaceShip.rotate(-5)
        spaceShip.right = True
    if keys[pygame.K_LEFT]:
        spaceShip.rotate(5)
        spaceShip.left = True
    if keys[pygame.K_UP]:
        spaceShip.forward = True
    if keys[pygame.K_SPACE]:
        if projectileTiming > 15:
            spaceShip.fire = True
            projectileInit(spaceShip)
            projectileTiming = 0
    if keys[pygame.K_ESCAPE]:
        pygame.QUIT
        run = False



    projectileTiming += 1
    gameTime += 1


    drawScreen(spaceShip.image, spaceShip.heading, spaceShip.xpos, spaceShip.ypos)