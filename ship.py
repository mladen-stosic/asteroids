import pygame
import math
from projectile import Projectile
from pygame import image as img


class Ship:

    def __init__(self, surface, heading, velocity, maxvelocity, xpos, ypos, forward, winWidth, winHeight):
        self.surface = surface
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.heading = heading
        self.velocity = velocity
        self.maxvelocity = maxvelocity
        self.xpos = xpos
        self.ypos = ypos
        self.forward = forward
        self.imagelist = []
        self.imagelist.append(img.load('spaceship0.png'))
        self.imagelist.append(img.load('spaceship1.png'))
        self.image = self.imagelist[0]
        self.acceleration = 0.1
        self.deceleration = 0.3
        self.fire = False
        self.center = [self.xpos, self.ypos]
        self.projectiles = []


    def rotate(self, angle):
        self.heading = self.heading % 360
        self.heading += angle

    def move(self):
        self.image = self.imagelist[0]
        self.center =  [self.xpos + 25, self.ypos + 25]
        self.xpos -= (math.cos(math.radians(self.heading) - (math.pi / 2))) * self.velocity
        self.ypos += (math.sin(math.radians(self.heading) - (math.pi / 2))) * self.velocity
        if self.forward:
            self.image = self.imagelist[1]
            if self.velocity < self.maxvelocity:
                self.velocity += self.acceleration
            else:
                self.velocity = self.maxvelocity
        elif self.velocity < 0:
            self.velocity = 0
        else:
            if self.velocity > 0:
                self.velocity -= self.deceleration

    def loadimg(self):

        self.image = pygame.transform.scale(self.image, (50, 50))


    def projectileInit(self):
        self.projectiles.append(Projectile(self.surface, self.winWidth, self.winHeight, self.xpos + 25, self.ypos + 25, self.heading, self.velocity))

    def projectileUpdate(self):

        i = 0
        while ((i <len(self.projectiles)) & (len(self.projectiles) > 0)):
            self.projectiles[i].updateImg()
            if not self.projectiles[i].inBound:
                self.projectiles.pop(i)
                if i > 1:
                    i-=1
            i+=1
        # if len(self.projectiles) > 0:
        #     for i in range(len(self.projectiles)):
        #         print(len(self.projectiles), i)
        #         self.projectiles[i].updateImg()
        #         if not self.projectiles[i].inBound:
        #             self.projectiles.pop(i)
