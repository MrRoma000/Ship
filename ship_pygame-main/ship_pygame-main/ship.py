import pygame


class Ship:
    def __init__(self, SW):
        self.screen = SW.screen
        self.screen_rect = SW.screen.get_rect()
        self.image = pygame.image.load("images/ship_resized.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.ship_speed = 1.5
        self.x = float(self.rect.x) # 250 -> 250.0

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.ship_speed
        self.rect.x = self.x

    def blit_ship(self):
        self.screen.blit(self.image, self.rect)
