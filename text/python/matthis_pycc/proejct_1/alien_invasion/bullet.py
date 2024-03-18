from turtle import screensize
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage bullets from ship"""

    def __init__(self, ai_game):
        """Create bullet object at ship's position"""
        super().__init__()
        self.screen - ai_game.screen
        self.settings = ai_game.settings
        slef.color - self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet.width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal
        self.y = float(self.rect.y)
