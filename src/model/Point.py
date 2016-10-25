#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Point:
    def __init__(self, init_x, init_y, number):
        self.id = number
        self.pos_x = init_x
        self.pos_y = init_y
        self.original_tuple = (init_x, init_y)
        self.msg = None

    def set_font(self, font):
        self.msg = font.render(str(self.id), True, (255, 0, 0))

    def draw(self, bg):
        bg.blit(self.msg, (self.pos_x, self.pos_y))

    def translate_and_scale(self, x_mov, y_mov, x_scale, y_scale):
        self.pos_x += x_mov
        self.pos_y += y_mov
        self.pos_x *= x_scale
        self.pos_y *= y_scale
