#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
import random
import six
if six.PY3:
    import configparser
    config = configparser.ConfigParser()
elif six.PY2:
    import ConfigParser
    config = ConfigParser.RawConfigParser()

# Please note that using RawConfigParser's set functions, you can assign
# non-string values to keys internally, but will receive an error when
# attempting to write to a file or when you get it in non-raw mode. Setting
# values using the mapping protocol or ConfigParser's set() does not allow
# such assignments to take place.
config.add_section('Section1')
config.set('Section1', 'an_int', '15')
config.set('Section1', 'a_bool', 'true')
config.set('Section1', 'a_float', str(random.random()))
config.set('Section1', 'baz', 'fun')
# config.set('Section1', 'bar', [1,2,3])
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')
config.setdefault('Section2', {'key': 'value'})
# config.set('Section2', 'key', 'value2')
config.set('Section2', 'spacevalue', 'space value')
config.set('Section2', 'space key', 'space value')
config.set('Section2', 'space key ', 'space value2')
config.set('Section2', ' space around ', ' space value ')

# Writing our configuration file to 'example.cfg'
with open('test.cfg', 'w') as configfile:
    config.write(configfile)



import configparser

config = configparser.ConfigParser()
config.read('test.cfg')
print("解析")
# print(config.get('Section2', 'spacevalue'))
print(config.get('Section2', 'space key'))
print("解析完成")
