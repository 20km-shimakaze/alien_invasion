import time
import pygame as pg
from text_board import TextBoard


class TimeBoard:
    def __init__(self, ai_game):
        self.start = time.time()
        self.end = time.time()
        self.x = 20
        self.y = 50
        self.board = TextBoard(ai_game, self.x, self.y)
        self.ai_game = ai_game

    def prep(self):
        self.board.prep_score('时间：'+str('{:.1f}'.format(self.end - self.start)))
        # self.board.prep_score(str(self.end - self.start))

    def show(self):
        self.end = time.time()
        if not self.ai_game.status.game_active:
            self.start = time.time()
        self.prep()
        self.board.show_score()

    def reset(self):
        self.start = time.time()
        self.end = time.time()
