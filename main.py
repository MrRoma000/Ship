import pygame
import sys
from ship import Ship

WIDTH = 1280
HEIGHT = 720
BACKGROUND = (230, 230, 230)


class StarWars:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.ship = Ship(self)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(BACKGROUND)
            self.ship.blit_ship()
            pygame.display.flip()
if __name__ == "__main__":
    game = StarWars()
    game.run_game()