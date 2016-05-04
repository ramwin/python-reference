#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-04-06 11:29:08

import datetime
import sqlite3
import redis

file_path = './test.db'
def main():
    '''不使用事务， 
        插入   100,000 数据需要3秒，
        插入 1,000,000 数据需要32秒'''
    start = datetime.datetime.now()
    conn = sqlite3.connect(file_path)
    for i in range(1000000):
        command = 'INSERT INTO TEST (NAME) VALUES ("%s")'%(str(i))
        conn.execute(command)
    conn.commit()
    end = datetime.datetime.now()
    print('耗时 %s 秒'%(end-start).seconds)

def main1():
    ''' 使用事务,
        插入   100,000 数据需要2秒,
        插入 1,000,000 数据需要27秒,
    '''
    start = datetime.datetime.now()
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    for i in range(1000000):
        command = 'INSERT INTO TEST (NAME) VALUES ("%s")'%(str(i))
        cursor.execute(command)
    conn.commit()
    end = datetime.datetime.now()
    print('耗时 %s 秒'%(end-start).seconds)

def main2():
    '''插入 1000000 条数据特别慢需要 273 秒'''
    r = redis.StrictRedis(host='localhost', port=6379,db=0)
    r.delete('test')
    start = datetime.datetime.now()
    for i in range(1000000):
        r.rpush('test', str(i))
    end = datetime.datetime.now()
    print('耗时 %s 秒'%(end-start).seconds)
if __name__ == '__main__':
    main2()
