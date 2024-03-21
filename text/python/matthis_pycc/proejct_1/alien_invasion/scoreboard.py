import pygame.font


class Scoreboard:
    """scoreboard class"""

    def __init__(self, ai_game):
        """initialize scorekeeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings for score info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare init score images
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # display score at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """turn high score into rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        # center high score at top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """draw score to screen"""
        self.screen.blit(self.score_image, self.score_rect)
