class Settings:
    """储存游戏《外星人入侵》中所有设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 默认设置
        # 屏幕设置设置
        self.screen_width_default = 1200
        self.screen_height_default = 800
        self.bg_color_default = (230, 230, 230)
        self.ship_speed_default = 1.5
        # 子弹设置默认
        self.bullet_speed_default = 1.0
        self.bullet_width_default = 3
        self.bullet_height_default = 15
        self.bullet_color_default = (0, 0, 255)
        self.bullet_allowed_default = 400
        # 外星人设置默认
        self.alien_speed_x_default = 0.6
        self.alien_speed_y_default = 0.15
        self.alien_speed_add_default = 1000
        # 飞船设置
        self.ships_left_default = 2

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 5.7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 255)
        self.bullet_allowed = 400
        self.alien_points = 50

        # 外星人设置
        self.alien_speed_x = 4.5
        self.alien_speed_y = 2.3
        self.alien_speed_add = 100

        # 飞船设置
        self.ships_left = 2

        # 最大帧率设置
        self.max_fps = 300

        # 设置界面
        self.set_screen_width = 600
        self.set_screen_height = 500

