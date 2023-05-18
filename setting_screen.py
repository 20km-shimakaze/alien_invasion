import pygame


class SetScreen:
    """设置界面，调整一部分参数"""
    def __init__(self, ai_game):
        pygame.init()
        self.setting = ai_game.settings
        self.screen = pygame.display.set_mode((self.setting.set_screen_width, self.setting.set_screen_height))
        pygame.display.set_caption("setting")
