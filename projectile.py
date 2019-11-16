import pygame
import math
from pygame import image as img

class Projectile:

    def __init__(self, surface, winWidth, winHeight, x, y, heading, shipvel):
        self.surface = surface
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.x = x
        self.y = y
        self.r = 5
        self.heading = heading
        self.img = 0
        self.inBound = True
        self.projectileVelocity = shipvel + 4

    def updateImg(self):
        self.x -= (math.cos(math.radians(self.heading) - (math.pi / 2))) * self.projectileVelocity
        self.y += (math.sin(math.radians(self.heading) - (math.pi / 2))) * self.projectileVelocity
        if ((self.x > self.winWidth) | (self.x < 0) | (self.y > self.winHeight) | (self.y < 0)):
            self.inBound = False
        if self.inBound:
            self.img = pygame.draw.circle(self.surface, (255, 255, 255), [round(self.x), round(self.y)], self.r)
