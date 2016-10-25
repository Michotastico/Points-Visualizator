#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Polygon:
    def __init__(self, points):
        self.points = points
        self.list_points = list(map(lambda point: (point.pos_x, point.pos_y), self.points))

    def draw(self, bg):
        map(lambda point: point.draw(bg), self.points)
        pygame.draw.lines(bg, (0, 0, 128), True, self.list_points, 1)

    def set_font(self, font):
        map(lambda point: point.set_font(font), self.points)
