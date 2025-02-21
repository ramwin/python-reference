#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-03-24 11:49:54


import six
import os
import os
if os.path.isfile('combine.cfg'):
    os.remove('combine.cfg')


filename = 'combine.cfg'
if six.PY2:
    import ConfigParser
    config = ConfigParser.RawConfigParser()
elif six.PY3:
    import configparser
    config = configparser.RawConfigParser()

config.read(filename)

# 创建配置文件
config.add_section('Section1')
config.set('Section1', 'AN_INT', '15')
config.set('Section1', 'a_bool', 'true')
config.set('Section1', 'a_float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

# 测试几个section的通信, 不可以。python3的extend才可以
# config.add_section('Basic')
# config.set('Basic', 'host', 'localhot')
# config.set('Section1', 'usebasic', '%(Basic:host)s')
config.set('Section1', 'host', 'ramwin8001')
config.set('Section1', 'port', '8001')
config.set('Section1', 'url', 'http://%(host)s:%(port)s/api/v1/oauth/permission')

with open(filename, 'w') as configfile:
    config.write(configfile)

# 读取配置文件

if six.PY2:
    config = ConfigParser.ConfigParser()
elif six.PY3:
    config = configparser.ConfigParser()

config.read(filename)
if six.PY2:
    print(config.get('Section1', 'foo', 0))
    print(config.get('Section1', 'foo', 1))
    print(config.get('Section1', 'foo'))  # 默认开启
    # print(config.get('Section1',' usebasic'))
    print(config.get('Section1', 'url'))
    print(config.get('Section1', 'AN_INT'))
elif six.PY3:
    print(config.get('Section1', 'foo', raw=False))
