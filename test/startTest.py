import unittest
from unittest.mock import MagicMock
from alien_invasion import AlienInvasion


class StartTest(unittest.TestCase):
    def setUp(self):
        AlienInvasion()

    # def tearDown(self) -> None:
    #     exit(0)

    # 模拟鼠标点击事件
    def click_mouse_test(self):
        mouse_click = MagicMock()



