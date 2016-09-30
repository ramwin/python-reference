#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-13 13:48:47

import random


class Card(object):
    '''
        This is the object for a single Card
    '''

    def __init__(self, suit='spade', number=1):
        '''
            suit: 'spade', 'diamond', 'club', 'heart', 'joker'
            number: 1,2,3,4,5,6,7,8,9,10,11,12,13
            if the card belong to joker, 0 represent little joker, 1 another.
        '''
        self.suit = suit
        self.number = number

    def getscore(self):
        return self.number if self.number < 10 else 10

    def __str__(self):
        return '%s %d' % (self.suit, self.number)


class Deck(object):
    '''
        This is the object for deck
    '''

    def __init__(self, joker=False):
        # TODO I don't know how to randomly pick a card in set
        self.cards = []
        for suit in ['spade', 'diamond', 'club', 'heart']:
            for number in range(0, 13):
                self.cards.append(Card(suit=suit, number=number))
        if joker is True:
            self.cards.append(Card(suit='joker', number=0))
            self.cards.append(Card(suit='joker', number=1))

    def pop(self):
        return self.cards.pop(random.randint(0, len(self.cards) - 1))

    def __iter__(self):
        while len(self.cards) > 0:
            yield self.pop()


class Person(object):
    '''
        A person represent the playse
    '''

    def __init__(self, max_number=15):
        '''
            max_number: if the the current point >= max_number, the person will
            not want more card any more

            def get(self, card):
                give the person a card

            def getscore(self):
                get the scroe of the person

            def expire(self):
                return True if the person want more card

        '''
        self.number = max_number
        self.cards = []

    def get(self, card):
        self.cards.append(card)

    @property
    def score(self):
        score = 0
        for card in self.cards:
            score += card.getscore()
        return score

    def final_score(self):
        return self.score if self.score <= 21 else 0

    def expire(self):
        return self.score <= self.number


def agame(person, deck):
    while person.expire():
        person.get(deck.pop())
    return person.final_score()


def main():
    deck = Deck()
    for i in deck:
        print(i)


def single(n):
    times = 0
    score = 0
    zero_time = 0
    max_number = n
    for i in range(10000):
        a = Person(max_number=max_number)
        deck = Deck()
        times += 1
        tmp = agame(a, deck)
        if tmp == 0:
            zero_time += 1
        score += agame(a, deck)
    print('保险数字选择 %d' % max_number)
    print('超过21点的概率 %0.2f' % (zero_time / times))
    print('平均数值 %0.2f ' % (score / times))
    print('不为0的平均数值 %0.2f' % (score / (times - zero_time)))


if __name__ == '__main__':
    for i in range(15, 20):
        single(i)
