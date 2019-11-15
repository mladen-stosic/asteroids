import pygame
import random
import math
from pygame import image as img

pygame.init()

spaceShip = img.load('a-01.png')
spaceShip = pygame.transform.scale(spaceShip, (50, 50))

winHeight = 600
winWidth = 800
run = True
x = []
y = []
r = []
velocity = 0.1
forward = False
maxvelocity = 4
heading = 0
xpos = winWidth / 2
ypos = winHeight / 2

win = pygame.display.set_mode((winWidth, winHeight))
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
for i in range(1000):
    x.append(random.randrange(5, winWidth - 5, 1))
    y.append(random.randrange(5, winHeight - 5, 1))
    r.append(random.randrange(0, 3))

def drawBg():
    for i in range(1000):
        pygame.draw.circle(win, (255,255,255), (x[i],y[i]), r[i])
        partVel = 1
        y[i] += partVel
        if x[i] >= winWidth:
            x[i] = 0
        if y[i] >= winHeight:
            y[i] = 0
        if x[i] < 0:
            x[i] = winWidth
        if y[i] < 0:
            y[i] = winHeight

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
    forward = False

    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys =  pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        heading -= 5
    if keys[pygame.K_LEFT]:
        heading += 5
    if keys[pygame.K_UP]:
        if velocity < maxvelocity:
            xpos -= (math.cos(math.radians(heading) - (math.pi / 2))) * velocity
            ypos += (math.sin(math.radians(heading) - (math.pi / 2))) * velocity
            velocity += 0.1
            forward = True
        else:
            xpos -= (math.cos(math.radians(heading) - (math.pi / 2))) * maxvelocity
            ypos += (math.sin(math.radians(heading) - (math.pi / 2))) * maxvelocity
            forward = True
    if not forward:
        velocity = 0.1
    if keys[pygame.K_RIGHT]:
        pass
    drawScreen(spaceShip, heading, xpos, ypos)
