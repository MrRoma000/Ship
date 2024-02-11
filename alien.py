import pygame
import random


class Alien():
    def __init__(self, SW):
        self.screen = SW.screen
        self.image = pygame.image.load('images/spirit_breaker_resized.png')
        self.rect = self.image.get_rect()
        self.screen_rect = SW.screen.get_rect()
        self.alien_speed = 0.5

        self.y = float(self.rect.y)
    def update_alien(self):
        if self.rect.bottom < self.screen_rect.bottom:
            self.y += self.alien_speed
        if self.rect.bottom == self.screen_rect.bottom:
            self.screen.blit(self.image, (random.randint(0,self.screen_rect.right),0), self.rect)
        self.rect.y = self.y
    def blit_alien(self):
        self.screen.blit(self.image, self.rect)