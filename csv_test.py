#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-04-21 10:31:45


import csv

def test_dictwriter():
    """使用dict来做header"""
    person1 = {
        'first_name': 'walter, ", ",联通',
        'last_name': 'white',
        'location': {
            'city': 'los angeles'
        }
    }
    person2 = {
        # 'first_name': 'jessic',
        # 'last_name': 'hellon',
        'location': {
            'city': 'huston',
        }
    }
    person3 = {
        # 'first_name': 'jessic',
        # 'last_name': 'hellon',
        'location': {
            'city': 'huston',
        }
    }
    persons = [person1, person2, person3]
    with open('test/dictwriter.csv', 'w', encoding="gbk") as csvfile:
        fieldnames = ['first_name', 'last_name', 'location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='raise')
        writer.writeheader()
        # writer.writerow(person1)
        # writer.writerow(person2)
        writer.writerows(persons)


def test_dynamic_header():
    """使用动态的header"""
    person1 = {
        # 'first_name': 'walter, ", ",',
        'last_name': 'white',
        'location': {
            'city': 'los angeles'
        }
    }
    person2 = {
        # 'first_name': 'jessic',
        # 'last_name': 'hellon',
        'location': {
            'city': 'huston',
        }
    }
    person3 = {
        # 'first_name': 'jessic',
        # 'last_name': 'hellon',
        'location': {
            'city': 'huston',
        }
    }
    persons = [person1, person2, person3]
    with open('test/dynamic_header.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name', 'location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='raise')
        writer.writeheader()
        # writer.writerow(person1)
        # writer.writerow(person2)
        writer.writerows(persons)

if __name__ == '__main__':
    test_dictwriter()
