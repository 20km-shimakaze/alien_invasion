import pygame
from pygame.sprite import Sprite
from random import randint
from settings import Settings


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        """初始化外星人并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图形并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings

        # 每个外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 存储外星人运动方向
        self.direct = randint(-1, 1)

    def update(self):
        self.x += self.direct * self.settings.alien_speed_x
        self.y += self.settings.alien_speed_y
        self.rect.x = self.x
        self.rect.y = self.y





