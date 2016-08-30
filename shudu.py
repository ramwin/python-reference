# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pprint
def single(i,j,array,n):
    posible=array[i][j]
    otherrow = range(n)
    otherrow.remove(i)
    othercolumn = range(n)
    othercolumn.remove(j)
    for row in otherrow:
        if len(array[row][j]) ==1:
            try:
                posible.remove(array[row][j][0])
            except:
                pass
    for column in othercolumn:
        if len(array[i][column]) ==1:
            try:
                posible.remove(array[i][column][0])
            except:
                pass
    array[i][j]=posible
    return array            
def single2(i,j,array,n):
    t = array[:]
    allone = []
    for k in range(3*i,3*i+3):
        for l in range(3*j,3*j+3):
            if len(array[k][l])==1:
                allone.append(array[k][l][0])
    for k in range(3*i,3*i+3):
        for l in range(3*j,3*j+3):
            if len(array[k][l])>1:
                for m in allone:
                    try:
                        array[k][l].remove(m)
                    except:
                        pass
    return array

def insert(array,n):
    # 利用横竖不能有重复来判断
    for i in range(n):
        for j in range(n):
            array = single(i,j,array,n)
    # 利用一个小框里面不能有重复来判断 9宫格特有
    for i in range(3):
        for j in range(3):
            array = single2(i,j,array,n)
    return array
def main():
    n=9     # 设定几宫格
    file = open('shudu.csv','r')
    linelist = file.readlines()
    array = []
    for i in range(n):
        array.append([])
        for j in range(n):
            array[i].append([])
    for i in range(n):
        oneline = linelist[i][:-1].split(',')
        for j in range(n):
            try:
                array[i][j] = [int(oneline[j])]
            except:
                array[i][j] = [1,2,3,4,5,6,7,8,9]
    cont = True
    while cont:
        num = 0
        cont = False
        for i in range(n):
            for j in range(n):
                if len(array[i][j]) > 1:
                    num += 1
                    cont = True
        array = insert(array,9)
        import time
        time.sleep(1)
        print '还有%d个空格没填'%(num)   
        if num == 2:
            break
    return array
if __name__ == '__main__':
    list = main()
    pprint.pprint(list)
    # for i in len(list):
    #     for j in len(i):
    #         print(list[i][j]),
    #     print()
