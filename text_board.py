import pygame.font


class TextBoard:
    """显示得分信息的类"""
    def __init__(self, ai_game, x, y):
        """初始化显示得分涉及的属性"""
        self.score_rect = None
        self.score_imag = None
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.status = ai_game.status
        self.x = x
        self.y = y

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont("SimHei", 30)
        # 准备初始得分图像'
        self.prep_score(0)

    def prep_score(self, text):
        """将得分转换为渲染的图像"""
        score_str = str(text)
        self.score_imag = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # 在屏幕右上角显示得分
        self.score_rect = self.score_imag.get_rect()
        self.score_rect.left = self.x
        self.score_rect.top = self.y

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_imag, self.score_rect)

