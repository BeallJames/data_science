import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """a class for a single alien"""

    def __init__(self, ai_game):
        """initial alien set position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load image and set rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # start new at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien's horizontal pos
        self.x = float(self.rect.x)

    def update(self):
        """move right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
