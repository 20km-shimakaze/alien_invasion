class GameStatus:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化信息"""
        self.settings = ai_game.settings
        self.reset_status()
        self.score = 0
        self.game_active = False

    def reset_status(self):
        """初始化再游戏运行期间可能有变化的统计信息"""

        # 子弹设置
        self.settings.bullet_speed = self.settings.bullet_speed_default
        self.settings.bullet_width = self.settings.bullet_width_default
        self.settings.bullet_height = self.settings.bullet_height_default
        self.settings.bullet_color = self.settings.bullet_color_default
        self.settings.bullet_allowed = self.settings.bullet_allowed_default

        # 外星人设置
        self.settings.alien_speed_x = self.settings.alien_speed_x_default
        self.settings.alien_speed_y = self.settings.alien_speed_y_default
        self.settings.alien_speed_add = self.settings.alien_speed_add_default

        # 飞船设置
        self.settings.ships_left = self.settings.ships_left_default
        
        self.score = 0
