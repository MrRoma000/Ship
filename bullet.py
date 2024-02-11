import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, SW):
        super().__init__()
        self.screen = SW.screen
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 1.0
        self.bullet_color = (60, 60, 60)
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midtop = SW.ship.rect.midtop
        self.y = float(self.rect.y)
    
    def update(self):
        self.y -= self.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)