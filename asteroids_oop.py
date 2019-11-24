import pygame
import random
import math
from ship import Ship
from projectile import Projectile
from pygame import image as img


# set window size
winHeight = 800
winWidth = 1200

#initialize pygame and window surface
pygame.init()
win = pygame.display.set_mode((winWidth, winHeight))

#load images
spaceshipimglist = [img.load('spaceship0.png'), img.load('spaceship1.png'), img.load('spaceshipl.png'), img.load('spaceshipr.png')]
# asteroidimageList = [img.load('rock1.png'), img.load('rock2.png'), img.load('rock2.png'), img.load('rock2.png'), img.load('rock2.png')]


# create spaceship object and load sprites
spaceShip = Ship(win, 0, 0.1, 6, winWidth/2 - 25, winHeight/2 - 25, False, False, False, winWidth, winHeight, spaceshipimglist)
spaceShip.loadimg()

run = True

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
    projectiles.append(Projectile(win, winWidth, winHeight, object.xpos + 25, object.ypos + 25, object.heading, object.velocity))

def projectileUpdate():
    i = 0
    while ((i <len(projectiles)) & (len(projectiles) > 0)):
        projectiles[i].updateImg()
        if not projectiles[i].inBound:
            projectiles.pop(i)
            if i > 1:
                i -= 1
        i += 1
### ======================================================

### asteroids creation and update ========================
asteroids = []
def asteroidInit(surface, winWidth, winHeight, heading, xpos, ypos, velocity, radius, imageList):
    asteroids.append(Asteroid(surface, winWidth, winHeight, heading, xpos, ypos, velocity, radius, imageList))

def asteroidUpdate():
    pass




### ======================================================

### background ===========================================
### initialize x,y,r for background
bgx = []
bgy = []
bgr = []
for i in range(1000):
    bgx.append(random.randrange(5, winWidth - 5, 1))
    bgy.append(random.randrange(5, winHeight - 5, 1))
    bgr.append(random.randrange(0, 3))

def drawBg():

    for i in range(1000):
        pygame.draw.circle(win, (255,255,255), (bgx[i],bgy[i]), bgr[i])
        partVel = 1
        bgy[i] += partVel
        if bgx[i] >= winWidth:
            bgx[i] = 0
        if bgy[i] >= winHeight:
            bgy[i] = 0
        if bgx[i] < 0:
            bgx[i] = winWidth
        if bgy[i] < 0:
            bgy[i] = winHeight

### ======================================================

### draw function=========================================
def drawScreen(shipimg, heading, posx, posy):
    win.fill((0,0,0))
    drawBg()
    shipimg = rot_center(shipimg, heading)
    win.blit(shipimg, (posx, posy))

    spaceShip.move()
    if spaceShip.fire:
        projectileUpdate()



    pygame.display.update()
### ======================================================

### main function ========================================
while run:
    spaceShip.forward = False
    spaceShip.right = False
    spaceShip.left = False
    pygame.time.delay(10)

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
        spaceShip.fire = True
        projectileInit(spaceShip)
    if keys[pygame.K_ESCAPE]:
        pygame.QUIT
        run = False




    drawScreen(spaceShip.image, spaceShip.heading, spaceShip.xpos, spaceShip.ypos)
