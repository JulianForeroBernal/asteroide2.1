import pygame
import math
from pygame.locals import *
from pygame.sprite import Sprite

class Bullet (Sprite):
    def __init__(self, pos, angle, vel, conten):
        self.vel = vel
        self.pos = pos
        self.conten = conten
        self.alcance = 25
        self.image = pygame.image.load("imagene/pequeña.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0], pos[1])
        self.angulo = angle


    def update(self): 
        self.alcance -=1
        self.vel[0]+= math.cos(math.radians((self.angulo)%360))
        self.vel[1]-= math.cos(math.radians((self.angulo)%360))
        self.rect = self.rect.move(self.vel)
        self.rect.x = self.rect.x % self.conten[0]
        self.rect.y = self.rect.y % self.conten[1]
