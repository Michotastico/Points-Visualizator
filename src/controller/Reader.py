#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from src.model.Point import Point
from src.model.Polygon import Polygon

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Reader:
    def __init__(self, path, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        self.path = path

    def read_file(self, filename):
        text_file = open(self.path+filename, "r")
        number_points = int(text_file.readline())
        points = []
        polygons = []

        min_x = sys.maxsize
        max_x = -sys.maxsize - 1
        min_y = sys.maxsize
        max_y = -sys.maxsize - 1

        for i in range(number_points):
            line = text_file.readline().split()

            if max_x < float(line[0]):
                max_x = float(line[0])

            if max_y < float(line[1]):
                max_y = float(line[1])

            if min_x > float(line[0]):
                min_x = float(line[0])

            if min_y > float(line[1]):
                min_y = float(line[1])

            points.append(Point(float(line[0]), float(line[1]), i))

        number_segments = int(text_file.readline())
        for i in range(number_segments):
            line = text_file.readline()

        x_movement = -min_x
        y_movement = -min_y

        x_scale = self.width / (max_x + x_movement)
        y_scale = self.height / (max_y + y_movement)

        map(lambda point: point.translate_and_scale(x_movement, y_movement, x_scale, y_scale), points)

        number_polygons = int(text_file.readline())
        for i in range(number_polygons):
            line = text_file.readline().split()
            polygons.append(Polygon(list(map(lambda index: points[int(index)], line))))

        return polygons
