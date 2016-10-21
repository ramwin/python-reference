#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-09-29 14:00:38


class Card():
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()

    def printstr(self):
        print(str(self.hard) + "," + str(self.soft))


class NumberCard():
    def _points(self):
        return int(self.suit), int(self.rank)


class MyCard(NumberCard, Card):
    pass


if __name__ == '__main__':
    card = MyCard(3,4)
    card.printstr()
