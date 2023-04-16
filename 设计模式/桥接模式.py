#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging


logging.basicConfig(level=logging.INFO)


class DrawAPI:

    def draw_circle(radius: int, x: int, y: int):
        pass


class RedCircle(DrawAPI):

    def draw_circle(self, radius: int, x: int, y: int):
        logging.info(
            "画一个红色的圆, radius: %d, x: %d, y: %d",
            radius, x, y)


class GreenCircle(DrawAPI):

    def draw_circle(self, radius: int, x: int, y: int):
        logging.info(
            "画一个绿色的圆, radius: %d, x: %d, y: %d",
            radius, x, y)


class Shape:

    def __init__(self, draw_api):
        self.draw_api = draw_api


class Circle(Shape):

    def __init__(self, x: int, y: int, radius: int, draw_api: DrawAPI):
        super().__init__(draw_api=draw_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.draw_api.draw_circle(
            self.radius, self.x, self.y)


def main():
    red_circle: Shape = Circle(100, 100, 10, RedCircle())
    green_circle: Shape = Circle(100, 100, 10, GreenCircle())

    red_circle.draw()
    green_circle.draw()


if __name__ == "__main__":
    main()
