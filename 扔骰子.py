#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2019-02-06 12:35:47

# 结果见 /results/扔骰子.png

import random


POINTS = [1, 2, 3, 4, 5, 6]
BAOZI = 100
MAX = 7
STAKE = 1


class Throw(object):

    def __init__(self):
        self.x = self.y = self.z = None
        pass

    def throw(self):
        self.x = random.choice(POINTS)
        self.y = random.choice(POINTS)
        self.z = random.choice(POINTS)

    def is_valid(self):
        if {self.x, self.y, self.z} == {1,2,3}:
            return True
        if {self.x, self.y, self.z} == {4,5,6}:
            return True
        if len({self.x, self.y, self.z}) == 2:
            return True
        if self.x == self.y == self.z != None:
            return True
        return False

    def __str__(self):
        if not self.is_valid():
            return "还没扔呢"
        if self.value == BAOZI:
            return "豹:{}".format(self.x)
        if self.value == MAX:
            return "4,5,6"
        if self.value == 0:
            return "洞宫"
        else:
            return "{}头".format(self.value)

    def throw_to_valid(self):
        while not self.is_valid():
            self.throw()

    @property
    def value(self):
        """返回结果"""
        assert self.is_valid()
        if self.x is None:
            raise Exception("还没扔呢")
        if {self.x, self.y, self.z} == {1,2,3}:
            return 0
        if {self.x, self.y, self.z} == {4,5,6}:
            return MAX
        if self.x == self.y == self.z != None:
            return BAOZI
        if self.x == self.y:
            return self.z
        if self.x == self.z:
            return self.y
        if self.y == self.z:
            return self.x

    def __gt__(self, other):
        return self.value > other.value


class Person(object):

    def __init__(self, is_host=False, money=0):
        self.is_host = is_host
        self.money = money
        pass

    def throw(self):
        t = Throw()
        t.throw_to_valid()
        self.dice = t
        return t

    def compare(self, host):
        assert host.is_host == True
        if self.dice.value == BAOZI:
            self.money += STAKE * 2
            host.money -= STAKE * 2
            return True
        elif self.dice.value == MAX:
            self.money += STAKE
            host.money -= STAKE
        elif self.dice.value == 6:
            self.money += STAKE
            host.money -= STAKE
        elif self.dice.value > host.dice.value:
            self.money += STAKE
            host.money -= STAKE
        elif self.dice.value < host.dice.value:
            self.money -= STAKE
            host.money += STAKE
        elif self.dice.value == host.dice.value:
            self.money -= STAKE
            host.money += STAKE


if __name__ == '__main__':
    host = Person(is_host=True, money=100)
    guest = Person(is_host=False, money=100)
    for i in range(20):
        guest_dice = guest.throw()
        host_dice = host.throw()
        print("客家结果: {}".format(guest_dice), end="\t")
        print(guest_dice.x, guest_dice.y, guest_dice.z, end="\t")
        print("庄家结果: {}".format(host_dice), end="\t")
        print(host_dice.x, host_dice.y, host_dice.z, end="\t")
        guest.compare(host)
        print("客家余额: {}".format(guest.money), end="\t")
        print("庄家余额: {}".format(host.money), end="\n")
