import sys
import time

from settings import Settings
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
from random import randint
from button import Button
from game_status import GameStatus
from time import sleep
from scoreboard import Scoreboard
import pygame.font
from text_board import TextBoard
import jsonUtils
from time_board import TimeBoard
from setting_button import SettingButton
from setting_screen import SetScreen


class AlienInvasion:
    """管理游戏资源和行为"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.status = GameStatus(self)
        self.sb = Scoreboard(self)
        self.alien_time = 0
        self.set_but = SettingButton(self)
        # self._creat_fleet()

        # 历史最高分
        self.json_data = self._get_json_data()

        # 左上角的最大分数
        self.best_score = TextBoard(self, 20, 20)
        self.best_score.prep_score('最高分：' + str(self.json_data['best']['score']))

        # 是否全屏
        self.full_screen = False

        # 时钟对象
        self.clock = pygame.time.Clock()

        # 创建play按钮
        self.play_button = Button(self, "Play")

        # 左上角显示游戏进行多少秒
        self.game_time = TimeBoard(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self.clock.tick(self.settings.max_fps)
            self._check_events()
            if self.status.game_active:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """响应案件和鼠标事件"""
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_settings_button(mouse_pos)

    def _check_settings_button(self, mouse_pos):
        """在玩家点击设置之后打开设置界面"""
        button_clicked = self.set_but.rect.collidepoint(mouse_pos)
        if button_clicked:
            pass
            ## 砍了
            # self.set_screen = SetScreen(self)

    def _check_play_button(self, mouse_pos):
        """在玩家点击Play之后开始游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.status.game_active:
            self.status.reset_status()
            self.status.game_active = True
            self.sb.prep_score()
            self.game_time.reset()
            self.aliens.empty()
            self.bullets.empty()
            # 隐藏鼠标
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向右移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            # 向上移动飞船
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # 向下移动飞船
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            self._exit_before()
            sys.exit()
        elif event.key == pygame.K_BACKQUOTE:
            # 按~切换是否全屏
            self.full_screen ^= True
            if self.full_screen:
                self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                self.settings.screen_width = self.screen.get_rect().width
                self.settings.screen_height = self.screen.get_rect().height
            else:
                self.settings.screen_width = self.settings.screen_width_default
                self.settings.screen_height = self.settings.screen_height_default
                self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            self._update_settings()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _fire_bullet(self):
        """创建一颗子弹，并加入到编组bullets中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        self.game_time.show()
        self.best_score.show_score()
        self.set_but.draw_button()
        #
        if not self.status.game_active:
            self.play_button.draw_button()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _get_json_data(self):
        return jsonUtils.read_json('data.json')

    def _update_settings(self):
        """更新屏幕大小"""
        self.ship.screen = self.screen
        self.ship.screen_rect = self.screen.get_rect()
        self.ship.settings = self.settings
        # 可以优化使得比例不变
        self.ship.rect.bottom = self.screen.get_rect().bottom

    def _update_bullets(self):
        """更新子弹位置并删除消失的子弹"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.status.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
        self.bullets.update()
        # 删除超过屏幕的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        """更新外星人位置信息和生成外星人"""
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._alien_hit()
        # 一定时间后随机生成一个外星人
        self.alien_time += 1
        if self.alien_time >= self.settings.alien_speed_add:
            self.alien_time %= self.settings.alien_speed_add
            self._creat_alien()

        # 判定击中情况
        for alien in self.aliens.copy():
            if alien.rect.bottom >= self.settings.screen_height:
                if self.settings.ships_left > 1:
                    self._alien_hit()
                else:
                    self.status.game_active = False
                    # 一局游戏结束，计算成绩
                    self._exit_before()

                    pygame.mouse.set_visible(True)
                self.aliens.remove(alien)
            elif alien.rect.left <= 0 or alien.rect.right >= self.settings.screen_width:
                alien.direct *= -1

    def _alien_hit(self):
        self.settings.ships_left -= 1
        if self.settings.ships_left <= 0:
            self.status.game_active = False
            # 一局游戏结束，计算成绩
            self._exit_before()
            pygame.mouse.set_visible(True)

        print('hit!')
        self.aliens.empty()
        self.bullets.empty()
        sleep(0.5)

    def _creat_fleet(self):
        """创建外星人"""
        alien = Alien(self)
        alien_with = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_with)
        # number_aliens_x = available_space_x // (2 * alien_with)

        # # 创建第一行外星人
        # for alien_number in range(number_aliens_x):
        #     self._creat_alien(alien_number)

    def _creat_alien(self):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        alien.x = randint(0, self.settings.screen_width - alien.rect.width)
        # alien_with = alien.rect.width
        # alien.x = alien_with + 2 * alien_with * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _exit_before(self):
        self._save_data()
        self.ship.rect.midbottom = self.screen.get_rect().midbottom

    def _save_data(self):
        if self.json_data['best']['score'] < self.status.score:
            self.json_data['best']['score'] = self.status.score
            self.json_data['best']['time'] = time.localtime()
            print("成绩更新！分数为", self.json_data['best']['score'])
        self.json_data['history'].append([{'time': time.localtime(), 'score': self.status.score}])
        self.best_score.prep_score('最高分：' + str(self.json_data['best']['score']))
        self.best_score.show_score()
        jsonUtils.write_json('data.json', self.json_data)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
