import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    def __init__(self, SW):
        super().__init__()
        self.screen = SW.screen
        self.image =  pygame.image.load("images\spirit_breaker.png")
        self.rect = self.image.get_rect()
        self.screen_rect = SW.screen.get_rect()
        #self.alien_speed = 0.5

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

        """def update_alien(self):
        if self.rect.bottom < self.screen_rect.bottom:
            self.y +=  self.alien_speed
        if self.rect.bottom == self.screen_rect.bottom:
            self.screen.blit(self.image,self.rect)
        self.rect.y = self.y"""

    """    def blit_alien(self):
        self.screen.blit(self.image, self.rect)"""

