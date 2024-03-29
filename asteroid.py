import pygame
import math
from pygame import image as img

class Asteroid():

    def __init__(self, surface, winWidth, winHeight, heading, xpos, ypos, velocity, radius, image):
        self.surface = surface
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.heading = heading
        self.velocity = velocity
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.inBound = True
        self.image = image

    def updateImg(self):
        self.xpos -= (math.cos(math.radians(self.heading) - (math.pi / 2))) * self.velocity
        self.ypos += (math.sin(math.radians(self.heading) - (math.pi / 2))) * self.velocity

        # check if its in boundaries
        if ((self.xpos + 2*self.radius > self.winWidth) | (self.xpos < 0) | (self.ypos + 2*self.radius > self.winHeight) | (self.ypos < 0)):
             self.inBound = False

    def center(self):
        return (self.xpos + self.radius, self.ypos + self.radius)

    def draw(self):
        self.surface.blit(self.image, (self.xpos, self.ypos))

