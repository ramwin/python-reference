# -*- coding: utf-8 -*-
def main(a,b):
    hex_of_a = str_to_hex(a)
    print("hex_of_a is:{0}".format(hex_of_a))
    hex_of_b = str_to_hex(b)
    print("hex_of_b is:{0}".format(hex_of_b))
    hex_of_ab = hex_xor(hex_of_a,hex_of_b)
    return hex_of_ab
def hex_xor(a,b):
    print(len(a))
    if (len(a) >= len(b)):
        print('a长')
        shorter, longer = b,a
    else:
        print('b长')
        shorter = a
        longer = b
    result = ''
    print shorter
    print longer
    for i in range(len(shorter)/2):
        print("i= {0}".format(i))
        result = result + single_hex_xor(shorter[2*i:2*i+2],longer[2*i:2*i+2])
    for i in range((len(longer)-len(shorter))/2):
        result = result + longer[2*i+len(shorter):2*i+len(shorter)+2]
    return result
def single_hex_xor(aa,bb):
    a = int(aa,16)
    b = int(bb,16)
    result = int(aa,16)^int(bb,16)
    return sing_int_to_hex(result)
def sing_int_to_hex(num):
    result = hex(num)
    if len(result)==3:
        return '0'+result[2:]
    else:
        return result[2:]
def str_to_hex(strs):   # 字符串变成十六进制的字符串
    result = ''
    for i in strs:
        result = result + chr_to_hex(i)
    return result
def chr_to_hex(char):   # 单个字符变成是十六进制的字符
    chr_hex = hex(ord(char))
    if len(chr_hex) == 3:
        return '0'+chr_hex[2]
    else:
        return chr_hex[2:]
def hex_to_chr(aa):
    result = ''
    for i in range(0,len(aa),2):
        result = result + chr( int(aa[i:i+2],16) )
    return result
