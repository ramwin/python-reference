#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-02-17 23:10:12

import re
file_path = './愚公移山游戏.txt'
def main():
    data_list = open(file_path,'r').readlines()
    title = data_list.pop(0)
    best_index = 0
    best = ''
    lowest_price = None
    for index,value in enumerate(data_list):
        name, level, speed, price = re.match(r'(.*)?:([\d.]+),([\d.]+),([\d.]+)\n$',value).groups()
        this_price = float(price)/float(speed)*float(level)
        if not lowest_price: 
            best = name
            lowest_price = this_price
        if this_price < lowest_price:
            lowest_price = this_price
            best = name
            best_index = index
    print('您现在应该购买的是:{0}'.format(best))
    new_level = input('现在您的 {0} 等级是:'.format(best))
    new_speed = input('现在您的 {0} 的生子速度是:'.format(best))
    new_price = input('现在您的 {0} 的价格是:'.format(best))
    data_list[best_index] = '{0}:{1},{2},{3}\n'.format(best,new_level,new_speed,new_price)
    file = open(file_path,'w')
    file.write(title)
    file.writelines(data_list)
    file.close()
    
if __name__ == '__main__':
    while True:
        main()
