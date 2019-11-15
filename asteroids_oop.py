import pygame
import random
import math
from klase import Ship
from pygame import image as img

winHeight = 600
winWidth = 800

pygame.init()
win = pygame.display.set_mode((winWidth, winHeight))

spaceShip = Ship(win, 0, 0.1, 6, winWidth/2, winHeight/2, False)
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


    pygame.display.update()
### ======================================================

### main function ========================================
while run:
    spaceShip.forward = False

    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys =  pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        spaceShip.rotate(-5)
    if keys[pygame.K_LEFT]:
        spaceShip.rotate(5)
    if keys[pygame.K_UP]:
        spaceShip.move()
    if not spaceShip.forward:
        spaceShip.velocity = 0.1
    if keys[pygame.K_RIGHT]:
        pass
    drawScreen(spaceShip.image, spaceShip.heading, spaceShip.xpos, spaceShip.ypos)
