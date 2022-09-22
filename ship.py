import pygame
import math
from pygame import image as img


class Ship:

    def __init__(self, surface, heading, velocity, maxvelocity, xpos, ypos, forward, left, right, winWidth, winHeight, imagelist):
        self.surface = surface
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.heading = heading
        self.velocity = velocity
        self.maxvelocity = maxvelocity
        self.xpos = xpos
        self.ypos = ypos
        self.forward = forward
        self.left = left
        self.right = right
        self.imagelist = imagelist
        self.image = self.imagelist[0]
        self.acceleration = 0.1
        self.deceleration = 0.3
        self.fire = False

    def rotate(self, angle):
        self.heading = self.heading % 360
        self.heading += angle

    def move(self):
        self.image = self.imagelist[0]
        self.center =  [self.xpos + 36, self.ypos + 36]
        self.xpos -= (math.cos(math.radians(self.heading) - (math.pi / 2))) * self.velocity
        self.ypos += (math.sin(math.radians(self.heading) - (math.pi / 2))) * self.velocity
        if self.forward:
            if self.right:
                self.image = self.imagelist[3]
            elif self.left:
                self.image = self.imagelist[2]
            else:
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
        if self.xpos < 0:
            self.xpos = self.winWidth - 36
        if self.xpos > self.winWidth:
            self.xpos = 0
        if self.ypos < 0:
            self.ypos = self.winHeight
        if self.ypos > self.winHeight:
            self.ypos = 0

    def loadimg(self):
        self.image = pygame.transform.scale(self.image, (50, 50))

    def destroy(self, game_over):
        # animate
        return pygame.QUIT