#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import sys

from src.controller.Reader import Reader
from src.view.Window import Window

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Controller:
    def __init__(self, filename):
        self.height = 400
        self.width = 500

        pygame.init()
        self.win = pygame.display.set_mode([self.width + 50, self.height + 50])
        pygame.display.set_caption('Visualizador')

        reader = Reader('resources/', self.width, self.height)
        polygons = reader.read_file(filename)

        font = pygame.font.SysFont('Arial', 20)

        map(lambda polygon: polygon.set_font(font), polygons)

        self.window = Window(self.win, polygons)

    def update(self):
        self.window.clean()
        self.window.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()









