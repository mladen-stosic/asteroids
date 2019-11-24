import pygame
import math
from pygame import image as img

class Asteroid():

    def __init__(self, surface, winWidth, winHeight, heading, xpos, ypos, velocity, radius, imageList):
        self.surface = surface
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.heading = heading
        self.velocity = velocity
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.imageList = imageList

    def updateImg(self):
        self.xpos -= (math.cos(math.radians(self.heading) - (math.pi / 2))) * self.velocity
        self.ypos += (math.sin(math.radians(self.heading) - (math.pi / 2))) * self.velocity

        # check if its in boundaries
        if ((self.x > self.winWidth) | (self.x < 0) | (self.y > self.winHeight) | (self.y < 0)):
            self.inBound = False
        if self.inBound:
            self.img = imageList[radius % 10]
