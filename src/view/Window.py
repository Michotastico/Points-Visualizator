#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Window:
    def __init__(self, screen, polygons):
        self.bg = screen
        self.color = (255, 255, 255)
        self.polygons = polygons

    def clean(self):
        self.bg.fill(self.color)

    def draw(self):
        map(lambda polygon: polygon.draw(self.bg), self.polygons)
        pygame.display.flip()
