#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-10 14:02:53

file = open('test.txt','w')
file.write('abcdef')
file.close()

file = open('test.txt','r+')
file.write('1')
file.write('2')
file.flush()
print(file.read(2))
file.seek(3,0)
file.write('3')
file.flush()
file.seek(3,0)
print(file.read(2))
# file.flush()
file.close()

file = open('test.txt','r')
print(file.read())
file.close()
