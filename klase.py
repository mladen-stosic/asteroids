import pygame
import math
from pygame import image as img


class Ship:

    def __init__(self, surface, heading, velocity, maxvelocity, xpos, ypos, forward):
        self.surface = surface
        self.heading = heading
        self.velocity = velocity
        self.maxvelocity = maxvelocity
        self.xpos = xpos
        self.ypos = ypos
        self.forward = forward
        self.image = 0
        self.acceleration = 0.1
        self.deceleration = 0.3


    def rotate(self, angle):
        self.heading += angle

    def move(self):

        self.xpos -= (math.cos(math.radians(self.heading) - (math.pi / 2))) * self.velocity
        self.ypos += (math.sin(math.radians(self.heading) - (math.pi / 2))) * self.velocity
        if self.forward:
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
        self.image = img.load('a-01.png')
        self.image = pygame.transform.scale(self.image, (50, 50))

    def fire(self):
        pass
