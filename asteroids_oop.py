import pygame
import random
import math
from ship import Ship
from pygame import image as img

# set window size
winHeight = 800
winWidth = 1200

#initialize pygame and window surface
pygame.init()
win = pygame.display.set_mode((winWidth, winHeight))

# create spaceship object and load sprites
spaceShip = Ship(win, 0, 0.1, 6, winWidth/2 - 25, winHeight/2 - 25, False, winWidth, winHeight)
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
        spaceShip.projectileUpdate()



    pygame.display.update()
### ======================================================

### main function ========================================
while run:
    spaceShip.forward = False
    pygame.time.delay(10)

    # keypress handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys =  pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        spaceShip.rotate(-5)
    if keys[pygame.K_LEFT]:
        spaceShip.rotate(5)
    if keys[pygame.K_UP]:
        spaceShip.forward = True
    if keys[pygame.K_SPACE]:
        spaceShip.fire = True
        spaceShip.projectileInit()
    if keys[pygame.K_ESCAPE]:
        pygame.QUIT
        run = False




    drawScreen(spaceShip.image, spaceShip.heading, spaceShip.xpos, spaceShip.ypos)
