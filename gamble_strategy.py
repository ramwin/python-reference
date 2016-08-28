#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-06-11 08:08:50

import random

class Person(object):
    def __init__(self, max_money=750, min_money=0, money=250):
        '''
            max_money: int, if a person win more than it, he will stop gambling
            min_money: int, if a person lose more than it, he will also stop 
            gambling
        '''
        self.max_money = max_money
        self.min_money = min_money
        self.money = money
        self.principal = money

    def go_on(self):
        '''
            return True if Person will continue the gamble
        '''
        return self.min_money < self.money < self.max_money

    def play_game(self):
        profit = random.randint(-10,10)
        self.money += profit

    def win(self):
        return self.money > self.principal

    def profit(self):
        return self.money - self.principal


def main():
    profit = 0
    win = 0
    lose = 0
    times = 100
    for i in range(times):
        a = Person()
        while a.go_on():
            a.play_game()
        if a.win():
            win += 1
        else:
            lose +=1
        profit += a.profit()
    print('该玩家一共玩了 %d 把，赢了 %d 把，输了 %d 把。胜率 %0.2f%%' % (times, win, lose, win*100/times))
    print('输赢: %d' % profit)
 

if __name__ == '__main__':
    main()
