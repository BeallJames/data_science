from typing import Self


class GameStats:
    """track stats"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """initialize stats that can change during game"""
        self.ships_left = self.settings.ship_limit
