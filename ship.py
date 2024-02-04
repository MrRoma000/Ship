import pygame


class Ship:
    def __init__(self, SW):
        self.screen = SW.screen
        self.screen_rect = SW.screen.get_rect()
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blit_ship(self):
        self.screen.blit(self.image, self.rect)