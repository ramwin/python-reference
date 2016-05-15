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
        '''
        self.number = 15
        self.cards = []
        self.score = 0

    def get(self, card):
        self.cards.append(card)

    def getscore(self):
        for card in self.cards:
            self.score += card.getscore()


def main():
    deck = Deck()
    for i in deck:
        print(i.getscore())


if __name__ == '__main__':
    main()
