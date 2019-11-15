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


    def rotate(self, angle):
        self.heading += angle

    def move(self):
        if self.velocity < self.maxvelocity:
            self.xpos -= (math.cos(math.radians(self.heading) - (math.pi / 2))) * self.velocity
            self.ypos += (math.sin(math.radians(self.heading) - (math.pi / 2))) * self.velocity
            self.velocity += 0.1
            self.forward = True
        else:
            self.xpos -= (math.cos(math.radians(self.heading) - (math.pi / 2))) * self.maxvelocity
            self.ypos += (math.sin(math.radians(self.heading) - (math.pi / 2))) * self.maxvelocity
            self.forward = True

    def loadimg(self):
        self.image = img.load('a-01.png')
        self.image = pygame.transform.scale(self.image, (50, 50))

    def fire(self):
        pass
