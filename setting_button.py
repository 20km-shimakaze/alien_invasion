import pygame


class SettingButton:
    def __init__(self, ai_game):
        """初始化按钮属性"""
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/settings.bmp')
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 15, 80
        self.button_color = (0, 255, 255)
        self.rect = pygame.Rect(0, 0, self.width, self.height)

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.blit(self.image, (self.width, self.height))
