#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

from src.controller.Controller import Controller

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


program = Controller('.txt')

while True:
    program.update()
    pygame.time.wait(1000/30)
