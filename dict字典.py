#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-04 09:58:15

dic = {'a':'b'}
'a' in dic  # 判断有没有key

def insertdata(dic, keys, value):        
    if len(keys) == 1:                   
        dic[keys[0]] = value             
        return 0                         
    if not keys[0] in dic:                   
        dic[keys[0]] = {}                
    insertdata(dic[keys[0]], keys[1:], value) 
insertdata(dic, ['key1','key2','key3'], 'ivalue')
print(dic.keys())
